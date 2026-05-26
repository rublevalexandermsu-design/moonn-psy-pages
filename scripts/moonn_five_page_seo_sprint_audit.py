from __future__ import annotations

import argparse
import html
import json
import re
import time
import urllib.parse
import urllib.request
import urllib.error
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
TODAY = datetime.now(timezone.utc).date().isoformat()
DEFAULT_PACKET = DOCS / f"moonn-five-page-seo-packets-{TODAY}.json"
SITEMAP_URL = "https://moonn.ru/sitemap.xml"
ROBOTS_URL = "https://moonn.ru/robots.txt"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; MoonnFivePageSEOAudit/1.0; +https://moonn.ru/)",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}
PLACEHOLDERS = ["Book design", "Your Name", "Your Email", "Html code will be here"]


def fetch(url: str, timeout: int = 30) -> tuple[int | None, str, str | None]:
    request = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            raw = response.read()
            charset = response.headers.get_content_charset() or "utf-8"
            return int(response.status), raw.decode(charset, errors="replace"), None
    except urllib.error.HTTPError as exc:
        try:
            raw = exc.read()
            charset = exc.headers.get_content_charset() if exc.headers else None
            body = raw.decode(charset or "utf-8", errors="replace")
        except Exception:  # noqa: BLE001
            body = ""
        return int(exc.code), body, f"HTTPError: {exc}"
    except Exception as exc:  # noqa: BLE001
        return None, "", str(exc)


def visible_text(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value)
    value = html.unescape(value)
    return re.sub(r"\s+", " ", value).strip()


def attr_value(tag: str, attr: str) -> str:
    match = re.search(rf"\b{re.escape(attr)}\s*=\s*(['\"])(.*?)\1", tag, flags=re.I | re.S)
    return html.unescape(match.group(2).strip()) if match else ""


def first_meta(content: str, key_attr: str, key_value: str) -> str:
    for tag in re.findall(r"<meta\b[^>]*>", content, flags=re.I | re.S):
        if attr_value(tag, key_attr).lower() == key_value.lower():
            return attr_value(tag, "content")
    return ""


def first_link(content: str, rel_value: str) -> str:
    for tag in re.findall(r"<link\b[^>]*>", content, flags=re.I | re.S):
        if attr_value(tag, "rel").lower() == rel_value.lower():
            return attr_value(tag, "href")
    return ""


def sitemap_urls() -> tuple[set[str] | None, str | None]:
    status, body, error = fetch(SITEMAP_URL)
    if status != 200:
        return None, error or f"status_{status}"
    root = ET.fromstring(body)
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    return ({item.findtext("sm:loc", default="", namespaces=ns).strip() for item in root.findall("sm:url", ns)}, None)


def robots_disallows() -> tuple[list[str] | None, str | None]:
    status, body, error = fetch(ROBOTS_URL)
    if status != 200:
        return None, error or f"status_{status}"
    rows: list[str] = []
    for line in body.splitlines():
        if line.lower().startswith("disallow:"):
            value = line.split(":", 1)[1].strip()
            if value:
                rows.append(value)
    return rows, None


def robots_blocked(url: str, disallows: list[str] | None) -> bool | None:
    if disallows is None:
        return None
    path = urllib.parse.urlparse(url).path or "/"
    for rule in disallows:
        prefix = rule.rstrip("*")
        if prefix and path.startswith(prefix):
            return True
    return False


