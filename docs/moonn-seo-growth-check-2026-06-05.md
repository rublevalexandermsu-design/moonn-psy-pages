# Moonn SEO Growth Check — 2026-06-05

## Scope

- Project: Moonn / Tatyana Munn site.
- Workstream: `moonn-seo-privacy-supervisor`.
- Branch: `codex/moonn-seo-supervisor-20260605` tracking `origin/codex/moonn-seo-audit`.
- Requested live domain: `https://мунн.рф/` (`https://xn--l1acaw.xn--p1ai/`).
- Legacy analytics domain: `https://moonn.ru/`.
- Requested reindex scope remains limited to the approved five URLs plus sitemap only.

## Verified Facts (this run)

### New-domain live health

- Live HTTP checks against `https://xn--l1acaw.xn--p1ai/` succeeded with `200` for:
  - `/`
  - `/events_tp`
  - `/lectures1`
  - `/psiholog-konsultacii-moskva`
  - `/sitemap.xml`
  - `/robots.txt`
- `python scripts\moonn_five_page_seo_sprint_audit.py --packet docs\moonn-five-page-seo-packets-2026-05-21.json --rendered --base-url https://xn--l1acaw.xn--p1ai` wrote:
  - `docs/moonn-five-page-seo-sprint-audit-2026-06-05.json`
  - `docs/moonn-five-page-seo-sprint-audit-2026-06-05.md`
- New-domain rendered audit results for the five approved URLs:
  - all five return HTTP `200`;
  - all five are present in `https://xn--l1acaw.xn--p1ai/sitemap.xml`;
  - none of the five is blocked by `robots.txt`;
  - rendered H1 count is `1` on all five pages.

### New-domain SEO drift

- All five approved `мунн.рф` pages still publish canonical tags pointing to legacy `https://moonn.ru/...`, so every page is flagged `canonical_mismatch`.
- The camp page `https://xn--l1acaw.xn--p1ai/podrostkovyy-lager-psihologiya` still has a rendered AEO gap:
  - rendered answer block count is `0`;
  - rendered H1 changed to `Психология без скуки: подростковый интенсив речи, уверенности, общения и ИИ`, which no longer matches the SEO sprint target H1.
- Raw/source hygiene debt is still live on `мунн.рф`:
  - camp page: raw H1 count `0`, missing alt `3`, placeholder hits `Your Name`, `Your Email`;
  - gallery page: missing alt `4`, placeholder hits `Your Name`, `Your Email`;
  - exam page: missing alt `3`;
  - consultations page: raw H1 count `2`, missing alt `13`;
  - reviews page: raw H1 count `2`, missing alt `12`.

### Privacy / RKN smoke lane

- Friday run: weekly full privacy audit was not executed because today is `2026-06-05` (Thursday/Friday morning cycle, not Monday).
- Low-risk endpoint smoke check on the live domain confirms:
  - `https://xn--l1acaw.xn--p1ai/privacy` -> `404`
  - `https://xn--l1acaw.xn--p1ai/personal-data-consent` -> `404`
  - `https://xn--l1acaw.xn--p1ai/cookies` -> `404`
  - `https://xn--l1acaw.xn--p1ai/data-subject-request` -> `404`
- Privacy publication packet still contains a missing operator variable: `OPERATOR_ADDRESS` is unconfirmed.

### Analytics / GSC / Yandex

- No new committed exports for Yandex.Metrika `96397286`, Yandex.Webmaster, or Google Search Console were found in this repo for the requested custom period.
- Legacy analytics evidence remains the latest committed `2026-06-03` GUI-verified read for `https://moonn.ru/`; it must stay labeled legacy and must not be used as proof that `мунн.рф` traffic migration is complete.
- A bounded `windows-mcp` GUI fallback attempt was started successfully, but no fresh cabinet aggregates were collected in this run; therefore analytics/GSC/Yandex status is not upgraded beyond the already committed legacy evidence.
- New-domain property blocker remains open: no verified GSC or Yandex.Webmaster property for `https://мунн.рф/` was confirmed in this run, so `новая property не подтверждена, traffic migration не доказан`.

### MIIIIPS

- MIIIIPS PR #11 deploy/merge verification is still blocked because this repo still does not contain the canonical repo + PR URL.

## Assumptions / Limits

- The five-page audit is current live evidence for `мунн.рф`; the `moonn.ru` cabinet metrics remain historical/legacy evidence.
- GUI fallback was intentionally kept bounded and read-only. No cabinet settings, reindex submissions, or screenshots were saved/committed.
- Because no verified `мунн.рф` Search Console / Webmaster property was opened in this run, analytics migration conclusions remain blocked.

## Blockers

- `P0` Canonical drift: all five approved `мунн.рф` pages still canonicalize to `moonn.ru`.
- `P0` Traffic-migration proof is missing: `мунн.рф` GSC/Yandex properties were not verified in this run.
- `P0` Privacy publication gap persists on the live domain: `/privacy`, `/personal-data-consent`, `/cookies`, `/data-subject-request` are still `404`.
- `P0` Camp page AEO drift persists: rendered answer block `0` and rendered H1 no longer matches the SEO sprint target.
- `P1` Source hygiene debt persists: raw H1 anomalies, placeholder remnants, and missing image `alt` remain across the five-page scope.
- `P1` MIIIIPS PR #11 verification remains blocked by missing canonical PR URL.

## Not Done

- No Tilda content edits.
- No legal/privacy publication.
- No GSC or Yandex.Webmaster submissions.
- No 83-URL batch actions.
- No screenshots saved or committed.

## Next Actions

1. Verify `https://мунн.рф/` properties in Google Search Console and Yandex.Webmaster; until then keep all `moonn.ru` cabinet numbers labeled legacy.
2. Fix canonical drift for the five approved `мунн.рф` pages at the Tilda/source layer, then rerun the same `--base-url https://xn--l1acaw.xn--p1ai` audit.
3. Investigate the camp-page AEO regression on `мунн.рф`: rendered answer block `0` and changed H1 indicate live content drift from the 2026-05-21 sprint packet.
4. Keep reindex bounded to the approved five URLs plus sitemap only; do not widen to the 83-URL Google URL Inspection batch.
5. Monday privacy layer should rerun `python scripts\moonn_privacy_compliance_audit.py --base-url https://xn--l1acaw.xn--p1ai` and recheck the four policy endpoints after any legal/publication change.
6. Record the canonical MIIIIPS PR #11 URL in a stable doc/registry so deploy verification stops blocking every supervisor run.
