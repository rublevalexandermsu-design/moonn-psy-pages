# Moonn SEO Growth Check — 2026-05-29

## Scope

- Project: Moonn / moonn.ru
- Workstream: daily `moonn-seo-privacy-supervisor` (SEO/AEO + analytics evidence; без live-изменений)
- Branch: `codex/moonn-seo-audit`
- Date (MSK): `2026-05-29`

## Verified Technical Facts (this host)

- Infra blocker: DNS resolution for `moonn.ru` is broken on this host (`[Errno 11001] getaddrinfo failed`).
  - Consequence: all live HTTP / sitemap / robots / rendered checks are invalid here today and must not be interpreted as a site regression.
- Daily five-page audit recorded (DNS-blocked, fast-fail):
  - `docs/moonn-five-page-seo-sprint-audit-2026-05-29.json`
  - `docs/moonn-five-page-seo-sprint-audit-2026-05-29.md`

## SEO Checklist Status

1) MIIIIPS PR #11 deploy/merge + live HTTP 200 verification: `BLOCKED` (canonical PR link still missing in this repo context).
2) Reindex follow-up (GSC + Yandex) for priority URLs: `BLOCKED` (requires authenticated GUI or API/exports; DNS blocker prevents even low-risk fetch here).
3) 83 pages audit/classification follow-up: `PAUSED` (no new evidence today; focus stays on infra + analytics access).
4) Yandex Services reviews / MSU Istina sync: `BLOCKED` (access/approval).
5) Paid video lectures: `PAUSED` (await verified video registry).

## Analytics / Growth Gate

- Period required: `2026-04-29 .. 2026-05-29`
- Status today:
  - API exports: `not found` in repo (no new export artifacts committed for Metrika/GSC/Webmaster).
  - GUI verification: `not performed` (needs Rublev Chrome profile; additionally this host has DNS blocker).
- Conclusion: do not claim SEO success by traffic today; keep as blocker.

## Blockers

1. `P0` Infra: DNS for `moonn.ru` broken on this host (`Errno 11001`).
2. `P0` Analytics evidence: no API/exports + no GUI-verified aggregates for `2026-04-29..today` captured in the last two runs (2026-05-28 and 2026-05-29).
3. `P0` MIIIIPS PR #11: canonical repo/PR URL still missing.

## Next Actions (bounded)

1. Fix/restore DNS/network on the supervisor host (or run the same supervisor from another known-good host) and re-run the five-page audit (raw + rendered).
2. Once DNS is healthy: GUI-only collection (Rublev Chrome profile) of aggregates for `2026-04-29..today`:
   - Metrika `96397286`: visits/users/pageviews + sources + top landing pages + top queries (aggregates only)
   - GSC property `https://moonn.ru/`: clicks/impressions/CTR/avg position + pages + queries (aggregates only)
   - Yandex Webmaster: sitemap last read / indexing statuses for priority URLs + queue statuses (aggregates only)
3. Record the canonical MIIIIPS PR #11 link in a stable doc/registry to stop repeated “unknown PR” blockers.