def raw_audit_page(page: dict, sitemap: set[str] | None, disallows: list[str] | None) -> dict:
    url = page["url"]
    status, body, error = fetch(url)
    item: dict = {
        "url": url,
        "pageId": page.get("sourcePageId", ""),
        "status": status,
        "inSitemap": (url in sitemap) if sitemap is not None else None,
        "robotsTxtBlocked": robots_blocked(url, disallows),
        "expectedTitle": page["seo"]["title"],
        "expectedDescription": page["seo"]["description"],
        "expectedH1": page["seo"]["h1"]["targetH1"],
    }
    if status != 200:
        item["fetchError"] = error or "fetch_failed"
        item["issues"] = [f"http_{status or 'ERROR'}"]
        return item
    title_match = re.search(r"<title[^>]*>(.*?)</title>", body, flags=re.I | re.S)
    title = visible_text(title_match.group(1)) if title_match else ""
    description = first_meta(body, "name", "description")
    canonical = first_link(body, "canonical")
    robots = first_meta(body, "name", "robots")
    h1_values = [visible_text(match) for match in re.findall(r"<h1\b[^>]*>(.*?)</h1>", body, flags=re.I | re.S)]
    img_tags = re.findall(r"<img\b[^>]*>", body, flags=re.I | re.S)
    missing_alt = sum(1 for tag in img_tags if not attr_value(tag, "alt").strip())
    placeholder_hits = [text for text in PLACEHOLDERS if text in body]
    jsonld_count = len(re.findall(r'application/ld\+json', body, flags=re.I))
    issues: list[str] = []
    if title != page["seo"]["title"]:
        issues.append("title_not_yet_updated")
    if description != page["seo"]["description"]:
        issues.append("description_not_yet_updated")
    if canonical.rstrip("/") != url.rstrip("/"):
        issues.append("canonical_mismatch")
    if "noindex" in robots.lower():
        issues.append("meta_noindex")
    if len(h1_values) != 1:
        issues.append("raw_h1_count_not_one")
    if placeholder_hits:
        issues.append("placeholder_text")
    if missing_alt:
        issues.append("images_missing_alt")
    if jsonld_count == 0:
        issues.append("missing_jsonld")
    if item["robotsTxtBlocked"] is None:
        issues.append("robots_txt_unknown")
    elif item["robotsTxtBlocked"]:
        issues.append("robots_txt_blocked")
    if item["inSitemap"] is None:
        issues.append("sitemap_unknown")
    elif not item["inSitemap"]:
        issues.append("not_in_sitemap")
    item.update(
        {
            "title": title,
            "description": description,
            "canonical": canonical,
            "robots": robots,
            "h1CountRaw": len(h1_values),
            "h1Raw": h1_values,
            "jsonLdCountRaw": jsonld_count,
            "imageCountRaw": len(img_tags),
            "imagesMissingAltRaw": missing_alt,
            "placeholderHitsRaw": placeholder_hits,
            "issues": issues,
            "readyForReindexAfterPublication": not any(
                issue in issues for issue in ["http_ERROR", "meta_noindex", "robots_txt_blocked", "not_in_sitemap"]
            ),
        }
    )
    return item


def rendered_audit(pages: list[dict], *, launch_timeout_ms: int = 60000, page_timeout_ms: int = 45000) -> list[dict]:
    try:
        from playwright.sync_api import sync_playwright
    except Exception as exc:  # noqa: BLE001
        return [{"url": page["url"], "renderedStatus": "skipped", "reason": f"playwright_unavailable: {exc}"} for page in pages]

    rows: list[dict] = []
    try:
        with sync_playwright() as p:
            start = time.monotonic()
            browser = p.chromium.launch(headless=True, timeout=launch_timeout_ms)
            context = browser.new_context(viewport={"width": 1366, "height": 900})
            context.set_default_timeout(page_timeout_ms)
            context.set_default_navigation_timeout(page_timeout_ms)
            for page in pages:
                audit = {"url": page["url"], "renderedStatus": "ok"}
                try:
                    browser_page = context.new_page()
                    try:
                        browser_page.goto(page["url"], wait_until="networkidle", timeout=page_timeout_ms)
                    except Exception:
                        browser_page.goto(page["url"], wait_until="domcontentloaded", timeout=page_timeout_ms)
                        browser_page.wait_for_timeout(5000)
                    h1_values = [text.strip() for text in browser_page.locator("h1").all_inner_texts() if text.strip()]
                    schema_count = browser_page.locator('script[type="application/ld+json"]').count()
                    answer_block_count = browser_page.locator("#moonn-five-page-answer-block").count()
                    body_text = browser_page.locator("body").inner_text(timeout=10000)
                    rendered_placeholders = [text for text in PLACEHOLDERS if text in body_text]
                    audit.update(
                        {
                            "titleRendered": browser_page.title(),
                            "h1CountRendered": len(h1_values),
                            "h1Rendered": h1_values,
                            "jsonLdCountRendered": schema_count,
                            "answerBlockCountRendered": answer_block_count,
                            "placeholderHitsRendered": rendered_placeholders,
                        }
                    )
                    browser_page.close()
                except Exception as exc:  # noqa: BLE001
                    audit.update({"renderedStatus": "error", "error": str(exc)})
                rows.append(audit)
                if time.monotonic() - start > max(30.0, (launch_timeout_ms / 1000) + (page_timeout_ms / 1000) * len(pages) + 30.0):
                    rows.append({"url": "", "renderedStatus": "aborted", "reason": "rendered_audit_watchdog_timeout"})
                    break
            context.close()
            browser.close()
    except Exception as exc:  # noqa: BLE001
        return [{"url": page["url"], "renderedStatus": "skipped", "reason": f"playwright_failed: {exc}"} for page in pages]
    return rows


