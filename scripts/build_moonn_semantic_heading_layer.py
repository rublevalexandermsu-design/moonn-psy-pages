import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLAN_PATH = ROOT / "docs" / "moonn-h1-h2-ui-apply-plan-2026-05-06.json"
OUT_PATH = ROOT / "docs" / "moonn-global-semantic-heading-layer-2026-05-06.html"
ASSET_PATH = ROOT / "assets" / "moonn-semantic-heading-layer.js"


def main() -> int:
    plan = json.loads(PLAN_PATH.read_text(encoding="utf-8"))
    items = []
    for action in plan["actions"]:
        items.append(
            {
                "path": action["url"].replace("https://moonn.ru", "") or "/",
                "recId": action["recId"],
                "tag": action["setTag"].lower(),
                "text": action.get("visibleSignal", ""),
            }
        )

    payload = json.dumps(items, ensure_ascii=False, separators=(",", ":"))
    js = f"""(function(){{
  var MOONN_HEADING_MAP = {payload};
  function norm(s){{return (s||'').replace(/\\s+/g,' ').trim().toLowerCase();}}
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
      if(itemPath!==path) return;
      var rec=document.getElementById('rec'+item.recId);
      if(!rec) return;
      var candidates=Array.prototype.slice.call(rec.querySelectorAll('[field="title"],[field="btitle"],.js-block-header-title,.t-title,h1,h2'));
      var target=candidates.find(function(el){{return norm(el.textContent)===norm(item.text);}})
        || candidates.find(function(el){{return norm(el.textContent).indexOf(norm(item.text).slice(0,24))!==-1;}})
        || candidates[0];
      if(target) replaceTag(target,item.tag);
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
    print(json.dumps({"items": len(items), "html_bytes": len(code), "asset_bytes": len(js)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
