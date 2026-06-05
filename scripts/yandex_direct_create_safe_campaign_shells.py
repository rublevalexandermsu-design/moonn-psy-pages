from __future__ import annotations

import argparse
import json
from datetime import date, timedelta
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
SECRET_PATH = ROOT / "registry" / "local-secrets" / "yandex-direct-oauth.local.json"
PACKAGE_PATH = ROOT / "docs" / "yandex-direct-teen-intensive-package-2026-06-05.json"
OUT_PATH = ROOT / "output" / "yandex-direct-create-safe-campaign-shells-2026-06-05.json"
API_BASE = "https://api.direct.yandex.com/json/v5"
METRIKA_COUNTER_ID = 96397286
MICRO = 1_000_000


def load_token() -> str:
    data = json.loads(SECRET_PATH.read_text(encoding="utf-8"))
    token = data.get("access_token")
    if not token:
        raise RuntimeError(f"Missing access_token in {SECRET_PATH}")
    return token


def call_direct(endpoint: str, method: str, params: dict, token: str) -> dict:
    payload = json.dumps({"method": method, "params": params}, ensure_ascii=False).encode("utf-8")
    request = Request(
        f"{API_BASE}/{endpoint}",
        data=payload,
        method="POST",
        headers={
            "Authorization": f"Bearer {token}",
            "Accept-Language": "ru",
            "Content-Type": "application/json",
        },
    )
    try:
        with urlopen(request, timeout=30) as response:
            status = response.status
            text = response.read().decode("utf-8", errors="replace")
    except HTTPError as error:
        status = error.code
        text = error.read().decode("utf-8", errors="replace")
    try:
        body = json.loads(text)
    except json.JSONDecodeError:
        return {"http_status": status, "raw": text[:2000]}
    body["http_status"] = status
    return body


def get_campaigns(token: str) -> list[dict]:
    body = call_direct(
        "campaigns",
        "get",
        {
            "SelectionCriteria": {},
            "FieldNames": ["Id", "Name", "Type", "State", "Status", "StatusPayment"],
        },
        token,
    )
    if "error" in body:
        raise RuntimeError(json.dumps(body["error"], ensure_ascii=False))
    return body.get("result", {}).get("Campaigns", [])


def build_campaign_add_item(item: dict) -> dict:
    budget_rub = int(item["daily_budget_rub_recommended"])
    is_search = item["type"] == "search"
    average_cpc = 50 * MICRO
    weekly_limit = max(budget_rub * 7 * MICRO, 300 * 7 * MICRO)
    search_strategy = (
        {
            "BiddingStrategyType": "AVERAGE_CPC",
            "PlacementTypes": {
                "SearchResults": "YES",
                "ProductGallery": "NO",
                "DynamicPlaces": "NO",
            },
            "AverageCpc": {
                "AverageCpc": average_cpc,
                "WeeklySpendLimit": weekly_limit,
            },
        }
        if is_search
        else {"BiddingStrategyType": "SERVING_OFF"}
    )
    network_strategy = (
        {"BiddingStrategyType": "SERVING_OFF"}
        if is_search
        else {
            "BiddingStrategyType": "AVERAGE_CPC",
            "AverageCpc": {
                "AverageCpc": average_cpc,
                "WeeklySpendLimit": weekly_limit,
            },
        }
    )
    return {
        "Name": item["name"],
        "StartDate": (date.today() + timedelta(days=1)).isoformat(),
        "NegativeKeywords": {"Items": item.get("common_negative_keywords", [])},
        "TextCampaign": {
            "BiddingStrategy": {
                "Search": search_strategy,
                "Network": network_strategy,
            },
            "Settings": [
                {"Option": "ADD_METRICA_TAG", "Value": "YES"},
                {"Option": "ENABLE_SITE_MONITORING", "Value": "YES"},
            ],
            "CounterIds": {"Items": [METRIKA_COUNTER_ID]},
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--execute", action="store_true", help="Actually create missing campaign shells.")
    args = parser.parse_args()

    token = load_token()
    package = json.loads(PACKAGE_PATH.read_text(encoding="utf-8"))
    package_campaigns = package["campaigns"]
    common_negative_keywords = package["common_negative_keywords"]
    existing = get_campaigns(token)
    existing_by_name = {item["Name"]: item for item in existing}

    missing = []
    skipped = []
    for campaign in package_campaigns:
        if campaign["name"] in existing_by_name:
            skipped.append(existing_by_name[campaign["name"]])
            continue
        add_item = dict(campaign)
        add_item["common_negative_keywords"] = common_negative_keywords
        missing.append(build_campaign_add_item(add_item))

    result = {
        "mode": "execute" if args.execute else "dry_run",
        "existing_count": len(existing),
        "existing_names": sorted(existing_by_name.keys()),
        "missing_count": len(missing),
        "missing_names": [item["Name"] for item in missing],
        "created_ids": [],
        "add_response": None,
        "suspend_response": None,
        "post_state": None,
        "safety": {
            "ads_created": 0,
            "adgroups_created": 0,
            "keywords_created": 0,
            "strategy": "create_with_average_cpc_then_suspend_campaigns",
            "metrika_counter_id": METRIKA_COUNTER_ID,
        },
    }

    if args.execute and missing:
        add_body = call_direct("campaigns", "add", {"Campaigns": missing}, token)
        result["add_response"] = add_body
        if "error" in add_body:
            OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
            OUT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
            print(json.dumps(result, ensure_ascii=False, indent=2))
            raise SystemExit(1)

        add_results = add_body.get("result", {}).get("AddResults", [])
        per_item_errors = [item for item in add_results if item.get("Errors")]
        if per_item_errors:
            result["per_item_errors"] = per_item_errors
            result["post_state"] = get_campaigns(token)
            OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
            OUT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
            print(json.dumps(result, ensure_ascii=False, indent=2))
            print(str(OUT_PATH))
            raise SystemExit(1)
        created_ids = [item.get("Id") for item in add_results if item.get("Id")]
        result["created_ids"] = created_ids
        if created_ids:
            result["suspend_response"] = call_direct(
                "campaigns",
                "suspend",
                {"SelectionCriteria": {"Ids": created_ids}},
                token,
            )
        result["post_state"] = get_campaigns(token)
    elif args.execute:
        result["post_state"] = existing

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    print(str(OUT_PATH))


if __name__ == "__main__":
    main()
