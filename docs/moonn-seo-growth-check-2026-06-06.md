# Moonn SEO Growth Check — 2026-06-06

## Scope

- Project: Moonn / Tatyana Munn site.
- Workstream: Moonn SEO/privacy supervisor.
- Branch for this run: `codex/moonn-seo-supervisor-20260606` from `origin/codex/moonn-seo-audit`.
- Live domain under test: `https://мунн.рф/` (`https://xn--l1acaw.xn--p1ai/` for technical fetches).
- Legacy evidence lane: `https://moonn.ru/` only when explicitly labeled historical/legacy.

## Проверенные факты

### Git / routing

- Текущий открытый checkout был `codex/moonn-camp-page-update`, то есть чужой контур для этого supervisor.
- Каноническая ветка `codex/moonn-seo-audit` занята отдельным worktree, поэтому этот прогон изолирован на `codex/moonn-seo-supervisor-20260606` от `origin/codex/moonn-seo-audit`.
- В worktree есть несвязанный untracked путь `docs/teen-psychology-camp-2026/remotion-teen-camp-promo/`; он не трогался и не включается в этот run.

### Live HTTP on `мунн.рф`

- Browser-like HTTP HEAD verification returned `200` for:
  - `https://мунн.рф/`
  - `https://мунн.рф/events_tp`
  - `https://мунн.рф/lectures1`
  - `https://мунн.рф/psiholog-konsultacii-moskva`
  - `https://мунн.рф/sitemap.xml`
  - `https://мунн.рф/robots.txt`
- Server path is now behind `ddos-guard`; earlier simple headless fetches that returned `403` should be treated as fetch-method noise, not as live-page outage.

### Five-page rendered audit on `мунн.рф`

- Ran:
  - `python scripts\moonn_five_page_seo_sprint_audit.py --packet docs\moonn-five-page-seo-packets-2026-05-21.json --rendered --base-url https://xn--l1acaw.xn--p1ai --out-prefix moonn-five-page-seo-sprint-audit-2026-06-06`
- New artifacts:
  - `docs/moonn-five-page-seo-sprint-audit-2026-06-06.json`
  - `docs/moonn-five-page-seo-sprint-audit-2026-06-06.md`
- All 5 packetized pages returned `200`, are present in sitemap, and are not blocked by `robots.txt`.
- Rendered H1 count is `1` on all 5 pages.
- Rendered answer block count:
  - `/podrostkovyy-lager-psihologiya` -> `0`
  - other 4 packet pages -> `1`

### New-domain canonical / packet drift

- Camp page improved in one layer: canonical is now self-referential on `https://xn--l1acaw.xn--p1ai/podrostkovyy-lager-psihologiya`.
- But the same camp page now mismatches the old sprint packet contract:
  - live `<title>`: `Подростковый психологический интенсив 14-17 лет в Москве | Татьяна Мунн`
  - expected packet title: `Подростковый психологический лагерь в Москве | Татьяна Мунн`
  - live description also reflects `интенсив`, not the old `лагерь` packet wording.
- Therefore the camp page is not a pure live regression anymore; it is a mixed state of:
  - real AEO issue: rendered answer block still `0`;
  - stale supervisor contract: packet still expects the pre-reframe camp metadata.
- The other 4 packet pages still expose `canonical_mismatch` to legacy `https://moonn.ru/...`.

### Raw SEO debt still visible

- Camp page: `raw_h1_count_not_one`, `images_missing_alt`.
- Gallery page: `canonical_mismatch`, `placeholder_text`, `images_missing_alt`.
- Consultations page: `canonical_mismatch`, `raw_h1_count_not_one`, `images_missing_alt`.
- Reviews page: `canonical_mismatch`, `raw_h1_count_not_one`, `images_missing_alt`.

### Analytics / cabinet access attempts

