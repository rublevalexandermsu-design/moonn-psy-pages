# Moonn SEO Growth Check — 2026-06-06

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
  - `python scripts\moonn_five_page_seo_sprint_audit.py --packet docs\moonn-five-page-seo-packets-2026-05-21.json --rendered --base-url https://xn--l1acaw.xn--p1ai --out-prefix moonn-five-page-seo-sprint-audit-2026-06-06`
- New dated artifacts:
  - `docs/moonn-five-page-seo-sprint-audit-2026-06-06.json`
  - `docs/moonn-five-page-seo-sprint-audit-2026-06-06.md`
- DNS for `xn--l1acaw.xn--p1ai` resolves on this host.
- All 5 scoped live URLs on `мунн.рф` returned HTTP `200`.
- `https://xn--l1acaw.xn--p1ai/sitemap.xml` includes all 5 scoped URLs in this run.
- `https://xn--l1acaw.xn--p1ai/robots.txt` does not block the 5 scoped URLs.
- Canonical status:
  - camp `/podrostkovyy-lager-psihologiya` now returns canonical `https://xn--l1acaw.xn--p1ai/podrostkovyy-lager-psihologiya`;
  - the other 4 pages still expose `canonical_mismatch` to legacy `https://moonn.ru/...`.
- Rendered H1 count is `1` on all 5 URLs.
- Rendered answer block count:
  - camp `/podrostkovyy-lager-psihologiya` -> `0`;
  - other 4 pages -> `1`.
- Raw source debt still visible:
  - camp raw title/description are not yet aligned with the 2026-05-21 packet;
  - gallery raw HTML still contains placeholder strings `Your Name` and `Your Email`;
  - missing raw image `alt` persists across all 5 pages;
  - raw H1 remains non-canonical on camp (`0`), consultations (`2`) and reviews (`2`).

### GUI evidence collected today

- In the real `Alexander` Chrome profile, Google Search Console for `sc-domain:xn--l1acaw.xn--p1ai` still opens `Oops, you don't have access to this property`.
- In the real `Alexander` Chrome profile, Yandex.Webmaster for `https://xn--l1acaw.xn--p1ai:443` shows the orange banner: `Сайт https://xn--l1acaw.xn--p1ai вам не принадлежит. Добавьте его в список ваших сайтов и подтвердите права на него, чтобы просматривать информацию.`
- Combined new-domain blocker for this run: `новая property не подтверждена, traffic migration не доказан`.

## Предположения / limits

- Today’s GSC and Yandex.Webmaster facts are GUI-only access/blocker checks; no cabinet settings were changed.
- The live audit used the punycode host for fetch stability; human-facing conclusions still refer to `мунн.рф`.
- Because the new-domain properties are not confirmed, legacy `moonn.ru` GSC/Metrika numbers still cannot be used as proof of `мунн.рф` migration.

## Blockers

- `P0` New-domain property blocker: `новая property не подтверждена, traffic migration не доказан`.
- `P0` Canonical migration is incomplete on 4 of the 5 scoped live pages: gallery, exam prep, consultations and reviews still point canonical to legacy `https://moonn.ru/...`.
- `P0` Camp page AEO regression persists on the live domain: rendered answer block is still `0`.
- `P0` Camp source metadata drift remains: raw title/description do not match the five-page packet even though the URL is reachable and canonical is now new-domain.
- `P1` Source cleanup debt remains: gallery placeholders, missing image `alt`, and raw H1 anomalies.

## Не делалось

- No Tilda edits.
- No canonical rewrites in page settings.
- No privacy/legal edits.
- No GSC or Yandex.Webmaster submissions.
- No Yandex.Metrika edits.
- No 83-URL batch actions.
- No cabinet settings changes.

## Следующий action

1. In Tilda Page settings SEO, replace native canonical on the remaining 4 scoped pages from `https://moonn.ru/...` to `https://xn--l1acaw.xn--p1ai/...` or `https://мунн.рф/...` consistently at source.
2. In Tilda for the camp page only, inspect why the rendered answer block is absent on `мунн.рф` and why the raw title/description still differ from the sprint packet.
3. In authenticated Chrome, verify/add access to the GSC property for `мунн.рф` and confirm the Yandex.Webmaster host before any scoped reindex submission.
4. After property confirmation, submit only the 5 scoped URLs plus sitemap; do not submit the 83-URL batch.

## Self-review

- Что проверено: live HTTP/sitemap/robots/rendered state for all 5 scoped `мунн.рф` URLs; GSC GUI access state for `sc-domain:xn--l1acaw.xn--p1ai`; Yandex.Webmaster GUI ownership state for `https://xn--l1acaw.xn--p1ai:443`.
- Какие артефакты изменены: `docs/moonn-five-page-seo-sprint-audit-2026-06-06.{json,md}`, `docs/moonn-seo-growth-check-2026-06-06.md`, `docs/moonn-five-page-seo-change-ledger-2026-05-21.json`, `docs/moonn-seo-growth-backlog.md`, `docs/codex-chat-history.md`.
- Где риск преждевременного отчёта: нельзя трактовать доступность live-страниц как завершённую доменную миграцию, пока новая property не подтверждена и canonical не выровнен на всех 5 URL.