def write_markdown(path: Path, payload: dict) -> None:
    lines = [
        f"# Moonn Five-Page SEO Sprint Audit — {payload['runDate']}",
        "",
        f"- Packet: `{payload['packet']}`",
        f"- Pages: `{len(payload['pages'])}`",
        "",
        "## Results",
        "",
    ]
    for page in payload["pages"]:
        issues = ", ".join(f"`{issue}`" for issue in page.get("issues", [])) or "`ok`"
        fetch_error = (page.get("fetchError") or "").strip()
        fetch_error_line = ""
        if fetch_error and page.get("status") != 200:
            fetch_error_line = f"- Fetch error: `{fetch_error[:160]}`"
        lines.extend(
            [
                f"### {page['url']}",
                "",
                f"- HTTP: `{page['status']}`",
                *( [fetch_error_line] if fetch_error_line else [] ),
                f"- Sitemap: `{page['inSitemap']}`",
                f"- Robots blocked: `{page['robotsTxtBlocked']}`",
                f"- Raw H1 count: `{page.get('h1CountRaw')}`",
                f"- Raw JSON-LD count: `{page.get('jsonLdCountRaw')}`",
                f"- Missing alt: `{page.get('imagesMissingAltRaw')}`",
                f"- Rendered status: `{page.get('rendered', {}).get('renderedStatus')}`",
                f"- Rendered H1 count: `{page.get('rendered', {}).get('h1CountRendered', '')}`",
                f"- Rendered answer block: `{page.get('rendered', {}).get('answerBlockCountRendered', '')}`",
                f"- Issues: {issues}",
                "",
            ]
        )
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def resolve_packet_path(packet_arg: str) -> Path:
    packet_path = (ROOT / packet_arg).resolve()
    if packet_path.exists():
        return packet_path

    candidates = sorted(DOCS.glob("moonn-five-page-seo-packets-*.json"), key=lambda p: p.name)
    if candidates:
        return candidates[-1].resolve()

    raise FileNotFoundError(f"Packet not found: {packet_arg}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit the five Moonn SEO sprint URLs.")
    parser.add_argument("--packet", default=str(DEFAULT_PACKET.relative_to(ROOT)))
    parser.add_argument("--rendered", action="store_true")
    parser.add_argument("--out-prefix", default=f"moonn-five-page-seo-sprint-audit-{TODAY}")
    args = parser.parse_args()

    packet_path = resolve_packet_path(args.packet)
    packet = json.loads(packet_path.read_text(encoding="utf-8"))
    sitemap, sitemap_error = sitemap_urls()
    disallows, robots_error = robots_disallows()
    pages = [raw_audit_page(page, sitemap, disallows) for page in packet["pages"]]
    rendered_rows = rendered_audit(packet["pages"]) if args.rendered else []
    rendered_by_url = {row["url"]: row for row in rendered_rows}
    for page in pages:
        page["rendered"] = rendered_by_url.get(page["url"], {"renderedStatus": "not_requested"})

    payload = {
        "version": 1,
        "runDate": TODAY,
        "createdAt": datetime.now(timezone.utc).isoformat(),
        "packet": str(packet_path.relative_to(ROOT)),
        "inputs": {
            "sitemapUrl": SITEMAP_URL,
            "robotsUrl": ROBOTS_URL,
            "sitemapFetchError": sitemap_error,
            "robotsFetchError": robots_error,
        },
        "pages": pages,
    }
    out_prefix = Path(args.out_prefix).name
    json_path = DOCS / f"{out_prefix}.json"
    md_path = DOCS / f"{out_prefix}.md"
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(md_path, payload)
    print(json.dumps({"json": str(json_path.relative_to(ROOT)), "md": str(md_path.relative_to(ROOT)), "pages": len(pages)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
