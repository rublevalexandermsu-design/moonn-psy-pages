from __future__ import annotations

import json
import re
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
import argparse
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse, urlunparse


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "docs" / "moonn-gsc-yandex-reindex-packet-2026-05-08.json"
RUN_DATE = datetime.now(timezone.utc).date().isoformat()
OUT_JSON = ROOT / "docs" / f"moonn-privacy-compliance-audit-{RUN_DATE}.json"
OUT_MD = ROOT / "docs" / f"moonn-privacy-compliance-audit-{RUN_DATE}.md"
DEFAULT_BASE_URL = "https://moonn.ru"

POLICY_PATHS = ["/privacy", "/personal-data-consent", "/cookies", "/data-subject-request"]


@dataclass
class PageResult:
    url: str
    status: int | str
    formSignals: int
    consentSignals: int
    checkboxSignals: int
    yandexMetrikaSignals: int
    webvisorSignals: int
    googleAnalyticsSignals: int
    hasPolicyLink: bool
    hasConsentLink: bool
    hasCookieText: bool
    riskFlags: list[str]


def fetch(url: str, timeout: int) -> tuple[int | str, str]:
    req = Request(idna_url(url), headers={"User-Agent": "MoonnComplianceAudit/1.0"})
    try:
        with urlopen(req, timeout=timeout) as response:
            return response.getcode(), response.read().decode("utf-8", errors="replace")
    except HTTPError as exc:
        return exc.code, exc.read().decode("utf-8", errors="replace")
    except URLError as exc:
        return f"ERROR:{exc.reason}", ""


def count(pattern: str, html: str) -> int:
    return len(re.findall(pattern, html, flags=re.IGNORECASE | re.DOTALL))


def idna_url(url: str) -> str:
    parsed = urlparse(url)
    netloc = parsed.netloc.encode("idna").decode("ascii")
    return urlunparse((parsed.scheme, netloc, parsed.path, parsed.params, parsed.query, parsed.fragment))


def analyze_page(url: str, timeout: int) -> PageResult:
    status, html = fetch(url, timeout=timeout)
    form_signals = count(r"t-form|js-form-proccess|data-tilda-formskey|formaction|<form\b", html)
    consent_signals = count(r"персональн|согласи|конфиденц|privacy|personal-data|consent", html)
    checkbox_signals = count(r'type=["\']checkbox["\']|t-checkbox|checkbox', html)
    yandex_signals = count(r"mc\.yandex\.ru|ym\(", html)
    webvisor_signals = count(r"webvisor\s*:\s*true", html)
    ga_signals = count(r"google-analytics|googletagmanager|gtag\(", html)
    has_policy_link = bool(re.search(r'href=["\'][^"\']*(privacy|policy|personal-data)', html, re.I))
    has_consent_link = bool(re.search(r'href=["\'][^"\']*(consent|soglas|personal-data)', html, re.I))
    has_cookie_text = bool(re.search(r"cookie|cookies|куки|метрик", html, re.I))

    flags: list[str] = []
    if isinstance(status, int) and status >= 400:
        flags.append("http_error")
    if form_signals and not checkbox_signals:
        flags.append("forms_without_detected_checkbox")
    if form_signals and consent_signals == 0:
        flags.append("forms_without_detected_consent_text")
    if yandex_signals and not has_cookie_text:
        flags.append("metrics_without_detected_cookie_notice_text")
    if ga_signals:
        flags.append("google_analytics_signal_detected")

    return PageResult(
        url=url,
        status=status,
        formSignals=form_signals,
        consentSignals=consent_signals,
        checkboxSignals=checkbox_signals,
        yandexMetrikaSignals=yandex_signals,
        webvisorSignals=webvisor_signals,
        googleAnalyticsSignals=ga_signals,
        hasPolicyLink=has_policy_link,
        hasConsentLink=has_consent_link,
        hasCookieText=has_cookie_text,
        riskFlags=flags,
    )


def load_scope_urls() -> list[str]:
    data = json.loads(PACKET.read_text(encoding="utf-8"))
    urls = [row["url"] for row in data["urls"]]
    return list(dict.fromkeys(urls))


def normalize_base_url(value: str) -> str:
    return value.rstrip("/")


def rewrite_url_host(url: str, base_url: str) -> str:
    parsed = urlparse(url)
    base = urlparse(base_url)
    return urlunparse((base.scheme, base.netloc, parsed.path, parsed.params, parsed.query, parsed.fragment))


