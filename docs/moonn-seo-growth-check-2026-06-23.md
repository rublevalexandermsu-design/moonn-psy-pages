# Moonn SEO Growth Check — 2026-06-23

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
  - `python scripts\moonn_five_page_seo_sprint_audit.py --packet docs\moonn-five-page-seo-packets-2026-05-21.json --base-url https://xn--l1acaw.xn--p1ai --out-prefix moonn-five-page-seo-sprint-audit-2026-06-23`
- New dated artifacts:
  - `docs/moonn-five-page-seo-sprint-audit-2026-06-23.json`
  - `docs/moonn-five-page-seo-sprint-audit-2026-06-23.md`
- DNS for `xn--l1acaw.xn--p1ai` resolves on this host.
- All 5 scoped live URLs on `мунн.рф` returned HTTP `200`.
- All 5 scoped URLs remain in `sitemap.xml` and are not blocked by `robots.txt`.
- Raw canonical still matches `мунн.рф` / `xn--l1acaw.xn--p1ai` on all 5 scoped URLs.
- Source-level debt remains:
  - camp raw H1 count is `0`, missing raw image `alt` count is `1`;
  - gallery raw H1 count is `1`, still exposes `Your Name` and `Your Email`, missing raw image `alt` count is `2`;
  - exam prep raw H1 count is `1`, missing raw image `alt` count is `1`;
  - consultations raw H1 count is `2`, missing raw image `alt` count is `11`;
  - reviews raw H1 count is `2`, missing raw image `alt` count is `10`.

### Rendered audit on `мунн.рф`

- Rendered run completed and produced dated artifacts:
  - `docs/moonn-five-page-seo-sprint-audit-2026-06-23-rendered.json`
  - `docs/moonn-five-page-seo-sprint-audit-2026-06-23-rendered.md`
- Rendered result is still mixed, not green:
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
- `git rev-parse --verify 49a093e` resolves locally as `49a093e65f1b07afd20a9e1deea8bbe6961ee7dc`.

## T+33 decision

- The 2026-05-21 sprint is now at approximately T+33.
- Do not retire or narrow the automation yet:
  - GSC live property remains unconfirmed from the latest successful proof, so Google-side migration and traffic impact are unproven;
  - rendered page-level verification is still mixed on 4 of 5 pages;
  - Yandex sitemap processing was not freshly rechecked today after the previous `В очереди` status.
- The strongest next step remains targeted: use a safer GSC verification route, re-check Yandex sitemap status, and split/harden the rendered navigation path for the four timeout pages.

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

1. Keep the GSC blocker exactly as-is until `sc-domain:xn--l1acaw.xn--p1ai` becomes accessible in a verified live-property route.
2. Re-check Yandex sitemap queued status through a safer bounded cabinet/API route; do not resubmit the already processed page URLs.
3. Split or harden rendered navigation further so the 4 timeout pages produce DOM evidence without requiring a whole-run retry.
4. Keep source cleanup as approval-required Tilda work: raw H1 normalization, gallery placeholders and missing image `alt`.
5. Keep privacy rollout approval-gated: confirm operator address/legal text, publish approved endpoints/check boxes, then rerun the live-domain privacy audit.
6. Do not propose automation retirement yet, because the live Google property blocker is still open, the rendered page-level gate is not green across all 5 URLs, and privacy/RKN blockers remain open.

## Self-review

- Что проверено: raw live HTTP/sitemap/robots/canonical state for all 5 scoped `мунн.рф` URLs; rendered audit; local canon anchors `assets/moonn-five-page-seo-sprint-layer.js` and commit `49a093e`.
- Что реально изменено: dated raw/rendered audit artifacts, this dated growth check, backlog/history/ledger updates.
- Где была ошибка/риск: cabinet checks were not freshly verified today; carrying forward 2026-06-20/2026-06-21 cabinet evidence must stay explicitly labeled as stale/latest-confirmed, not fresh.
- Новое правило: if cabinet verification is not freshly completed, the run may record raw/rendered evidence but must not update GSC/Yandex statuses or infer traffic migration from legacy/currently inaccessible properties.
