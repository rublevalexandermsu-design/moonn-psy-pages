# Moonn SEO Growth Check — 2026-06-05

## Scope

- Project: Moonn / Tatyana Munn site.
- Workstream: `moonn-five-page-seo-aeo-supervisor`.
- Branch: `codex/moonn-seo-audit`.
- Live domain under test: `https://мунн.рф/` (`https://xn--l1acaw.xn--p1ai/` for technical fetches).
- Legacy analytics lane: `https://moonn.ru/` only when explicitly labeled historical/legacy.
- Reindex scope remains limited to the approved five URLs plus sitemap; no 83-URL batch.

## Проверенные факты

### Live HTML / rendered audit on `мунн.рф`

- Ran:
  - `python scripts\moonn_five_page_seo_sprint_audit.py --packet docs\moonn-five-page-seo-packets-2026-05-21.json --rendered --base-url https://xn--l1acaw.xn--p1ai --out-prefix moonn-five-page-seo-sprint-audit-2026-06-05`
- New dated artifacts:
  - `docs/moonn-five-page-seo-sprint-audit-2026-06-05.json`
  - `docs/moonn-five-page-seo-sprint-audit-2026-06-05.md`
- DNS for `xn--l1acaw.xn--p1ai` resolves on this host.
- All 5 scoped live URLs on `мунн.рф` returned HTTP `200`.
- `https://xn--l1acaw.xn--p1ai/sitemap.xml` includes all 5 scoped URLs in this run.
- `https://xn--l1acaw.xn--p1ai/robots.txt` does not block the 5 scoped URLs.
- Rendered H1 count is `1` on all 5 URLs.
- Rendered answer block count:
  - camp `/podrostkovyy-lager-psihologiya` -> `0`;
  - other 4 pages -> `1`.

### New live blockers surfaced on `мунн.рф`

- All 5 live pages still expose `canonical_mismatch`: canonical points to legacy `https://moonn.ru/...`, not `https://мунн.рф/...`.
- Camp page raw HTML still has placeholder strings `Your Name` and `Your Email`.
- Gallery page raw HTML still has placeholder strings `Your Name` and `Your Email`.
- Missing raw image `alt` persists across all 5 pages.
- Raw H1 remains non-canonical on camp (`0`), consultations (`2`) and reviews (`2`), even though rendered H1 is corrected.
- Camp page rendered AEO answer block regressed again to `0`, so the five-page live layer is not green two runs in a row.

### Local canon still intact

- `assets/moonn-five-page-seo-sprint-layer.js` exists in repo.
- git object `49a093e` resolves as `commit`.
- `docs/moonn-five-page-reindex-urls-2026-05-21.txt` is unchanged.

### GUI evidence collected today

- Google Search Console GUI check for the new property route surfaced a blocker, not success:
  - in the real `Alexander` Chrome profile, opening `sc-domain:xn--l1acaw.xn--p1ai` showed `Oops, you don't have access to this property`;
  - therefore `мунн.рф` GSC property is not verified for this operator in this run.
- No new Yandex.Webmaster `мунн.рф` host confirmation was captured today.
- No new Metrika-by-host evidence for `мунн.рф` was captured today.

## Предположения / limits

- The `Oops, you don't have access to this property` GSC page is GUI-visible evidence of missing access, but no cabinet settings were changed.
- The live audit used the punycode host for fetch stability; human-facing conclusions still refer to `мунн.рф`.
- Today’s success of `мунн.рф` sitemap inclusion does not prove Google/Yandex have migrated traffic; it only proves live HTTP/sitemap/robots visibility from this host.

## Blockers

- `P0` Domain migration blocker: canonical on all 5 live pages still points to `moonn.ru`.
- `P0` New-domain analytics blocker: GSC property for `мунн.рф` is not accessible for the current operator; migration traffic cannot be proven.
- `P0` New-domain webmaster blocker: Yandex.Webmaster host/property for `мунн.рф` remains unverified in this run.
- `P0` AEO blocker: camp page rendered answer block is still `0`.
- `P1` Source cleanup debt remains: raw placeholders + missing `alt` + raw H1 anomalies.

## Не делалось

- No Tilda content edits.
- No canonical rewrites in page settings.
- No privacy/legal edits.
- No GSC or Yandex.Webmaster submissions.
- No 83-URL batch actions.
- No cabinet settings changes.

## Следующий action

1. In Tilda Page settings SEO, replace native canonical on the 5 scoped pages from `https://moonn.ru/...` to `https://xn--l1acaw.xn--p1ai/...` or `https://мунн.рф/...` consistently at source.
2. In Tilda for the camp page only, inspect why the rendered answer block is absent on `мунн.рф` while the other 4 pages still render it.
3. In authenticated Chrome, verify or obtain access to the GSC property for `мунн.рф`, then submit only the 5 scoped URLs plus sitemap.
4. Verify whether Yandex.Webmaster host `https://мунн.рф/` exists and is confirmed before any bounded reindex submission.
5. Keep live `мунн.рф` checks and legacy `moonn.ru` analytics separated in future reports.
