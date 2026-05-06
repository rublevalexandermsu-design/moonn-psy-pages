import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLAN_PATH = ROOT / "docs" / "moonn-h1-h2-ui-apply-plan-2026-05-06.json"
BLOCK_MAP_PATH = ROOT / "docs" / "moonn-h1-h2-block-map-2026-05-06.json"
OUT_JSON = ROOT / "docs" / "moonn-h1-h2-capability-buckets-2026-05-06.json"
OUT_MD = ROOT / "docs" / "moonn-h1-h2-capability-buckets-2026-05-06.md"


def main() -> int:
    plan = json.loads(PLAN_PATH.read_text(encoding="utf-8"))
    block_map = json.loads(BLOCK_MAP_PATH.read_text(encoding="utf-8"))
    record_types = {}
    for item in block_map["items"]:
        for block in item["relevantBlocks"]:
            record_types[(item["url"], block["recId"])] = block.get("recordType", "")

    proven_supported = {"485"}
    proven_unsupported = {"18", "578"}
    buckets = {
        "supported_block_setting": [],
        "unsupported_needs_design_solution": [],
        "manual_verify": [],
    }
    for action in plan["actions"]:
        record_type = record_types.get((action["url"], action["recId"]), "")
        item = {**action, "recordType": record_type}
        if record_type in proven_supported:
            buckets["supported_block_setting"].append(item)
        elif record_type in proven_unsupported:
            buckets["unsupported_needs_design_solution"].append(item)
        else:
            buckets["manual_verify"].append(item)

    report = {
        "version": 1,
        "createdAt": "2026-05-06",
        "basis": "post-pilot Tilda UI capability check",
        "counts": {key: len(value) for key, value in buckets.items()},
        "provenSupportedRecordTypes": sorted(proven_supported),
        "provenUnsupportedRecordTypes": sorted(proven_unsupported),
        "buckets": buckets,
    }
    OUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Moonn H1/H2 Capability Buckets",
        "",
        f"- Supported block-setting actions: {len(buckets['supported_block_setting'])}",
        f"- Unsupported, needs design solution: {len(buckets['unsupported_needs_design_solution'])}",
        f"- Manual verify before applying: {len(buckets['manual_verify'])}",
        "",
        "## Supported Block Setting",
        "",
    ]
    for item in buckets["supported_block_setting"]:
        lines.append(
            f"- `{item['setTag']}` type `{item['recordType']}` {item['url']} "
            f"rec`{item['recId']}` — {item['visibleSignal']}"
        )
    lines += ["", "## Unsupported: Needs Design Solution", ""]
    for item in buckets["unsupported_needs_design_solution"]:
        lines.append(
            f"- `{item['setTag']}` type `{item['recordType']}` {item['url']} "
            f"rec`{item['recId']}` — {item['visibleSignal']}"
        )
    lines += ["", "## Manual Verify", ""]
    for item in buckets["manual_verify"]:
        lines.append(
            f"- `{item['setTag']}` type `{item['recordType']}` {item['url']} "
            f"rec`{item['recId']}` — {item['visibleSignal']}"
        )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps(report["counts"], ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
