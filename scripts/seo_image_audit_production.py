import argparse
import csv
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import urlparse

from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCOPE = ROOT / "registry" / "tilda" / "moonn-production-83-rollout.json"
DEFAULT_JSON_OUT = ROOT / "registry" / "seo" / "moonn-production-83-image-seo-audit.json"
DEFAULT_CSV_OUT = ROOT / "registry" / "seo" / "moonn-production-83-image-seo-audit.csv"

CYR = {
    "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e", "ё": "e",
    "ж": "zh", "з": "z", "и": "i", "й": "y", "к": "k", "л": "l", "м": "m",
    "н": "n", "о": "o", "п": "p", "р": "r", "с": "s", "т": "t", "у": "u",
    "ф": "f", "х": "h", "ц": "c", "ч": "ch", "ш": "sh", "щ": "sch", "ъ": "",
    "ы": "y", "ь": "", "э": "e", "ю": "yu", "я": "ya",
}


def slugify(value: str, max_len: int = 92) -> str:
    value = (value or "").lower().replace("—", " ").replace("–", " ")
    value = "".join(CYR.get(ch, ch) for ch in value)
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-{2,}", "-", value).strip("-")
    return value[:max_len].strip("-") or "moonn-image"


def image_ext(url: str) -> str:
    path = urlparse(url).path
    ext = Path(path).suffix.lower().lstrip(".")
    if ext in {"jpg", "jpeg", "png", "webp", "gif", "svg"}:
        return "jpg" if ext == "jpeg" else ext
    return "webp"


def clean_text(value: str, max_len: int = 180) -> str:
    value = re.sub(r"\s+", " ", value or "").strip()
    return value[:max_len].strip()


def proposed_alt(title: str, heading: str, kind: str) -> str:
    base = heading or title
    if kind == "background":
        return clean_text(f"Обложка страницы: {base}", 125)
    return clean_text(f"{base} — Татьяна Мунн, психолог МГУ", 125)


def proposed_filename(alias: str, title: str, heading: str, index: int, ext: str) -> str:
    topic = heading or title or alias or "moonn"
    slug = slugify(f"tatiana-munn-psiholog-mgu {alias} {topic}", 110)
    return f"{slug}-{index:02d}.{ext}"


def load_pages(scope_path: Path) -> list[dict]:
    pages = json.loads(scope_path.read_text(encoding="utf-8"))
    if not isinstance(pages, list):
        raise ValueError(f"Scope must be a list: {scope_path}")
    return pages


def audit_page(page, item: dict, timeout_ms: int) -> dict:
    url = item["production_url"]
    response = page.goto(url, wait_until="domcontentloaded", timeout=timeout_ms)
    page.wait_for_timeout(2200)
    data = page.evaluate(
        """() => {
            const skip = (src) =>
                !src ||
                /^data:image\\//i.test(src) ||
                /mc\\.yandex\\.ru\\/watch\\//i.test(src) ||
                /res\\.smartwidgets\\.ru\\/res\\/sw_logo_/i.test(src);
            const headingFor = (el) => {
                const record = el.closest('.r, .t-rec, section, article, div') || el.parentElement;
                const h = record ? record.querySelector('h1,h2,h3,.t-title,.t-heading,[field="title"]') : null;
                return (h?.innerText || '').trim();
            };
            const textFor = (el) => {
                const record = el.closest('.r, .t-rec, section, article, div') || el.parentElement;
                return (record?.innerText || '').trim().replace(/\\s+/g, ' ').slice(0, 240);
            };
            const imageRows = Array.from(document.querySelectorAll('img')).map((img, idx) => {
                const src = img.currentSrc || img.getAttribute('src') || img.getAttribute('data-original') || '';
                if (skip(src)) return null;
                const rect = img.getBoundingClientRect();
                return {
                    kind: 'img',
                    index: idx + 1,
                    src,
                    alt: img.getAttribute('alt') || '',
                    title: img.getAttribute('title') || '',
                    loading: img.getAttribute('loading') || '',
                    width: Math.round(rect.width),
                    height: Math.round(rect.height),
                    natural_width: img.naturalWidth || null,
                    natural_height: img.naturalHeight || null,
                    heading: headingFor(img),
                    context_text: textFor(img),
                    above_fold: rect.top < window.innerHeight,
                    css_selector_hint: img.className || img.id || ''
                };
            }).filter(Boolean);
            const bgRows = Array.from(document.querySelectorAll('[data-original], [style*="background-image"]')).map((el, idx) => {
                const raw = el.getAttribute('data-original') || getComputedStyle(el).backgroundImage || '';
                const match = raw.match(/url\\(["']?([^"')]+)["']?\\)/i);
                const src = raw.startsWith('http') ? raw : (match ? match[1] : '');
                if (skip(src)) return null;
                const rect = el.getBoundingClientRect();
                return {
                    kind: 'background',
                    index: idx + 1,
                    src,
                    alt: '',
                    title: '',
                    loading: '',
                    width: Math.round(rect.width),
                    height: Math.round(rect.height),
                    natural_width: null,
                    natural_height: null,
                    heading: headingFor(el),
                    context_text: textFor(el),
                    above_fold: rect.top < window.innerHeight,
                    css_selector_hint: el.className || el.id || ''
                };
            }).filter(Boolean);
            const ogImage = document.querySelector('meta[property="og:image"]')?.content || '';
            return {
                title: document.title || '',
                canonical: document.querySelector('link[rel="canonical"]')?.href || '',
                og_image: ogImage,
                images: imageRows.concat(bgRows)
            };
        }"""
    )
    rows = []
    seen = set()
    for idx, image in enumerate(data["images"], start=1):
        src = image["src"]
        if src in seen:
            continue
        seen.add(src)
        ext = image_ext(src)
        alt = proposed_alt(data["title"], image.get("heading", ""), image["kind"])
        filename = proposed_filename(item.get("alias", ""), data["title"], image.get("heading", ""), idx, ext)
        current_name = Path(urlparse(src).path).name
        has_seo_filename = bool(re.search(r"(tatiana|munn|moonn|psiholog|mgu|emotion|ei|eq|konsult|lekci|trening|kurs)", current_name, re.I))
        rows.append(
            {
                **image,
                "image_id": hashlib.sha1(src.encode("utf-8")).hexdigest()[:12],
                "current_filename": current_name,
                "proposed_filename": filename,
                "proposed_alt": alt,
                "proposed_title": alt,
                "needs_alt_source_fix": not clean_text(image.get("alt", "")) or image.get("alt", "").strip() in {"image", "photo"},
                "needs_title_fix": not clean_text(image.get("title", "")),
                "needs_filename_reupload": not has_seo_filename,
                "is_og_image": src == data.get("og_image"),
            }
        )
    return {
        "url": url,
        "alias": item.get("alias"),
        "source_page_id": item.get("source_page_id"),
        "network_status": response.status if response else None,
        "title": data["title"],
        "canonical": data["canonical"],
        "og_image": data["og_image"],
        "image_count": len(rows),
        "images": rows,
    }