- Repo search still found no committed API/export artifacts for the requested analytics contract; latest canonical API blockers remain:
  - Yandex.Metrika API: `403 access_denied`
  - Yandex.Webmaster API: `403 INVALID_OAUTH_TOKEN`
  - Google Search Console API: `401 Login Required`
- Bounded GUI fallback was attempted through the real `Alexander` Chrome profile without changing settings.
- Google Search Console for new property still blocks access in this run:
  - window title: `Oops, you don't have access to this property`
  - account: `rublevalexandermsu@gmail.com`
  - property: `xn--p1ai`
- Yandex.Webmaster for new host also blocks access in this run:
  - visible warning: `Сайт https://xn--l1acaw.xn--p1ai вам не принадлежит. Добавьте его в список ваших сайтов и подтвердите права на него`
- New-domain traffic metrics were not collected in this run:
  - the active Metrika session was already sitting inside an unsaved goal-creation modal;
  - to avoid interfering with cabinet state, no metric-navigation clicks or form actions were performed.
- Required blocker wording remains unchanged: `новая property не подтверждена, traffic migration не доказан`.

### Privacy / RKN lane

- Full weekly privacy layer was not run today because today is Saturday, 2026-06-06.
- No live privacy/publication changes were made.

### MIIIIPS lane

- MIIIIPS PR `#11` deploy/merge verification is still blocked in repo context: canonical repo + PR URL remains missing.

## Blockers

1. `P0` `новая property не подтверждена, traffic migration не доказан`.
2. `P0` Yandex.Webmaster host for `мунн.рф` is also not verified for the current operator.
3. `P0` Camp page still has a real AEO problem: rendered answer block is `0`.
4. `P0` Supervisor contract drift: packet `docs/moonn-five-page-seo-packets-2026-05-21.json` still expects old `лагерь` metadata for the camp page, so future runs will keep mixing stale expectations with live facts until the packet is split or refreshed.
5. `P1` Canonical migration remains incomplete on 4 of 5 packet pages: gallery, `psypodgotovka1`, consultations, reviews still point to `moonn.ru`.
6. `P1` Raw SEO cleanup debt remains: placeholders, raw H1 anomalies, and missing `alt`.
7. `P1` MIIIIPS PR `#11` remains unverifiable because the canonical PR URL is still absent from repo docs/registry.

## Не делалось

- No Tilda edits.
- No legal/privacy publication.
- No GSC/Yandex property verification actions.
- No reindex submissions.
- No screenshots were saved or committed.
- No Metrika goal form interactions were made.
- No 83-URL actions.

## Follow-up

1. Refresh or split the five-page packet so the camp page is measured against the approved `интенсив` contour, not the old `лагерь` wording.
2. Fix native canonical on the remaining 4 scoped `мунн.рф` pages so they stop pointing to `https://moonn.ru/...`.
3. Inspect the live camp page source/runtime in Tilda and explain why rendered answer block stays `0` after the legal/public copy reframe.
4. Verify or obtain access to the GSC property for `мунн.рф`; until then keep all GSC traffic numbers labeled legacy-only.
5. Verify or obtain access to the Yandex.Webmaster host for `мунн.рф`; until then do not claim new-domain reindex status.
6. Create a read-only Metrika collection route for `96397286` that does not start from `goals?...goal_create=new`, so supervisor runs cannot collide with unsaved settings state.
7. Record the canonical MIIIIPS PR `#11` repo + URL in a stable doc/registry to stop repeating the same unknown-PR blocker.

## Self-review

- Requested scope: daily limited supervisor over live `мунн.рф`, analytics/growth access, and privacy cadence.
- Completed: routing correction, live HTTP check, new-domain rendered audit, bounded GSC/Yandex GUI blocker verification, backlog-worthy blocker classification.
- Not completed: new-domain analytics aggregates, privacy weekly audit, MIIIIPS PR verification.
- Key algorithm fix from this run: do not treat the camp page as a single SEO regression when the live page and the packet contract have diverged. First separate true live breakage from stale packet expectations.
