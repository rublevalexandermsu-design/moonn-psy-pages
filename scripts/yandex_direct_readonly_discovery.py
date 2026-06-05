from __future__ import annotations

import json
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
SECRET_PATH = ROOT / "registry" / "local-secrets" / "yandex-direct-oauth.local.json"
OUT_PATH = ROOT / "output" / "yandex-direct-readonly-discovery-2026-06-05.json"
API_BASE = "https://api.direct.yandex.com/json/v5"


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


def extract_result(body: dict, key: str) -> list:
    if "error" in body:
        return []
    result = body.get("result") or {}
    value = result.get(key)
    return value if isinstance(value, list) else []


def main() -> None:
    token = load_token()
    calls: dict[str, dict] = {}

    calls["clients"] = call_direct(
        "clients",
        "get",
        {"FieldNames": ["Login"]},
        token,
    )

    calls["campaigns"] = call_direct(
        "campaigns",
        "get",
        {
            "SelectionCriteria": {},
            "FieldNames": [
                "Id",
                "Name",
                "Type",
                "State",
                "Status",
                "StatusPayment",
                "StatusClarification",
                "StartDate",
                "EndDate",
            ],
        },
        token,
    )

    campaigns = extract_result(calls["campaigns"], "Campaigns")
    campaign_ids = [item["Id"] for item in campaigns if "Id" in item]
    if campaign_ids:
        calls["adgroups"] = call_direct(
            "adgroups",
            "get",
            {
                "SelectionCriteria": {"CampaignIds": campaign_ids},
                "FieldNames": ["Id", "Name", "CampaignId", "Status", "ServingStatus"],
            },
            token,
        )
    else:
        calls["adgroups"] = {"http_status": 200, "result": {"AdGroups": []}, "note": "No campaigns"}

    adgroups = extract_result(calls["adgroups"], "AdGroups")
    adgroup_ids = [item["Id"] for item in adgroups if "Id" in item]
    if adgroup_ids:
        calls["ads"] = call_direct(
            "ads",
            "get",
            {
                "SelectionCriteria": {"AdGroupIds": adgroup_ids},
                "FieldNames": ["Id", "AdGroupId", "CampaignId", "Type", "State", "Status"],
                "TextAdFieldNames": ["Title", "Title2", "Text", "Href"],
            },
            token,
        )
        calls["keywords"] = call_direct(
            "keywords",
            "get",
            {
                "SelectionCriteria": {"AdGroupIds": adgroup_ids},
                "FieldNames": ["Id", "AdGroupId", "CampaignId", "Keyword", "State", "Status"],
            },
            token,
        )
    else:
        calls["ads"] = {"http_status": 200, "result": {"Ads": []}, "note": "No ad groups"}
        calls["keywords"] = {"http_status": 200, "result": {"Keywords": []}, "note": "No ad groups"}

    summary = {
        "client_logins": [item.get("Login") for item in extract_result(calls["clients"], "Clients")],
        "campaign_count": len(campaigns),
        "adgroup_count": len(adgroups),
        "ad_count": len(extract_result(calls["ads"], "Ads")),
        "keyword_count": len(extract_result(calls["keywords"], "Keywords")),
        "errors": {
            name: body.get("error")
            for name, body in calls.items()
            if isinstance(body, dict) and body.get("error")
        },
    }
    output = {"summary": summary, "calls": calls}
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    print(str(OUT_PATH))


if __name__ == "__main__":
    main()