def write_csv(path: Path, pages: list[dict]) -> None:
    fields = [
        "url", "alias", "source_page_id", "image_id", "kind", "src", "current_filename",
        "proposed_filename", "alt", "proposed_alt", "title", "proposed_title", "heading",
        "above_fold", "is_og_image", "needs_alt_source_fix", "needs_title_fix", "needs_filename_reupload",
    ]
    with path.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for page in pages:
            for image in page["images"]:
                writer.writerow({field: page.get(field, image.get(field, "")) for field in fields})


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit Moonn production images and produce SEO filename/alt manifest.")
    parser.add_argument("--scope", default=str(DEFAULT_SCOPE.relative_to(ROOT)))
    parser.add_argument("--json-out", default=str(DEFAULT_JSON_OUT.relative_to(ROOT)))
    parser.add_argument("--csv-out", default=str(DEFAULT_CSV_OUT.relative_to(ROOT)))
    parser.add_argument("--timeout-ms", type=int, default=45000)
    args = parser.parse_args()

    pages = load_pages(ROOT / args.scope)
    results = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/147.0 Safari/537.36",
            viewport={"width": 1440, "height": 1200},
        )
        for item in pages:
            browser_page = context.new_page()
            try:
                result = audit_page(browser_page, item, args.timeout_ms)
            except Exception as exc:
                result = {
                    "url": item.get("production_url"),
                    "alias": item.get("alias"),
                    "source_page_id": item.get("source_page_id"),
                    "error": str(exc),
                    "images": [],
                    "image_count": 0,
                }
            finally:
                browser_page.close()
            results.append(result)
        browser.close()

    all_images = [image for page in results for image in page.get("images", [])]
    summary = {
        "page_count": len(results),
        "error_count": sum(1 for item in results if item.get("error")),
        "image_count": len(all_images),
        "pages_without_images": sum(1 for item in results if not item.get("images")),
        "images_needing_source_alt": sum(1 for item in all_images if item["needs_alt_source_fix"]),
        "images_needing_title": sum(1 for item in all_images if item["needs_title_fix"]),
        "images_needing_filename_reupload": sum(1 for item in all_images if item["needs_filename_reupload"]),
        "og_image_count": sum(1 for item in all_images if item["is_og_image"]),
    }
    payload = {
        "schema_version": "1.0",
        "generated_at": "2026-05-03",
        "scope": str((ROOT / args.scope).relative_to(ROOT)),
        "summary": summary,
        "pages": results,
    }
    json_out = ROOT / args.json_out
    csv_out = ROOT / args.csv_out
    json_out.parent.mkdir(parents=True, exist_ok=True)
    json_out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_csv(csv_out, results)
    print(json.dumps(summary, ensure_ascii=False))
    return 0 if summary["error_count"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
