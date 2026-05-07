import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLAN_PATH = ROOT / "docs" / "moonn-h1-h2-ui-apply-plan-2026-05-06.json"
BLOCK_MAP_PATH = ROOT / "docs" / "moonn-h1-h2-block-map-2026-05-06.json"
PACKET_PATH = ROOT / "docs" / "moonn-h1-h2-source-cleanup-packet-2026-05-06.json"
OUT_PATH = ROOT / "docs" / "moonn-global-semantic-heading-layer-2026-05-06.html"
ASSET_PATH = ROOT / "assets" / "moonn-semantic-heading-layer.js"


def path_from_url(url: str) -> str:
    return url.replace("https://moonn.ru", "") or "/"


def first_title_candidate(blocks: list[dict]) -> dict | None:
    generic = {
        "психолог татьяна мунн",
        "что говорит наука",
        "как применять эмоциональный интеллект на практике",
        "когда обратиться к психологу:",
    }
    for block in blocks:
        for text in block.get("textCandidates", []):
            normalized = " ".join(text.lower().split())
            if normalized and normalized not in generic:
                return {"recId": str(block["recId"]), "text": text}
    return None


def main() -> int:
    plan = json.loads(PLAN_PATH.read_text(encoding="utf-8"))
    block_map = json.loads(BLOCK_MAP_PATH.read_text(encoding="utf-8"))
    packet = json.loads(PACKET_PATH.read_text(encoding="utf-8"))
    packet_by_url = {item["url"]: item for item in packet["items"]}
    skipped_by_url = {item["url"]: item for item in plan.get("skipped", [])}

    items_by_key = {}
    for action in plan["actions"]:
        item = {
            "path": path_from_url(action["url"]),
            "recId": str(action["recId"]),
            "tag": action["setTag"].lower(),
            "text": action.get("visibleSignal", ""),
            "source": "ui-apply-plan",
        }
        items_by_key[(item["path"], item["recId"], item["tag"], item["text"])] = item

    # Add missing-H1 pages that were skipped by the conservative UI plan only when
    # there is a plausible existing visible page title. Weak/date/time/zero-block
    # signals stay in the manual bucket because making them H1 would hurt SEO.
    for mapped in block_map["items"]:
        source = packet_by_url.get(mapped["url"], {})
        path = path_from_url(mapped["url"])
        if "missing_h1" not in source.get("issues", []):
            continue
        if any(item["path"] == path and item["tag"] == "h1" for item in items_by_key.values()):
            continue
        skipped = skipped_by_url.get(mapped["url"], {})
        if skipped and skipped.get("reason") not in {"descriptive_signal_without_token_match"}:
            continue
        candidate = first_title_candidate(mapped.get("relevantBlocks", []))
        if not candidate:
            continue
        item = {
            "path": path,
            "recId": candidate["recId"],
            "tag": "h1",
            "text": candidate["text"],
            "source": "block-map-missing-h1",
        }
        items_by_key[(item["path"], item["recId"], item["tag"], item["text"])] = item

    # Home page has several section H1s in raw Tilda markup; use the existing
    # visible brand/person signal as the single rendered H1 and demote sections.
    for mapped in block_map["items"]:
        if mapped["url"] != "https://moonn.ru/":
            continue
        candidate = first_title_candidate(mapped.get("relevantBlocks", []))
        if not candidate:
            continue
        item = {
            "path": "/",
            "recId": candidate["recId"],
            "tag": "h1",
            "text": candidate["text"],
            "source": "home-person-h1",
        }
        items_by_key[(item["path"], item["recId"], item["tag"], item["text"])] = item

    # For pages that already have several H1 tags, enforce one rendered H1. If a
    # page-level H1 is explicitly promoted above, all other H1s are downgraded.
    # Otherwise, the first existing H1 remains and the rest are downgraded.
    page_rules = []
    for mapped in block_map["items"]:
        source = packet_by_url.get(mapped["url"], {})
        if "multiple_h1" not in source.get("issues", []):
            continue
        path = path_from_url(mapped["url"])
        current_h1_texts = source.get("currentH1", [])
        promoted = [item for item in items_by_key.values() if item["path"] == path and item["tag"] == "h1"]
        page_rules.append(
            {
                "path": path,
                "mode": "single-h1",
                "keepRecId": promoted[0]["recId"] if promoted else None,
                "keepText": promoted[0]["text"] if promoted else (current_h1_texts[0] if current_h1_texts else ""),
                "source": "multiple-h1-normalizer",
            }
        )

    items = list(items_by_key.values())
    payload = json.dumps(items, ensure_ascii=False, separators=(",", ":"))
    page_rules_payload = json.dumps(page_rules, ensure_ascii=False, separators=(",", ":"))
    js = f"""(function(){{
  var MOONN_HEADING_MAP = {payload};
  var MOONN_PAGE_RULES = {page_rules_payload};
  function norm(s){{return (s||'').replace(/\\s+/g,' ').trim().toLowerCase();}}
  function samePath(a,b){{return ((a||'/').replace(/\\/$/,'')||'/')===((b||'/').replace(/\\/$/,'')||'/');}}
  function replaceTag(el, tag){{
    if(!el || el.tagName.toLowerCase()===tag) return;
    var next=document.createElement(tag);
    for(var i=0;i<el.attributes.length;i++){{var a=el.attributes[i]; next.setAttribute(a.name,a.value);}}
    next.innerHTML=el.innerHTML;
    el.parentNode.replaceChild(next,el);
  }}
  function apply(){{
    var path=location.pathname.replace(/\\/$/,'') || '/';
    MOONN_HEADING_MAP.forEach(function(item){{
      var itemPath=(item.path||'/').replace(/\\/$/,'') || '/';
      if(!samePath(itemPath,path)) return;
      var rec=document.getElementById('rec'+item.recId);
      if(!rec) return;
      var candidates=Array.prototype.slice.call(rec.querySelectorAll('[field="title"],[field="btitle"],.js-block-header-title,.t-title,h1,h2'));
      var target=candidates.find(function(el){{return norm(el.textContent)===norm(item.text);}})
        || candidates.find(function(el){{return norm(el.textContent).indexOf(norm(item.text).slice(0,24))!==-1;}})
        || candidates[0];
      if(target) replaceTag(target,item.tag);
    }});
    MOONN_PAGE_RULES.forEach(function(rule){{
      if(!samePath(rule.path,path)) return;
      var h1s=Array.prototype.slice.call(document.querySelectorAll('h1'));
      if(h1s.length<=1) return;
      var keep=null;
      if(rule.keepRecId){{
        var rec=document.getElementById('rec'+rule.keepRecId);
        if(rec) keep=Array.prototype.slice.call(rec.querySelectorAll('h1')).find(function(el){{return !rule.keepText || norm(el.textContent)===norm(rule.keepText);}})
          || rec.querySelector('h1');
      }}
      if(!keep && rule.keepText) keep=h1s.find(function(el){{return norm(el.textContent)===norm(rule.keepText);}});
      if(!keep) keep=h1s[0];
      h1s.forEach(function(el){{if(el!==keep) replaceTag(el,'h2');}});
    }});
  }}
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',apply); else apply();
  window.addEventListener('load',apply);
}})();"""
    code = f"""<!-- moonn-semantic-heading-layer:start -->
<script>
{js}
</script>
<!-- moonn-semantic-heading-layer:end -->"""
    OUT_PATH.write_text(code, encoding="utf-8")
    ASSET_PATH.write_text(js + "\n", encoding="utf-8")
    print(json.dumps({"items": len(items), "pageRules": len(page_rules), "html_bytes": len(code), "asset_bytes": len(js)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
