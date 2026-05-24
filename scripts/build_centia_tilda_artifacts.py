from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist" / "centia"
OUT_DIR = ROOT / "docs" / "centia-tilda"

REPO_CDN = "https://cdn.jsdelivr.net/gh/rublevalexandermsu-design/moonn-psy-pages"
DEFAULT_REF = "codex%2Fstudia"

PAGE_ALIASES = {
    "index.html": "/fnt",
    "prostranstvo.html": "/fnt-prostranstvo",
    "raspisanie.html": "/fnt-raspisanie",
    "oplata.html": "/fnt-bron",
    "contacts.html": "/fnt-kontakty",
    "deti-7-10.html": "/fnt-deti-7-10",
    "podrostki-11-13.html": "/fnt-podrostki-11-13",
    "podrostki-14-16.html": "/fnt-podrostki-14-16",
    "podrostki-15-17.html": "/fnt-podrostki-15-17",
    "roditelyam.html": "/fnt-roditelyam",
    "vzroslym.html": "/fnt-vzroslym",
    "o-tatyane.html": "/fnt-o-tatyane",
}


def extract(pattern: str, html: str) -> str:
    match = re.search(pattern, html, flags=re.I | re.S)
    return match.group(1).strip() if match else ""


def cdn_url(path: str, ref: str) -> str:
    normalized = path.replace("\\", "/").lstrip("/")
    if normalized.startswith("assets/images/"):
        repo_path = "centia/source/" + normalized
    elif normalized.startswith("assets/seo-images/"):
        repo_path = "centia/" + normalized.removeprefix("assets/")
    else:
        repo_path = "dist/centia/" + normalized
    return f"{REPO_CDN}@{ref}/{repo_path}"


def rewrite_asset_urls(html: str, ref: str) -> str:
    def replace_attr(match: re.Match[str]) -> str:
        attr = match.group(1)
        quote = match.group(2)
        value = match.group(3)
        if value.startswith(("http://", "https://", "data:", "mailto:", "tel:", "#")):
            return match.group(0)
        if value.startswith("assets/"):
            return f"{attr}={quote}{cdn_url(value, ref)}{quote}"
        return match.group(0)

    html = re.sub(r"\b(src|href)=(['\"])([^'\"]+)\2", replace_attr, html)

    def replace_css_url(match: re.Match[str]) -> str:
        value = match.group(1).strip("\"'")
        if value.startswith(("http://", "https://", "data:")):
            return match.group(0)
        if value.startswith("assets/"):
            return f"url('{cdn_url(value, ref)}')"
        return match.group(0)

    return re.sub(r"url\(([^)]+)\)", replace_css_url, html)


def rewrite_page_links(html: str) -> str:
    for filename, alias in PAGE_ALIASES.items():
        html = html.replace(f'href="{filename}"', f'href="{alias}"')
    return html


def tilda_block_from_full_page(full_html: str, ref: str) -> str:
    styles = "\n".join(re.findall(r"<style[^>]*>[\s\S]*?</style>", full_html, flags=re.I))
    scripts = "\n".join(re.findall(r"<script(?![^>]+application/ld\+json)[^>]*>[\s\S]*?</script>", full_html, flags=re.I))
    body = extract(r"<body[^>]*>([\s\S]*?)</body>", full_html)
    block = "\n".join(part for part in [styles, body, scripts] if part)
    block = rewrite_asset_urls(block, ref)
    block = rewrite_page_links(block)
    block = block.replace('href="/fnt#groups"', 'href="#groups"')
    return block.strip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ref", default=DEFAULT_REF, help="GitHub ref for jsDelivr URLs.")
    args = parser.parse_args()

    if not DIST.exists():
        raise SystemExit(f"Missing build directory: {DIST}")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    manifest = {
        "scope": "centia_tilda_publication_artifacts",
        "asset_ref": args.ref,
        "asset_cdn_base": f"{REPO_CDN}@{args.ref}",
        "pages": [],
    }

    for html_file in sorted(DIST.glob("*.html")):
        if html_file.name not in PAGE_ALIASES:
            continue
        full_html = html_file.read_text(encoding="utf-8")
        title = extract(r"<title>([\s\S]*?)</title>", full_html)
        description = extract(r'<meta\s+name=["\']description["\']\s+content=["\']([\s\S]*?)["\']', full_html)
        block = tilda_block_from_full_page(full_html, args.ref)
        block_name = f"{html_file.stem}-tilda-html-block.html"
        (OUT_DIR / block_name).write_text(block, encoding="utf-8")
        manifest["pages"].append(
            {
                "source": f"dist/centia/{html_file.name}",
                "block": f"docs/centia-tilda/{block_name}",
                "title": title,
                "description": description,
                "recommended_alias": PAGE_ALIASES[html_file.name].lstrip("/"),
            }
        )

    (OUT_DIR / "tilda-pages-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
