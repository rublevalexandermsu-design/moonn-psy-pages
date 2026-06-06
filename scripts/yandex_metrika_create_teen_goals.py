from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_COUNTER_ID = "96397286"
DEFAULT_SECRET_PATH = ROOT / "registry" / "local-secrets" / "yandex-metrika-oauth.local.json"

GOAL_IDS = [
    "lead_click",
    "lead_submit",
    "click_telegram",
    "click_whatsapp",
    "click_phone",
    "payment_start",
    "payment_submit",
    "payment_success",
    "program_view",
    "pdf_download",
]

GOAL_LABELS = {
    "lead_click": "Teen intensive: CTA click",
    "lead_submit": "Teen intensive: lead submitted",
    "click_telegram": "Teen intensive: Telegram click",
    "click_whatsapp": "Teen intensive: WhatsApp click",
    "click_phone": "Teen intensive: phone click",
    "payment_start": "Teen intensive: payment opened",
    "payment_submit": "Teen intensive: checkout submitted",
    "payment_success": "Teen intensive: payment success",
    "program_view": "Teen intensive: program view",
    "pdf_download": "Teen intensive: PDF download",
}


def read_token(secret_path: Path) -> str:
    env_token = os.environ.get("YANDEX_METRIKA_TOKEN")
    if env_token:
        return env_token.strip()
    if not secret_path.exists():
        raise RuntimeError(
            f"Metrika OAuth token not found. Put access_token into {secret_path} "
            "or set YANDEX_METRIKA_TOKEN."
        )
    data = json.loads(secret_path.read_text(encoding="utf-8"))
    token = data.get("access_token") or data.get("oauth_token")
    if not token:
        raise RuntimeError(f"No access_token field in {secret_path}")
    return str(token).strip()


def call_api(method: str, url: str, token: str, payload: dict | None = None) -> tuple[int, dict]:
    body = None if payload is None else json.dumps(payload, ensure_ascii=False).encode("utf-8")
    request = Request(url, data=body, method=method)
    request.add_header("Authorization", f"OAuth {token}")
    request.add_header("Accept", "application/json")
    if body is not None:
        request.add_header("Content-Type", "application/json")
    try:
        with urlopen(request, timeout=30) as response:
            raw = response.read().decode("utf-8")
            return response.status, json.loads(raw) if raw else {}
    except HTTPError as error:
        raw = error.read().decode("utf-8", errors="replace")
        try:
            parsed = json.loads(raw) if raw else {}
        except json.JSONDecodeError:
            parsed = {"raw": raw}
        return error.code, parsed
    except URLError as error:
        raise RuntimeError(f"API network error: {error}") from error


def build_goal(goal_id: str) -> dict:
    return {
        "goal": {
            "name": GOAL_LABELS[goal_id],
            "type": "action",
            "conditions": [{"type": "exact", "url": goal_id}],
        }
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Create explicit Yandex Metrika JS goals for the Moonn teen intensive.")
    parser.add_argument("--counter-id", default=DEFAULT_COUNTER_ID)
    parser.add_argument("--secret", default=str(DEFAULT_SECRET_PATH))
    parser.add_argument("--apply", action="store_true", help="Actually create missing goals. Without this flag, only reports the plan.")
    parser.add_argument("--out", default="output/yandex-metrika-teen-goals-create-report-2026-06-06.json")
    args = parser.parse_args()

    token = read_token(Path(args.secret))
    base = f"https://api-metrika.yandex.net/management/v1/counter/{args.counter_id}/goals"
    status, data = call_api("GET", base, token)
    report = {
        "counterId": args.counter_id,
        "apply": args.apply,
        "listStatus": status,
        "existing": [],
        "missing": [],
        "created": [],
        "errors": [],
    }
    if status != 200:
        report["errors"].append({"operation": "list_goals", "status": status, "response": data})
        out_path = ROOT / args.out
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 2

    goals = data.get("goals", [])
    existing_conditions = set()
    existing_names = set()
    for goal in goals:
        existing_names.add(str(goal.get("name", "")))
        for condition in goal.get("conditions") or []:
            if isinstance(condition, dict) and condition.get("url"):
                existing_conditions.add(str(condition["url"]))

    for goal_id in GOAL_IDS:
        if goal_id in existing_conditions or GOAL_LABELS[goal_id] in existing_names:
            report["existing"].append(goal_id)
            continue
        report["missing"].append(goal_id)
        if args.apply:
            create_status, create_data = call_api("POST", base, token, build_goal(goal_id))
            item = {"goalId": goal_id, "status": create_status, "response": create_data}
            if create_status == 200:
                report["created"].append(item)
            else:
                report["errors"].append(item)

    out_path = ROOT / args.out
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if not report["errors"] else 3


if __name__ == "__main__":
    raise SystemExit(main())
