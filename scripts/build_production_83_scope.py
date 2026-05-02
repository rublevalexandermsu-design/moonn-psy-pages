import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OLD_SCOPE = ROOT / "registry" / "tilda" / "moonn-production-73-rollout.json"
PAGES = ROOT / "output" / "tilda-production-current-snapshot" / "pages.json"
OUT = ROOT / "registry" / "tilda" / "moonn-production-83-rollout.json"


def production_url(page: dict) -> str:
    raw_alias = page.get("alias") or ""
    alias = raw_alias.strip("/")
    if alias:
        suffix = "/" if raw_alias.endswith("/") else ""
        return f"https://moonn.ru/{alias}{suffix}"
    filename = page.get("filename")
    if filename and filename != "page42678538.html":
        return f"https://moonn.ru/{filename}"
    return "https://moonn.ru/"


def main() -> int:
    old_scope = json.loads(OLD_SCOPE.read_text(encoding="utf-8"))
    pages = json.loads(PAGES.read_text(encoding="utf-8"))
    old_ids = {str(page["source_page_id"]) for page in old_scope}
    pages_by_id = {str(page["id"]): page for page in pages}
    sorted_pages = sorted(
        [page for page in pages if page.get("published")],
        key=lambda page: int(page.get("sort") or 999999),
    )

    scope = []
    for item in old_scope:
        page = pages_by_id.get(str(item["source_page_id"]), {})
        scope.append(
            {
                **item,
                "production_url": production_url(page) if page else item["production_url"],
                "title": page.get("title") or "",
                "published": page.get("published") or "",
                "sort": page.get("sort") or "",
                "scope_source": "production_73_existing",
            }
        )

    additions = []
    for page in sorted_pages:
        page_id = str(page["id"])
        alias = (page.get("alias") or "").strip("/")
        if page_id in old_ids or not alias:
            continue
        additions.append(
            {
                "alias": alias,
                "source_page_id": page_id,
                "staging_page_id": None,
                "production_url": production_url(page),
                "staging_url": None,
                "cluster": "unclassified",
                "rollout_status": "pending",
                "design_status": "pending",
                "live_status": None,
                "theme_marker_count": 0,
                "pinned_theme_count": 0,
                "title": page.get("title") or "",
                "published": page.get("published") or "",
                "sort": page.get("sort") or "",
                "scope_source": "production_alias_expansion_10",
            }
        )
        if len(additions) == 10:
            break

    result = scope + additions
    if len(result) != 83:
        raise RuntimeError(f"Expected 83 pages, got {len(result)}")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"out": str(OUT.relative_to(ROOT)), "count": len(result), "additions": additions}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