def write_report(payload: dict[str, Any]) -> None:
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    pages = payload["pages"]
    policy = payload["policyEndpoints"]
    high_risk = [p for p in pages if p["riskFlags"]]
    form_pages = [p for p in pages if p["formSignals"]]

    lines = [
        f"# Moonn Privacy Compliance Audit — {RUN_DATE}",
        "",
        "## Summary",
        "",
        f"- Scope URLs checked: `{len(pages)}`.",
        f"- Policy endpoints checked: `{len(policy)}`.",
        f"- Pages with form signals: `{len(form_pages)}`.",
        f"- Pages with risk flags: `{len(high_risk)}`.",
        "",
        "## Policy Endpoints",
        "",
    ]
    for row in policy:
        lines.append(f"- `{row['url']}` — `{row['status']}`")

    lines.extend([
        "",
        "## Required Publication Pages",
        "",
        "- `/privacy` — policy for personal-data processing.",
        "- `/personal-data-consent` — consent text linked from every form checkbox.",
        "- `/cookies` — cookies and Yandex Metrika/Webvisor notice.",
        "- `/data-subject-request` — request/withdrawal/update/deletion procedure, or equivalent section inside `/privacy`.",
        "",
        "## High-Risk Pages",
        "",
    ])
    for row in high_risk[:80]:
        flags = ", ".join(row["riskFlags"])
        lines.append(f"- `{row['url']}` — `{flags}`")

    if len(high_risk) > 80:
        lines.append(f"- ...and `{len(high_risk) - 80}` more. See JSON.")

    lines.extend([
        "",
        "## Gate",
        "",
        "- Do not treat this as legal advice.",
        "- Final publication requires confirmed operator details and legal approval.",
        "- Do not disable Yandex/Google crawling while fixing compliance.",
    ])
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def is_dns_like_failure(status: int | str) -> bool:
    if isinstance(status, int):
        return False
    if not status.startswith("ERROR:"):
        return False
    msg = status.lower()
    return any(
        needle in msg
        for needle in (
            "getaddrinfo failed",
            "name or service not known",
            "nodename nor servname provided",
            "temporary failure in name resolution",
            "dns",
            "11001",
            "11002",
            "11004",
        )
    )


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument("--timeout", type=int, default=25, help="HTTP timeout seconds per URL.")
    parser.add_argument(
        "--preflight-timeout",
        type=int,
        default=8,
        help="HTTP timeout seconds for preflight fetch used to fast-fail DNS outages.",
    )
    parser.add_argument(
        "--base-url",
        default=DEFAULT_BASE_URL,
        help="Live base URL to audit. Example: https://мунн.рф or https://xn--l1acaw.xn--p1ai.",
    )
    parser.add_argument(
        "--max-urls",
        type=int,
        default=0,
        help="Optional cap for scoped smoke checks. 0 means all URLs.",
    )
    return parser


def main() -> None:
    args = build_arg_parser().parse_args()
    base_url = normalize_base_url(args.base_url)
    urls = [rewrite_url_host(url, base_url) for url in load_scope_urls()]
    if args.max_urls and args.max_urls > 0:
        urls = urls[: args.max_urls]
    policy_urls = [f"{base_url}{path}" for path in POLICY_PATHS]

    preflight_url = f"{base_url}/robots.txt"
    preflight_status, _ = fetch(preflight_url, timeout=args.preflight_timeout)
    dns_blocked = is_dns_like_failure(preflight_status)
    if dns_blocked:
        policy_results = [asdict(PageResult(url=url, status=preflight_status, formSignals=0, consentSignals=0, checkboxSignals=0, yandexMetrikaSignals=0, webvisorSignals=0, googleAnalyticsSignals=0, hasPolicyLink=False, hasConsentLink=False, hasCookieText=False, riskFlags=["infra_dns_blocked"])) for url in policy_urls]
        page_results = [asdict(PageResult(url=url, status=preflight_status, formSignals=0, consentSignals=0, checkboxSignals=0, yandexMetrikaSignals=0, webvisorSignals=0, googleAnalyticsSignals=0, hasPolicyLink=False, hasConsentLink=False, hasCookieText=False, riskFlags=["infra_dns_blocked"])) for url in urls]
    else:
        policy_results = [asdict(analyze_page(url, timeout=args.timeout)) for url in policy_urls]
        page_results = [asdict(analyze_page(url, timeout=args.timeout)) for url in urls]

    payload = {
        "version": 1,
        "createdAt": datetime.now(timezone.utc).isoformat(),
        "scope": "Moonn 83 production URLs privacy/form/cookie compliance read-only audit",
        "sourcePacket": str(PACKET.relative_to(ROOT)),
        "infra": {
            "baseUrl": base_url,
            "preflight": {
                "url": preflight_url,
                "status": preflight_status,
                "timeoutSeconds": args.preflight_timeout,
            },
            "dnsLikeFailure": dns_blocked,
            "perUrlTimeoutSeconds": args.timeout,
            "maxUrls": args.max_urls,
        },
        "policyEndpoints": policy_results,
        "pages": page_results,
        "notes": [
            "This is a technical audit, not legal advice.",
            "Final public legal text requires confirmed operator details and legal approval.",
            "Google Analytics signals are flagged separately because cross-border/legal handling depends on actual configuration.",
        ],
    }
    write_report(payload)
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")


if __name__ == "__main__":
    main()
