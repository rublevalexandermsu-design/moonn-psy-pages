import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "registry" / "seo" / "moonn-production-83-schema-snippets.json"
AUDIT = ROOT / "registry" / "seo" / "moonn-production-83-seo-audit.json"
OUT = ROOT / "assets" / "moonn-seo-aeo-enhancer.js"


def extract_json_ld(snippet: str) -> dict:
    match = re.search(r'<script type="application/ld\+json">\s*(.*?)\s*</script>', snippet, flags=re.DOTALL)
    if not match:
        raise ValueError("JSON-LD script not found")
    return json.loads(match.group(1))


def path_key(url: str) -> str:
    return re.sub(r"/+$", "", url.replace("https://moonn.ru", "")) or "/"


def main() -> int:
    schema_manifest = json.loads(SCHEMA.read_text(encoding="utf-8"))
    audit = json.loads(AUDIT.read_text(encoding="utf-8"))
    page_meta = {}
    for page in audit["pages"]:
        page_meta[path_key(page["url"])] = {
            "title": page["title"],
            "description": page["description"],
            "alias": page["alias"],
            "url": page["url"],
        }

    schemas = {}
    for item in schema_manifest["snippets"]:
        schema = extract_json_ld(item["snippet"])
        schemas[path_key(item["url"])] = {
            "marker": item["marker"],
            "schema": schema,
        }

    payload = {
        "generated_at": "2026-05-02",
        "scope": "moonn-production-83",
        "schemas": schemas,
        "page_meta": page_meta,
    }

    js = f"""/*
  Moonn production SEO/AEO enhancer.
  Generated from registry/seo/moonn-production-83-schema-snippets.json.
  Purpose: rendered-DOM SEO support for Tilda pages while source-level block cleanup is pending.
*/
(function () {{
  'use strict';
  var PAYLOAD = {json.dumps(payload, ensure_ascii=False, separators=(",", ":"))};

  function normalizedPath() {{
    var path = window.location.pathname || '/';
    path = path.replace(/\\/+$/, '');
    return path || '/';
  }}

  function findPageData() {{
    var path = normalizedPath();
    return PAYLOAD.schemas[path] || PAYLOAD.schemas[path + '/'] || PAYLOAD.schemas['/'];
  }}

  function findPageMeta() {{
    var path = normalizedPath();
    return PAYLOAD.page_meta[path] || PAYLOAD.page_meta[path + '/'] || PAYLOAD.page_meta['/'] || {{}};
  }}

  function ensureMeta(name, content) {{
    if (!content) return;
    var selector = 'meta[name=\"' + name + '\"]';
    var node = document.head.querySelector(selector);
    if (!node) {{
      node = document.createElement('meta');
      node.setAttribute('name', name);
      document.head.appendChild(node);
    }}
    if (!node.getAttribute('content')) {{
      node.setAttribute('content', content);
    }}
  }}

  function injectSchema() {{
    var page = findPageData();
    if (!page || !page.schema || document.getElementById('moonn-rendered-jsonld')) return;
    var script = document.createElement('script');
    script.type = 'application/ld+json';
    script.id = 'moonn-rendered-jsonld';
    script.setAttribute('data-moonn-seo-marker', page.marker);
    script.text = JSON.stringify(page.schema);
    document.head.appendChild(script);
  }}

  function fixLinks() {{
    Array.prototype.forEach.call(document.querySelectorAll('a[href]'), function (link) {{
      var href = link.getAttribute('href') || '';
      var next = href;
      next = next.replace(/^http:\\/\\/wa\\.me\\/79777770303/i, 'https://wa.me/79777770303');
      next = next.replace(/^http:\\/\\/twa\\.me\\/79777770303/i, 'https://wa.me/79777770303');
      next = next.replace(/^http:\\/\\/\\.moonn\\.ru/i, 'https://moonn.ru');
      next = next.replace(/^\\/http:\\/\\/wa\\.me\\/\\+?79777770303/i, 'https://wa.me/79777770303');
      if (next !== href) {{
        link.setAttribute('href', next);
        link.setAttribute('data-moonn-link-fixed', '1');
      }}
      if (/^https:\\/\\/wa\\.me\\//i.test(next)) {{
        link.setAttribute('rel', 'nofollow noopener');
      }}
    }});
  }}

  function improveImages() {{
    var meta = findPageMeta();
    var title = meta.title || document.title || 'Татьяна Мунн, психолог МГУ';
    Array.prototype.forEach.call(document.querySelectorAll('img'), function (img, index) {{
      var alt = (img.getAttribute('alt') || '').trim();
      if (!alt || alt === 'image' || alt === 'photo') {{
        img.setAttribute('alt', title + ' - изображение ' + (index + 1));
        img.setAttribute('data-moonn-alt-fixed', '1');
      }}
      if (!img.getAttribute('loading')) {{
        img.setAttribute('loading', 'lazy');
      }}
      if (!img.getAttribute('decoding')) {{
        img.setAttribute('decoding', 'async');
      }}
    }});
  }}

  function improveHead() {{
    var meta = findPageMeta();
    ensureMeta('author', 'Татьяна Мунн');
    ensureMeta('publisher', 'Татьяна Мунн');
    ensureMeta('robots', 'index, follow, max-image-preview:large');
    ensureMeta('theme-color', '#f4d8ee');
    if (meta.description) ensureMeta('abstract', meta.description);
  }}

  function run() {{
    injectSchema();
    fixLinks();
    improveImages();
    improveHead();
    document.documentElement.setAttribute('data-moonn-seo-aeo-enhanced', PAYLOAD.scope);
  }}

  if (document.readyState === 'loading') {{
    document.addEventListener('DOMContentLoaded', run);
  }} else {{
    run();
  }}
}}());
"""
    OUT.write_text(js, encoding="utf-8")
    print(json.dumps({"out": str(OUT.relative_to(ROOT)), "bytes": OUT.stat().st_size}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
