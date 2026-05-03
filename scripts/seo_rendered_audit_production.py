import argparse
import json
from pathlib import Path

from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCOPE = ROOT / "registry" / "tilda" / "moonn-production-83-rollout.json"
DEFAULT_OUT = ROOT / "registry" / "seo" / "moonn-production-83-rendered-seo-audit.json"


def load_pages(scope_path: Path) -> list[dict]:
    pages = json.loads(scope_path.read_text(encoding="utf-8"))
    if not isinstance(pages, list):
        raise ValueError(f"Scope must be a list: {scope_path}")
    return pages


def audit_page(page, url: str, timeout_ms: int) -> dict:
    response = page.goto(url, wait_until="domcontentloaded", timeout=timeout_ms)
    page.wait_for_timeout(1800)
    return page.evaluate(
        """(url) => {
            const links = Array.from(document.querySelectorAll('a[href]')).map((a) => a.getAttribute('href') || '');
            const images = Array.from(document.querySelectorAll('img')).filter((img) => {
                const src = img.getAttribute('src') || '';
                if (/mc\\.yandex\\.ru\\/watch\\//i.test(src)) return false;
                if (/res\\.smartwidgets\\.ru\\/res\\/sw_logo_/i.test(src)) return false;
                if (/^data:image\\//i.test(src) && img.closest('noscript')) return false;
                return true;
            });
            const jsonLd = Array.from(document.querySelectorAll('script[type="application/ld+json"]'));
            return {
                url,
                http_status: window.__codexResponseStatus || null,
                title: document.title || '',
                canonical: document.querySelector('link[rel="canonical"]')?.href || '',
                enhancer_script: !!document.querySelector('script[src*="moonn-seo-aeo-enhancer.js"]'),
                rendered_jsonld: !!document.getElementById('moonn-rendered-jsonld'),
                jsonld_count: jsonLd.length,
                bad_links: links.filter((href) =>
                    /^http:\\/\\/wa\\.me\\//i.test(href) ||
                    /^http:\\/\\/twa\\.me\\//i.test(href) ||
                    /^http:\\/\\/\\.moonn\\.ru/i.test(href) ||
                    /^\\/http:\\/\\/wa\\.me\\//i.test(href)
                ),
                missing_alt_count: images.filter((img) => !(img.getAttribute('alt') || '').trim()).length,
                lazy_missing_count: images.filter((img) => !img.getAttribute('loading')).length,
                body_text_len: (document.body?.innerText || '').trim().length
            };
        }""",
        url,
    ) | {"network_status": response.status if response else None}


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit rendered Moonn production pages after Tilda SEO/AEO enhancer loads.")
    parser.add_argument("--scope", default=str(DEFAULT_SCOPE.relative_to(ROOT)))
    parser.add_argument("--out", default=str(DEFAULT_OUT.relative_to(ROOT)))
    parser.add_argument("--timeout-ms", type=int, default=45000)
    args = parser.parse_args()

    pages = load_pages(ROOT / args.scope)
    results = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/147.0.0.0 Safari/537.36"
            ),
            viewport={"width": 1440, "height": 1200},
        )
        for item in pages:
            page = context.new_page()
            try:
                result = audit_page(page, item["production_url"], args.timeout_ms)
                result.update(
                    {
                        "alias": item.get("alias"),
                        "source_page_id": item.get("source_page_id"),
                    }
                )
            except Exception as exc:
                result = {
                    "alias": item.get("alias"),
                    "source_page_id": item.get("source_page_id"),
                    "url": item.get("production_url"),
                    "error": str(exc),
                }
            finally:
                page.close()
            results.append(result)
        browser.close()

    summary = {
        "page_count": len(results),
        "error_count": sum(1 for item in results if item.get("error")),
        "enhancer_missing_count": sum(1 for item in results if not item.get("enhancer_script")),
        "rendered_jsonld_missing_count": sum(1 for item in results if not item.get("rendered_jsonld")),
        "bad_link_pages": sum(1 for item in results if item.get("bad_links")),
        "missing_alt_pages": sum(1 for item in results if item.get("missing_alt_count", 0) > 0),
        "lazy_missing_pages": sum(1 for item in results if item.get("lazy_missing_count", 0) > 0),
    }
    payload = {"summary": summary, "results": results}
    out = ROOT / args.out
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False))
    return 0 if summary["error_count"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
