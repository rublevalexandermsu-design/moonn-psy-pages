import argparse
import json
from pathlib import Path


MENU_RECORD_TYPES = {"257", "454", "456", "978", "966", "967", "978", "1272", "1368"}
ZERO_BLOCK_TYPES = {"396"}
WEAK_H1_SIGNALS = {
    "как это работает",
    "практика",
    "частые вопросы",
    "вопросы для саморефлексии",
    "11.00 - 20.00",
    "11.00-20.00",
}
SKIP_URLS = {
    "https://moonn.ru/",
    "https://moonn.ru/st1",
    "https://moonn.ru/st2",
}


def first_text_signal(block: dict) -> str:
    headings = block.get("headings") or []
    if headings:
        return headings[0]["text"]
    candidates = block.get("textCandidates") or []
    return candidates[0] if candidates else ""


def significant_tokens(text: str) -> set[str]:
    stop = {
        "для",
        "что",
        "как",
        "это",
        "или",
        "при",
        "мгу",
        "психолог",
        "татьяна",
        "мунн",
        "эмоционального",
        "эмоциональный",
        "интеллекта",
        "психологии",
        "психология",
    }
    tokens = {
        token.strip("—:-,!?()[]«»").lower()
        for token in text.replace("/", " ").split()
        if len(token.strip("—:-,!?()[]«»")) >= 5
    }
    return {token for token in tokens if token not in stop}


def h1_candidate_confidence(signal: str, target: str, record_type: str) -> tuple[str, str]:
    normalized = signal.strip().lower()
    if record_type in ZERO_BLOCK_TYPES:
        return "manual", "zero_block_heading_semantics_needs_visual_edit"
    if normalized in WEAK_H1_SIGNALS or any(char.isdigit() for char in normalized[:8]):
        return "manual", "weak_or_date_time_signal"
    signal_tokens = significant_tokens(signal)
    target_tokens = significant_tokens(target)
    overlap = signal_tokens & target_tokens
    if overlap or normalized in target.lower() or target.lower() in normalized:
        return "high", "signal_matches_target"
    if len(signal) >= 16 and not signal.isupper():
        return "medium", "descriptive_signal_without_token_match"
    return "manual", "low_context_match"


def is_menu_like(block: dict) -> bool:
    return str(block.get("recordType", "")) in MENU_RECORD_TYPES


def choose_missing_h1_block(item: dict) -> dict | None:
    blocks = item.get("relevantBlocks") or []
    target = (item.get("targetH1") or "").lower()
    non_menu = [block for block in blocks if not is_menu_like(block)]
    for block in non_menu:
        signal = first_text_signal(block).lower()
        if signal and (signal in target or target in signal):
            return block
    return non_menu[0] if non_menu else (blocks[0] if blocks else None)


def build_plan(block_map: dict) -> dict:
    actions = []
    skipped = []
    for item in block_map["items"]:
        url = item["url"]
        issues = set(item.get("issues", []))
        if url in SKIP_URLS:
            skipped.append({"url": url, "pageId": item["pageId"], "reason": "manual_or_test_page"})
            continue

        if "missing_h1" in issues:
            block = choose_missing_h1_block(item)
            if not block:
                skipped.append({"url": url, "pageId": item["pageId"], "reason": "no_candidate_block"})
                continue
            visible_signal = first_text_signal(block)
            confidence, confidence_reason = h1_candidate_confidence(
                visible_signal, item.get("targetH1") or "", str(block.get("recordType", ""))
            )
            if confidence != "high":
                skipped.append(
                    {
                        "url": url,
                        "pageId": item["pageId"],
                        "recId": block["recId"],
                        "reason": confidence_reason,
                        "visibleSignal": visible_signal,
                        "targetH1": item.get("targetH1"),
                    }
                )
                continue
            actions.append(
                {
                    "url": url,
                    "pageId": item["pageId"],
                    "recId": block["recId"],
                    "setTag": "H1",
                    "reason": "missing_h1",
                    "visibleSignal": visible_signal,
                    "targetH1": item.get("targetH1"),
                    "confidence": confidence,
                }
            )
            continue

        if "multiple_h1" in issues:
            h1_blocks = [
                block
                for block in item.get("relevantBlocks", [])
                if any(heading.get("level") == "h1" for heading in block.get("headings", []))
            ]
            if not h1_blocks:
                skipped.append({"url": url, "pageId": item["pageId"], "reason": "no_h1_blocks_mapped"})
                continue
            for block in h1_blocks[1:]:
                actions.append(
                    {
                        "url": url,
                        "pageId": item["pageId"],
                        "recId": block["recId"],
                        "setTag": "H2",
                        "reason": "multiple_h1_extra",
                        "visibleSignal": first_text_signal(block),
                        "targetH1": item.get("targetH1"),
                    }
                )
    return {
        "version": 1,
        "createdAt": "2026-05-06",
        "source": "docs/moonn-h1-h2-block-map-2026-05-06.json",
        "scope": "supported_tilda_ui_apply_plan_for_heading_tag_fields",
        "policy": {
            "undocumentedTildaEndpoints": "not_used",
            "applicationMethod": "Real Google Chrome + Tilda block Settings -> SEO: tag for title",
            "skip": "homepage and test pages are not batch-edited",
        },
        "totalActions": len(actions),
        "totalPages": len({action["url"] for action in actions}),
        "actions": actions,
        "skipped": skipped,
    }


def write_md(plan: dict, path: Path) -> None:
    lines = [
        "# Moonn H1/H2 Tilda UI apply plan",
        "",
        f"- Actions: {plan['totalActions']}",
        f"- Pages: {plan['totalPages']}",
        f"- Skipped: {len(plan['skipped'])}",
        "",
        "## Actions",
        "",
    ]
    for action in plan["actions"]:
        lines.append(
            f"- `{action['setTag']}` page `{action['pageId']}` rec`{action['recId']}` "
            f"{action['url']} — {action['visibleSignal']}"
        )
    lines.append("")
    lines.append("## Skipped")
    lines.append("")
    for item in plan["skipped"]:
        lines.append(f"- {item['url']}: {item['reason']}")
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Build supported UI apply plan for Moonn H1/H2 cleanup.")
    parser.add_argument("--block-map", default="docs/moonn-h1-h2-block-map-2026-05-06.json")
    parser.add_argument("--out-json", default="docs/moonn-h1-h2-ui-apply-plan-2026-05-06.json")
    parser.add_argument("--out-md", default="docs/moonn-h1-h2-ui-apply-plan-2026-05-06.md")
    args = parser.parse_args()

    block_map = json.loads(Path(args.block_map).read_text(encoding="utf-8"))
    plan = build_plan(block_map)
    Path(args.out_json).write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_md(plan, Path(args.out_md))
    print(json.dumps({"actions": plan["totalActions"], "pages": plan["totalPages"], "skipped": len(plan["skipped"])}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
