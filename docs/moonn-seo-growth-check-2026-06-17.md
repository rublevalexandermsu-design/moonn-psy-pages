# Moonn SEO Growth Check — 2026-06-17

## Scope

- Project: Moonn / Tatyana Munn site.
- Workstream: `moonn-five-page-seo-aeo-supervisor`.
- Branch: `codex/moonn-seo-supervisor-20260617-clean`.
- Live domain under test: `https://мунн.рф/` (`https://xn--l1acaw.xn--p1ai/` for technical fetches).
- Reindex scope remains limited to `https://мунн.рф/`, `/events_tp`, `/lectures1`, `/psiholog-konsultacii-moskva` and approved five-page artifacts only; no 83-URL batch.

## Проверенные факты

### Live SEO on `мунн.рф`

- Ran successfully:
  - `python scripts\moonn_five_page_seo_sprint_audit.py --packet docs\moonn-five-page-seo-packets-2026-05-21.json --base-url https://xn--l1acaw.xn--p1ai --out-prefix moonn-five-page-seo-sprint-audit-2026-06-17`
- New dated artifacts:
  - `docs/moonn-five-page-seo-sprint-audit-2026-06-17.json`
  - `docs/moonn-five-page-seo-sprint-audit-2026-06-17.md`
- DNS for `xn--l1acaw.xn--p1ai` resolves on this host.
- All 5 scoped live URLs on `мунн.рф` returned HTTP `200`.
- `https://xn--l1acaw.xn--p1ai/sitemap.xml` includes all 5 scoped URLs in this run.
- `https://xn--l1acaw.xn--p1ai/robots.txt` does not block the 5 scoped URLs.
- Raw canonical remains aligned with `мунн.рф` / `xn--l1acaw.xn--p1ai` on all 5 scoped URLs.
- Source-level SEO debt is unchanged from `2026-06-16`:
  - gallery page raw HTML still contains placeholder strings `Your Name` and `Your Email`;
  - missing raw image `alt` persists across all 5 pages;
  - raw H1 remains non-canonical on camp (`0`), consultations (`2`) and reviews (`2`).

### Analytics / cabinets on the new domain

- Google Search Console in the real `Alexander` Chrome profile still opens `Oops, you don't have access to this property` for `sc-domain:xn--l1acaw.xn--p1ai`.
- Yandex.Webmaster now shows a confirmed site card and opens the summary page for `https://мунн.рф`:
  - site list contains `https://мунн.рф`;
  - summary page opens for `https://мунн.рф`;
  - visible summary signals: `Ошибок нет`, `3 рекомендации`, duplicate-title/description widget says no large duplicate cluster was found.
- Yandex.Metrika counter `96397286` is still a legacy lane:
  - cabinet label remains `Счетчик 1 Сайт moonn.ru`;
  - visible site labels are `moonn.ru` / `www.moonn.ru`;
  - no verified `мунн.рф` counter/export was visible in this bounded pass.

### Privacy / RKN read-only audit

- Ran successfully:
  - `python scripts\moonn_privacy_compliance_audit.py --base-url https://xn--l1acaw.xn--p1ai`
- New dated artifacts:
  - `docs/moonn-privacy-compliance-audit-2026-06-17.json`
  - `docs/moonn-privacy-compliance-audit-2026-06-17.md`
- `robots.txt` on the live domain returns `200`.
- Canonical privacy endpoints on the live domain still return `404`:
  - `/privacy`
  - `/personal-data-consent`
  - `/cookies`
  - `/data-subject-request`
- `83/83` scoped URLs show form signals.
- `78/83` scoped URLs were flagged with `forms_without_detected_checkbox`.
- No `gtag` / Google Analytics drift was detected by the audit script in this pass.

## Предположения / limits

- Yandex.Webmaster new-domain property is now real and readable, but it does not by itself prove traffic migration from `moonn.ru` to `мунн.рф`.
- Because GSC access is still blocked and Metrika remains legacy-only, there is still no trustworthy cross-source analytics packet for `2026-04-29..2026-06-17` on the new domain.
- The rendered five-page quality gate was not retried today because the last two `--rendered` runs on `2026-06-16` timed out; raw SEO and cabinet verification were prioritized for a bounded daily pass.

## Blockers

- `P0` Google Search Console blocker: new-domain property for `sc-domain:xn--l1acaw.xn--p1ai` is still inaccessible in the current Chrome profile.
- `P0` Yandex.Metrika blocker: counter `96397286` remains legacy-only (`moonn.ru` / `www.moonn.ru`), so traffic migration to `мунн.рф` is not proven.
- `P0` Privacy publication blocker: `/privacy`, `/personal-data-consent`, `/cookies`, `/data-subject-request` still return `404` on the live domain.
- `P0` Form compliance blocker: `78/83` scoped URLs still show forms without a detected required checkbox.
- `P1` Rendered audit durability blocker from `2026-06-16` remains open.
- `P1` Source cleanup debt remains: gallery placeholders, missing image `alt`, and raw H1 anomalies.

## Не делалось

- No Tilda edits.
- No legal/public text publication.
- No GSC submissions or ownership changes.
- No Yandex.Webmaster setting changes.
- No Yandex.Metrika edits.
- No URL Inspection batch actions.
- No screenshots were committed or published.

## Следующий action

1. Split the migration blocker: keep `GSC blocked` and `Metrika legacy-only` separate; do not report Yandex.Webmaster as missing anymore.
2. In the next bounded cabinet pass, try to locate an authorized GSC property for `https://мунн.рф/` or `sc-domain:xn--l1acaw.xn--p1ai` without falling back to `moonn.ru`.
3. Verify whether a dedicated `мунн.рф` Metrika counter exists anywhere in the account; if the cabinet still offers only `moonn.ru`, keep the analytics blocker and stop there.
4. Keep privacy remediation strictly as a publication packet until operator variables and legal approval are confirmed; do not publish legal pages from automation.
5. Stabilize the rendered supervisor lane before claiming the five-page SEO/AEO path is green end-to-end.

## Self-review

- Что было запрошено: ежедневный SEO/AEO, analytics и privacy supervisor для live-домена `мунн.рф` без перехода на `moon.ru` и без рабочего fallback на legacy `moonn.ru`.
- Что реально сделано: свежий raw SEO audit на `мунн.рф`, fresh privacy audit с live-domain override, bounded GUI verification для GSC, Yandex.Webmaster и Yandex.Metrika.
- Что фактически проверено: HTTP `200`, sitemap, robots, raw canonical, GSC access blocker, existence of the `https://мунн.рф` Yandex.Webmaster property, legacy-only state of Metrika counter `96397286`, live privacy endpoint `404` state, checkbox gap.
- Где риск преждевременного отчёта: нельзя говорить, что migration blocker полностью снят, потому что только Yandex.Webmaster green; GSC и Metrika по новому домену остаются неполными.
