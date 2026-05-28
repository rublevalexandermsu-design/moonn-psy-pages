# Moonn SEO/Growth Supervisor Check — 2026-05-28

## Scope

- Project: Moonn / `moonn.ru`
- Workstream: `codex/moonn-seo-audit`
- Period requested for analytics: `2026-04-29..2026-05-28`
- Mode: limited supervisor (no live Tilda changes, no cabinet settings changes)

## Verified facts

- Repo branch: `codex/moonn-seo-audit` (tracks `origin/codex/moonn-seo-audit`).
- Live HTTP verification from this host is **blocked by DNS**: `moonn.ru` does not resolve (`Errno 11001 getaddrinfo failed`).
- Daily five-page audit artifacts were produced, but all page checks are `http_ERROR` due to DNS (do not treat as SEO regression evidence):
  - `docs/moonn-five-page-seo-sprint-audit-2026-05-28.json`
  - `docs/moonn-five-page-seo-sprint-audit-2026-05-28.md`
- Attempted GUI fallback via `windows-mcp` failed in this environment:
  - `windows-mcp/Snapshot`: timeout
  - `windows-mcp/Screenshot`: `Transport closed`

## Analytics/growth gate (result)

- API: no new exports/tokens were available in-repo; API access remains unproven in this run.
- GUI: blocked by `windows-mcp` transport failure; no new GUI-verified aggregates were collected for `2026-04-29..2026-05-28`.
- Therefore: no traffic/SEO-growth conclusions are allowed for this run.

## Blockers

1. `P0` Host DNS/network: restore name resolution for `moonn.ru` (current DNS server shown as `172.19.0.2` returns NXDOMAIN).
2. `P0` GUI tooling: fix `windows-mcp` availability/transport so the bounded Rublev-profile Chrome check can be executed without changing cabinet settings.
3. `P1` MIIIIPS PR #11: canonical repo+PR URL is still missing from this repo (cannot verify merge/deploy state).

## Follow-up tasks (5–7)

1. Re-run `python scripts/moonn_five_page_seo_sprint_audit.py --packet docs/moonn-five-page-seo-packets-2026-05-21.json --rendered` after DNS is restored; expect HTTP 200 + sitemap/robots signals to become non-`None`.
2. In authenticated Chrome (Rublev profile), collect **aggregate-only** evidence for `2026-04-29..today`:
   - Yandex.Metrika `96397286`: visits/users/pageviews, sources, search phrases, landing pages, click goals.
   - GSC `https://moonn.ru/`: clicks/impressions/CTR/avg position + top queries + top pages.
   - Yandex Webmaster: sitemap last-read and indexing statuses.
3. Perform a bounded single-page investigation for the camp page AEO gap in Chrome (no edits): verify whether `#moonn-five-page-answer-block` is present, and whether the sprint layer JS loads/executes without errors.
4. Record the canonical MIIIIPS PR #11 URL (repo + PR link) into a doc/registry file to stop repeated “unknown PR” blockers.
5. Keep privacy/RKN weekly audit on Monday only (next scheduled check: 2026-06-01), unless explicitly requested earlier.

