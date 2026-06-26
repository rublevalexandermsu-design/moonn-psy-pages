# Moonn SEO Growth Check — 2026-06-26

## Scope

- Project: Moonn / Tatyana Munn site.
- Workstream: `moonn-five-page-seo-aeo-supervisor`.
- Branch: `codex/moonn-seo-audit`.
- Live domain under test: `https://мунн.рф/` (`https://xn--l1acaw.xn--p1ai/` for technical fetches).
- Legacy analytics lane: `https://moonn.ru/` remains historical only and was not used as a working property in this run.
- Reindex scope stayed limited to the approved five URLs plus sitemap; no 83-URL batch.

## Проверенные факты

### Raw and rendered live audit on `мунн.рф`

- First rendered attempt used too short an outer command timeout and produced no artifact; it was not counted as evidence.
- A first completed run surfaced `not_in_sitemap` and `canonical_mismatch` on all five URLs, but direct sitemap inspection showed the five URLs present in punycode form. The audit script was then hardened to compare Unicode and punycode IDN URLs in one normalized form.
- Final completed run after audit hardening:
  - `python scripts\moonn_five_page_seo_sprint_audit.py --rendered --base-url https://мунн.рф --out-prefix moonn-five-page-seo-sprint-audit-2026-06-26`
- New dated artifacts:
  - `docs/moonn-five-page-seo-sprint-audit-2026-06-26.json`
  - `docs/moonn-five-page-seo-sprint-audit-2026-06-26.md`
- DNS for `мунн.рф` resolves to the punycode lookup host `xn--l1acaw.xn--p1ai`.
- All 5 scoped live URLs on `мунн.рф` returned HTTP `200`.
- All 5 scoped URLs are present in `sitemap.xml` after IDN normalization.
- `robots.txt` was fetched and none of the five scoped URLs is blocked.
- Raw canonical is aligned to the live domain after IDN normalization: canonical is emitted as `https://xn--l1acaw.xn--p1ai/...`, which is the punycode form of `https://мунн.рф/...`.
- Titles and descriptions still match the 2026-05-21 packet on all 5 scoped pages.
- Source-level debt remains:
  - camp raw H1 count is `0`, missing raw image `alt` count is `1`;
  - gallery raw H1 count is `1`, still exposes `Your Name` and `Your Email`, missing raw image `alt` count is `2`;
  - exam prep raw H1 count is `1`, missing raw image `alt` count is `1`;
  - consultations raw H1 count is `2`, missing raw image `alt` count is `11`;
  - reviews raw H1 count is `2`, missing raw image `alt` count is `10`.

### Rendered page-level result

- The run completed and produced a dated artifact, but the page-level gate is still mixed:
  - camp `/podrostkovyy-lager-psihologiya` completed with `renderedStatus=ok`, `h1CountRendered=1`, `answerBlockCountRendered=1`;
  - gallery `/kartiny-tatiany-munn` timed out at `Page.goto` `45000ms`;
  - exam prep `/psypodgotovka1` timed out at `Page.goto` `45000ms`;
  - consultations `/psiholog-konsultacii-moskva` timed out at `Page.goto` `45000ms`;
  - reviews `/otzivi` timed out at `Page.goto` `45000ms`.

### Cabinet evidence

- No fresh Google Search Console proof was obtained in this run.
- No fresh Yandex.Webmaster GUI/API proof was obtained in this run.
- Latest confirmed GSC evidence remains the 2026-06-20 GUI check: `sc-domain:xn--l1acaw.xn--p1ai` / visible resource `мунн.рф` showed no access. Therefore the canonical blocker remains active: `новая property не подтверждена, traffic migration не доказан`.
- Latest confirmed Yandex.Webmaster evidence remains the 2026-06-21 GUI check: the five submitted page URLs were `Заявка обработана`; `sitemap.xml` remained `В очереди`. This was not freshly rechecked today.

### Local canon anchors

- `assets/moonn-five-page-seo-sprint-layer.js` exists in the canonical worktree.
- Commit `49a093e` resolves locally as `49a093e Add Moonn five-page SEO sprint packet`.

## T+37 decision

- The 2026-05-21 sprint is now approximately T+37.
- Do not retire or narrow the automation yet:
  - GSC live property remains unconfirmed from latest successful proof, so Google-side migration and traffic impact are unproven;
  - rendered page-level verification is still mixed on 4 of 5 pages;
  - source cleanup debt remains on raw H1, gallery placeholders and image `alt`;
  - Yandex sitemap processing was not freshly rechecked after the previous `В очереди` status.

## Blockers

- `P0` GSC property blocker persists from latest confirmed proof: `новая property не подтверждена, traffic migration не доказан`.
- `P1` Rendered page-level blocker persists on 4 of 5 pages: gallery, exam prep, consultations and reviews still hit `Page.goto` `45000ms`.
- `P1` Yandex sitemap status is stale from 2026-06-21 and still needs a bounded re-check; do not resubmit the already processed page URLs.
- `P1` Source cleanup debt remains: raw H1 anomalies, gallery placeholders and missing image `alt`.
- `P0` Weekly privacy/RKN audit from 2026-06-22 found live-domain compliance blockers: four standard privacy endpoints return `404`, `78/83` production URLs have form signals without detected checkbox, and Yandex Metrika is present on `83/83` checked pages.

## Не делалось

- No Tilda edits.
- No canonical rewrites in page settings.
- No privacy/legal edits.
- No GSC submission.
- No Yandex.Metrika edits.
- No new Yandex.Webmaster submissions.
- No 83-URL batch actions.
- No cabinet settings changes.

## Следующий action

1. Re-check Yandex sitemap queued status through a safer bounded cabinet/API route; do not resubmit the already processed page URLs.
2. Keep the GSC blocker exactly as-is until `sc-domain:xn--l1acaw.xn--p1ai` becomes accessible in a verified live-property route.
3. Split or harden rendered navigation further so the 4 timeout pages produce DOM evidence without requiring a whole-run retry.
4. Keep source cleanup as approval-required Tilda work: raw H1 normalization, gallery placeholders and missing image `alt`.
5. Keep privacy rollout approval-gated: confirm operator address/legal text, publish approved endpoints/check boxes, then rerun the live-domain privacy audit.

## Self-review

- Что проверено: raw live HTTP/sitemap/robots/canonical state for all 5 scoped `мунн.рф` URLs; rendered audit; local canon anchors `assets/moonn-five-page-seo-sprint-layer.js` and commit `49a093e`.
- Что реально изменено: IDN normalization in `scripts/moonn_five_page_seo_sprint_audit.py`, dated audit artifacts, this dated growth check, backlog/history/ledger updates.
- Где была ошибка/риск: the first rendered attempt had an outer timeout shorter than the script's worst-case page-timeout budget; the first completed audit also risked a false sitemap/canonical regression because it compared Unicode and punycode URL forms literally.
- Новое правило: normalize IDN URL forms before comparing sitemap/canonical evidence, and ensure rendered command-level timeout exceeds `launch_timeout + page_timeout * page_count + watchdog buffer`.
