import argparse
import json
import os
import re
import time
from html import unescape
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import urlopen


API_BASE_URL = "https://api.tildacdn.info/v1"
REC_RE = re.compile(r'(<div[^>]+id=["\']rec(?P<recid>\d+)["\'][\s\S]*?)(?=<div[^>]+id=["\']rec\d+["\']|</body>|$)', re.I)
HEADING_RE = re.compile(r"<h(?P<level>[1-6])\b(?P<attrs>[^>]*)>(?P<body>[\s\S]*?)</h[1-6]>", re.I)
TEXT_CLASS_RE = re.compile(
    r'<(?:div|span)[^>]+class=["\'][^"\']*(?:t-title|t-heading|tn-atom)[^"\']*["\'][^>]*>(?P<body>[\s\S]*?)</(?:div|span)>',
    re.I,
)


def load_env(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    if path.exists():
        for raw_line in path.read_text(encoding="utf-8-sig").splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            values[key.strip()] = value.strip()
    values.update({key: value for key, value in os.environ.items() if key.startswith("TILDA_")})
    return values


def require_config(values: dict[str, str]) -> dict[str, str]:
    missing = [key for key in ("TILDA_PUBLIC_KEY", "TILDA_SECRET_KEY") if not values.get(key)]
    if missing:
        raise RuntimeError("Missing Tilda env values: " + ", ".join(missing))
    return {
        "publickey": values["TILDA_PUBLIC_KEY"],
        "secretkey": values["TILDA_SECRET_KEY"],
        "projectid": values.get("TILDA_PROJECT_ID", ""),
    }


def call_tilda(method: str, params: dict[str, str], retries: int = 4) -> dict:
    url = f"{API_BASE_URL}/{method}/?{urlencode(params)}"
    for attempt in range(1, retries + 1):
        try:
            with urlopen(url, timeout=30) as response:
                data = json.loads(response.read().decode("utf-8"))
            break
        except HTTPError as error:
            if error.code not in {409, 429, 500, 502, 503, 504} or attempt == retries:
                body = error.read().decode("utf-8", errors="replace")[:500]
                raise RuntimeError(f"Tilda API {method} HTTP {error.code}: {body}") from error
            time.sleep(2 * attempt)
    if data.get("status") == "ERROR":
        raise RuntimeError(f"Tilda API {method} failed: {data.get('message') or data.get('error')}")
    return data["result"]


def text_from_html(value: str) -> str:
    value = re.sub(r"<script\b[^>]*>[\s\S]*?</script>", " ", value, flags=re.I)
    value = re.sub(r"<style\b[^>]*>[\s\S]*?</style>", " ", value, flags=re.I)
    value = re.sub(r"<[^>]+>", " ", value)
    return re.sub(r"\s+", " ", unescape(value)).strip()


def block_type(block_html: str) -> str:
    match = re.search(r'data-record-type=["\']([^"\']+)["\']', block_html, re.I)
    return match.group(1) if match else ""


def collect_headings(block_html: str) -> list[dict]:
    headings = []
    for match in HEADING_RE.finditer(block_html):
        text = text_from_html(match.group("body"))
        if not text:
            continue
        headings.append(
            {
                "level": f"h{match.group('level')}",
                "text": text,
                "attrs": re.sub(r"\s+", " ", match.group("attrs")).strip()[:240],
            }
        )
    return headings


def collect_candidates(block_html: str) -> list[str]:
    candidates = []
    seen = set()
    for match in TEXT_CLASS_RE.finditer(block_html):
        text = text_from_html(match.group("body"))
        if not text or len(text) < 8 or len(text) > 180:
            continue
        key = text.lower()
        if key in seen:
            continue
        seen.add(key)
        candidates.append(text)
        if len(candidates) >= 8:
            break
    return candidates


def parse_blocks(html: str) -> list[dict]:
    blocks = []
    for match in REC_RE.finditer(html):
        block_html = match.group(0)
        headings = collect_headings(block_html)
        candidates = collect_candidates(block_html)
        if not headings and not candidates:
            continue
        blocks.append(
            {
                "recId": match.group("recid"),
                "recordType": block_type(block_html),
                "headings": headings,
                "textCandidates": candidates,
            }
        )
    return blocks


def choose_relevant_blocks(blocks: list[dict], target_h1: str, current_h1: list[str]) -> list[dict]:
    needles = [target_h1.lower()] + [item.lower() for item in current_h1]
    relevant = []
    for block in blocks:
        haystack = " ".join(
            [heading["text"] for heading in block["headings"]] + block["textCandidates"]
        ).lower()
        if any(needle and (needle in haystack or haystack in needle) for needle in needles):
            relevant.append(block)
    if relevant:
        return relevant[:6]
    heading_blocks = [block for block in blocks if block["headings"]]
    return (heading_blocks or blocks)[:6]


def build_report(packet_path: Path, env_path: Path) -> dict:
    config = require_config(load_env(env_path))
    packet = json.loads(packet_path.read_text(encoding="utf-8"))
    local_page_ids = load_local_page_id_map()
    items = []
    skipped = []
    for index, item in enumerate(packet["items"], start=1):
        page_id = item.get("pageId") or local_page_ids.get(item["url"])
        if not page_id:
            skipped.append(
                {
                    "url": item["url"],
                    "reason": "missing_page_id_in_packet_and_local_snapshot",
                    "kind": item.get("kind"),
                    "issues": item.get("issues", []),
                }
            )
            continue
        page_id = str(page_id)
        print(f"[{index}/{len(packet['items'])}] read pageid={page_id} url={item['url']}")
        page_data = call_tilda(
            "getpagefull",
            {
                "publickey": config["publickey"],
                "secretkey": config["secretkey"],
                "pageid": page_id,
            },
        )
        time.sleep(0.4)
        html = page_data.get("html", "")
        blocks = parse_blocks(html)
        current_h1 = item.get("currentH1") or []
        relevant = choose_relevant_blocks(blocks, item.get("targetH1", ""), current_h1)
        items.append(
            {
                "url": item["url"],
                "pageId": page_id,
                "issues": item["issues"],
                "targetH1": item.get("targetH1"),
                "currentH1": current_h1,
                "blockCountWithHeadingSignals": len(blocks),
                "relevantBlocks": relevant,
                "uiAction": item.get("sourceLevelGate"),
            }
        )
    return {
        "version": 1,
        "createdAt": "2026-05-06",
        "sourcePacket": packet_path.as_posix(),
        "scope": "read_only_tilda_block_map_for_h1_h2_cleanup",
        "total": len(items),
        "skipped": skipped,
        "items": items,
    }


def load_local_page_id_map() -> dict[str, str]:
    candidates = [
        Path("output/tilda-production-current-snapshot/published-pages.json"),
        Path("output/tilda-snapshot/published-pages.json"),
    ]
    mapping: dict[str, str] = {}
    for path in candidates:
        if not path.exists():
            continue
        pages = json.loads(path.read_text(encoding="utf-8"))
        for page in pages:
            url = page.get("url")
            page_id = page.get("id")
            if url and page_id:
                mapping[url] = str(page_id)
    return mapping


def write_markdown(report: dict, path: Path) -> None:
    lines = [
        "# Moonn H1/H2 Tilda block map",
        "",
        "Read-only map generated from official Tilda API `getpagefull`. It does not write to Tilda.",
        "",
        f"- Total pages: {report['total']}",
        f"- Skipped pages: {len(report.get('skipped', []))}",
        "",
    ]
    if report.get("skipped"):
        lines.append("## Skipped")
        lines.append("")
        for item in report["skipped"]:
            lines.append(f"- {item['url']}: {item['reason']} ({item.get('kind')})")
        lines.append("")
    for item in report["items"]:
        lines.append(f"## {item['url']}")
        lines.append("")
        lines.append(f"- Page ID: `{item['pageId']}`")
        lines.append(f"- Issues: `{', '.join(item['issues'])}`")
        lines.append(f"- Target H1: {item['targetH1']}")
        if item["currentH1"]:
            lines.append(f"- Current H1: {', '.join(item['currentH1'])}")
        lines.append(f"- Candidate blocks: {len(item['relevantBlocks'])}")
        for block in item["relevantBlocks"][:4]:
            headings = "; ".join(f"{heading['level']} {heading['text']}" for heading in block["headings"])
            candidates = "; ".join(block["textCandidates"][:3])
            signal = headings or candidates or "no text signal"
            lines.append(f"  - rec{block['recId']} type `{block['recordType']}`: {signal}")
        lines.append("")
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Build read-only Tilda rec-block map for Moonn H1/H2 cleanup.")
    parser.add_argument("--env", default=".env")
    parser.add_argument("--packet", default="docs/moonn-h1-h2-source-cleanup-packet-2026-05-06.json")
    parser.add_argument("--out-json", default="docs/moonn-h1-h2-block-map-2026-05-06.json")
    parser.add_argument("--out-md", default="docs/moonn-h1-h2-block-map-2026-05-06.md")
    args = parser.parse_args()

    report = build_report(Path(args.packet), Path(args.env))
    out_json = Path(args.out_json)
    out_md = Path(args.out_md)
    out_json.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(report, out_md)
    print(json.dumps({"outJson": str(out_json), "outMd": str(out_md), "total": report["total"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
