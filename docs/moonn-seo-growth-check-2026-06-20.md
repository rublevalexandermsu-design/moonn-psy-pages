# Moonn SEO Growth Check — 2026-06-20

## Scope

- Project: Moonn / Tatyana Munn site.
- Workstream: `moonn-five-page-seo-aeo-supervisor`.
- Branch: `codex/moonn-seo-audit`.
- Live domain under test: `https://мунн.рф/` (`https://xn--l1acaw.xn--p1ai/` for technical fetches).
- Legacy analytics lane: `https://moonn.ru/` remains historical only and was not used as a working property in this run.
- Reindex scope stayed limited to the approved five URLs plus sitemap; no 83-URL batch.

## Проверенные факты

### Raw live audit on `мунн.рф`

- Ran successfully:
  - `python scripts\moonn_five_page_seo_sprint_audit.py --packet docs\moonn-five-page-seo-packets-2026-05-21.json --base-url https://xn--l1acaw.xn--p1ai --out-prefix moonn-five-page-seo-sprint-audit-2026-06-20`
- New dated artifacts:
  - `docs/moonn-five-page-seo-sprint-audit-2026-06-20.json`
  - `docs/moonn-five-page-seo-sprint-audit-2026-06-20.md`
- DNS for `xn--l1acaw.xn--p1ai` resolves on this host.
- All 5 scoped live URLs on `мунн.рф` returned HTTP `200`.
- `https://xn--l1acaw.xn--p1ai/sitemap.xml` includes all 5 scoped URLs.
- `https://xn--l1acaw.xn--p1ai/robots.txt` does not block the 5 scoped URLs.
- Raw canonical still matches `мунн.рф` / `xn--l1acaw.xn--p1ai` on all 5 scoped URLs.
- Source-level debt remains:
  - camp raw H1 count is `0`;
  - consultations and reviews raw H1 count is `2`;
  - gallery still exposes `Your Name` and `Your Email`;
  - missing raw image `alt` persists on all 5 pages.

### Rendered audit on `мунн.рф`

- First rendered attempt timed out externally after about `604s` and produced no dated rendered artifact, so it was not treated as proof.
- Minimal audit-tool hardening was applied in `scripts/moonn_five_page_seo_sprint_audit.py`: Playwright pages are now closed in `finally`, and context/browser close is best-effort. This prevents one failed navigation from leaving stale pages open and blocking the whole supervisor run.
- Re-run completed successfully in about `388s`:
  - `python scripts\moonn_five_page_seo_sprint_audit.py --packet docs\moonn-five-page-seo-packets-2026-05-21.json --rendered --base-url https://xn--l1acaw.xn--p1ai --out-prefix moonn-five-page-seo-sprint-audit-2026-06-20-rendered`
- New dated rendered artifacts:
  - `docs/moonn-five-page-seo-sprint-audit-2026-06-20-rendered.json`
  - `docs/moonn-five-page-seo-sprint-audit-2026-06-20-rendered.md`
- Rendered result is still mixed, not green:
  - camp `/podrostkovyy-lager-psihologiya` completed with `renderedStatus=ok`, `h1CountRendered=1`, `answerBlockCountRendered=1`, `placeholderHitsRendered=[]`;
  - gallery `/kartiny-tatiany-munn` timed out at `Page.goto` `45000ms`;
  - exam prep `/psypodgotovka1` timed out at `Page.goto` `45000ms`;
  - consultations `/psiholog-konsultacii-moskva` timed out at `Page.goto` `45000ms`;
  - reviews `/otzivi` timed out at `Page.goto` `45000ms`.

### Fresh GUI cabinet evidence

- Google Search Console for the live property is still blocked:
  - route: `search.google.com/search-console?...resource_id=sc-domain:xn--l1acaw.xn--p1ai`;
  - visible message: `У вас нет доступа к этому ресурсу`;
  - visible resource: `мунн.рф`.
- Therefore the canonical GSC-side blocker remains active: `новая property не подтверждена, traffic migration не доказан`.
- Yandex.Webmaster for the live host is accessible:
  - visible host selector: `https://мунн.рф`;
  - visible page: `Переобход страниц`;
  - route: `webmaster.yandex.ru/site/https:xn--l1acaw.xn--p1ai:443/indexing/reindex/`.
- Yandex reindex status for the bounded batch submitted on `2026-06-19 09:11 MSK`:
  - `/podrostkovyy-lager-psihologiya`: `Заявка обработана`;
  - `/otzivi`: `Заявка обработана`;
  - `/psiholog-konsultacii-moskva`: `Заявка обработана`;
  - `/kartiny-tatiany-munn`: `Заявка обработана`;
  - `/psypodgotovka1`: `Заявка обработана`;
  - `/sitemap.xml`: `В очереди`.

### Local canon anchors

- `assets/moonn-five-page-seo-sprint-layer.js` exists in the canonical worktree.
- `git rev-parse --verify 49a093e` still resolves locally.

## T+28/T+30 decision

- The 2026-05-21 sprint is now at approximately T+30.
- Do not retire or narrow the automation yet:
  - GSC live property is still inaccessible, so Google-side migration and traffic impact are unproven;
  - rendered page-level verification is still red/mixed on 4 of 5 pages;
  - Yandex reindex has processed the five pages, but sitemap is still queued.
- The strongest next step is not another broad reindex. It is a targeted fix for rendered navigation durability plus live-property access/metrics proof.

## Blockers

- `P0` GSC property blocker persists: `новая property не подтверждена, traffic migration не доказан`.
- `P1` Rendered page-level blocker persists on 4 of 5 pages: gallery, exam prep, consultations and reviews still hit `Page.goto` `45000ms`.
- `P1` Source cleanup debt remains: raw H1 anomalies, gallery placeholders and missing image `alt`.
- `P1` Yandex sitemap reindex is still queued even though the five submitted page URLs are processed.

## Не делалось

- No Tilda edits.
- No canonical rewrites in page settings.
- No privacy/legal edits.
- No GSC submission because the live property is still inaccessible there.
- No Yandex.Metrika edits.
- No new Yandex.Webmaster submissions.
- No 83-URL batch actions.
- No cabinet settings changes.

## Следующий action

1. Keep the GSC blocker exactly as-is until `sc-domain:xn--l1acaw.xn--p1ai` becomes accessible.
2. Re-check Yandex sitemap queued status in the next run; do not resubmit the already processed page URLs.
3. Split or harden rendered navigation further so the 4 timeout pages produce DOM evidence without requiring a whole-run retry.
4. Do not propose automation retirement at T+28/T+30 yet, because the live Google property blocker is still open and the rendered page-level gate is not green across all 5 URLs.

## Self-review

- Что проверено: raw live HTTP/sitemap/robots/canonical state for all 5 scoped `мунн.рф` URLs; rendered audit after tool hardening; fresh GSC blocker screen; fresh Yandex.Webmaster submitted-URL statuses; local canon anchors `assets/moonn-five-page-seo-sprint-layer.js` and commit `49a093e`.
- Что реально изменено: rendered-audit cleanup logic in `scripts/moonn_five_page_seo_sprint_audit.py`, dated raw/rendered audit artifacts, this dated growth check, backlog/ledger/history updates.
- Где была ошибка/риск: первый rendered run timed out and produced no artifact; without tool hardening this could be falsely reported as no fresh rendered evidence instead of an audit-tool durability defect.
- Новое правило: rendered audit failures must close page/context/browser resources best-effort and still produce dated partial artifacts; a timeout with no dated artifact remains partial/blocked evidence.
