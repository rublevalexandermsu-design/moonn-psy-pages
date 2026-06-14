# Moonn SEO Growth Backlog

Canonical backlog for Moonn SEO/AEO growth checks, analytics evidence and privacy/RKN follow-up.

## 2026-05-20

1. `P0` Analytics access: obtain Yandex.Metrika export or OAuth/API access for counter `96397286`.
2. `P0` Analytics access: obtain Google Search Console export or API access for property `https://moonn.ru/`.
3. `P0` Report contract: every SEO-growth report must include visits/users/pageviews, acquisition sources, search phrases, top landing pages, click goals and blockers.
4. `P1` Robots: decide and fix `/psy4psy`, `/schematherapy`, `/selfharm`.
5. `P1` Images: build source-level image alt/title remediation packet for the 83 production URLs.
6. `P1` Privacy endpoints: decide whether `/politic` remains canonical or whether `/privacy`, `/cookies`, `/personal-data-consent`, `/data-subject-request` must be published after legal approval.
7. `P2` Audit durability: keep dated audit outputs and never overwrite historical reports during supervisor runs.

## 2026-05-21 — Five-Page SEO/AEO Sprint

1. `DONE 2026-05-21` Tilda publication gate: applied `docs/moonn-five-page-seo-packets-2026-05-21.json` through authenticated Alexander/Rublev Chrome and published only the five scoped pages.
2. `DONE 2026-05-21` HEAD/AEO gate: added `docs/moonn-five-page-seo-sprint-head-snippet-2026-05-21.html` to each scoped page HEAD; rendered answer blocks, FAQ/schema and click goals are live.
3. `DONE 2026-05-21` Technical live check: `scripts/moonn_five_page_seo_sprint_audit.py --packet docs/moonn-five-page-seo-packets-2026-05-21.json --rendered` confirms 200, sitemap true, robots false, rendered H1 = 1, rendered answer block = 1 and no rendered placeholders on all five pages.
4. `P0` Reindex scope: submit only `docs/moonn-five-page-reindex-urls-2026-05-21.txt` and sitemap in Google Search Console/Yandex Webmaster; do not resubmit all 83 URLs.
5. `P0` Source cleanup: remove raw placeholders from camp/gallery and replace missing raw image alt attributes on the five pages at source/Tilda level.
6. `P1` Measurement: collect T+14/T+28 GSC and Yandex.Metrika page/query evidence for the five URLs and write results into `docs/moonn-five-page-seo-change-ledger-2026-05-21.json`.
7. `P1` Content cluster: prepare the next 20-40 support pages/FAQ/cases around parents of teenagers, exam anxiety, communication and self-esteem only after the five-page technical layer is green.

## 2026-05-22 — Supervisor Run

1. `P0` Live fetch blocker: Codex sandbox HTTP checks returned `http_ERROR` for all 5 pages (no raw metrics). Windows MCP lightweight fetch got `403` for 4/5 URLs (non-browser access blocked). Required: verify via authenticated Chrome GUI (Rublev profile) or an allowlisted fetcher, and log the real HTTP/robots/sitemap results.
2. `P0` Public copy hygiene: `/otzivi` currently contains internal/technical explanatory paragraphs (“на данной странице… это нужно для поиска…”) and a placeholder-style image reference for “подтверждение отзыва”. This violates the “no internal layer” rule on public pages and should be rewritten/removed at Tilda source after explicit approval.
3. `P1` Audit durability: keep daily dated outputs (`docs/moonn-five-page-seo-sprint-audit-YYYY-MM-DD.*`) and avoid overwriting 2026-05-21 baseline.
4. `P0` Git workflow blocker: current environment denies write access to `.git` (cannot create `.git/index.lock`), so changes cannot be committed/pushed from Codex. Fix ACL/ownership or run git from a user with write permission, then commit the supervisor artifacts in one scoped commit.

## 2026-05-23 — Supervisor Run

1. `OK` Five-page non-rendered audit succeeded from this host: all 5 URLs returned HTTP 200, are in sitemap, and are not blocked by robots. Evidence: `docs/moonn-five-page-seo-sprint-audit-2026-05-23.json`.
2. `P0` Rendered verification remains unproven on this host: 2026-05-22 showed Playwright `WinError 5` and sandbox HTTP issues; keep treating rendered/DOM checks as GUI-only until Playwright is confirmed working.
3. `P0` Source cleanup remains: raw HTML still contains placeholder strings on 2 pages (camp/gallery) and missing `alt` on images across all 5 pages; requires explicit approval for Tilda source edits.
4. `P1` MIIIIPS PR #11 deploy/merge verification is still blocked: the referenced PR number was not found in `rublevalexandermsu-design/moonn-psy-pages`; needs the correct repo link or a saved canonical PR URL in the registry.

## 2026-05-24 — Supervisor Run

1. `OK` Five-page rendered audit succeeded from this host: all 5 URLs returned HTTP 200, are in sitemap, and are not blocked by robots. Evidence: `docs/moonn-five-page-seo-sprint-audit-2026-05-24.json`.
2. `P0` AEO regression/scope issue: `https://moonn.ru/podrostkovyy-lager-psihologiya` rendered answer block count is `0` (should be `1` for the five-page sprint). Needs investigation in live HTML/rendered DOM and Tilda HEAD injection for this page only (do not touch other URLs).
3. `P0` Source cleanup unchanged: raw HTML still contains placeholder strings on 2 pages (camp/gallery) and missing `alt` on images across all 5 pages; requires explicit approval for Tilda source edits.
4. `P1` Raw H1 remains non-canonical on 3 pages (camp/consultations/reviews) even though rendered H1 is `1`. Treat as technical debt until source-level H1 is fixed.

## 2026-05-25 — Supervisor Run

1. `OK` Five-page rendered audit succeeded from this host: all 5 URLs returned HTTP `200`, are in sitemap, and are not blocked by robots. Evidence: `docs/moonn-five-page-seo-sprint-audit-2026-05-25.json`.
2. `P0` AEO gap persists on camp page: `https://moonn.ru/podrostkovyy-lager-psihologiya` rendered answer block count is still `0` (expected `1` for the sprint layer). Investigate in live HTML/rendered DOM and the page’s Tilda HEAD injection for this page only (no other URLs).
3. `P0` Source cleanup unchanged: raw placeholder strings remain on 2 pages (camp/gallery), and missing raw image `alt` remains across all 5 pages; requires explicit approval for Tilda source edits.
4. `P1` Raw H1 remains non-canonical on 3 pages (camp/consultations/reviews) even though rendered H1 is `1`. Track as technical debt until source-level H1 is fixed.

## 2026-05-25 — Supervisor Run (Monday, weekly privacy layer)

1. `DONE 2026-05-25` Weekly privacy audit executed (low-risk, local script). Evidence: `docs/moonn-privacy-compliance-audit-2026-05-25.{json,md}`.
2. `P0` Privacy publication gap: policy endpoints return `404` — `/privacy`, `/personal-data-consent`, `/cookies`, `/data-subject-request`. Treat as a hard blocker for RKN/privacy readiness until a legally approved publication plan is executed.
3. `P0` Forms + consent gap (audit signal): `forms_without_detected_checkbox` flagged across most of the 83 URLs. Needs a constrained, page-template-level verification in Tilda (checkbox + consent link text) after explicit approval; do not “fix blindly” by injecting text via JS.
4. `P0` AEO regression persists: `https://moonn.ru/podrostkovyy-lager-psihologiya` rendered answer block count is still `0` (expected `1`). Next step is a single-page DOM/HEAD inspection in authenticated Chrome to confirm what exactly is missing (JSON-LD vs visible block vs selector drift).
5. `P1` Image hygiene debt persists: missing `alt` is still non-trivial across the five pages (e.g., `/psiholog-konsultacii-moskva`, `/otzivi`). Prepare a source-level alt remediation packet (per-page list of image URLs -> target alt) before any live edits.
6. `P0` Analytics evidence still blocked: no new API/export artifacts for Yandex.Metrika `96397286`, Yandex Webmaster, or GSC were produced in this run. Next action: bounded GUI-only collection via Rublev Chrome profile for `2026-04-29..today` (aggregate metrics + top landings/queries), without changing settings.
7. `P1` MIIIIPS PR #11 remains untraceable from repo context: store the canonical repo+PR URL in a registry/doc to prevent repeated “unknown PR” blockers.

## 2026-05-26 — Supervisor Run

1. `OK` Five-page rendered audit succeeded from this host: all 5 URLs returned HTTP `200`, are in sitemap, and are not blocked by robots. Evidence: `docs/moonn-five-page-seo-sprint-audit-2026-05-26.json` and `docs/moonn-five-page-seo-sprint-audit-2026-05-26-rendered.json`.
2. `P0` AEO gap persists on camp page: `https://moonn.ru/podrostkovyy-lager-psihologiya` rendered answer block count is still `0` (expected `1` for the sprint layer). Confirm via authenticated Chrome DOM/HEAD inspection for this page only (no other URLs).
3. `P0` Source cleanup unchanged: raw placeholder strings remain on 2 pages (camp/gallery), and missing raw image `alt` remains across all 5 pages; requires explicit approval for Tilda source edits.
4. `P1` Raw H1 remains non-canonical on 3 pages (camp/consultations/reviews) even though rendered H1 is `1`. Track as technical debt until source-level H1 is fixed.
5. `P0` Analytics evidence still blocked in practice: attempted GUI access hit re-auth/identity prompts for Google Search Console and Yandex services; no new aggregates for `2026-04-29..2026-05-26` were captured in this run.
6. `P0` Next bounded step: in Rublev Chrome profile, complete re-auth if prompted and capture only aggregate numbers (Metrika + GSC + Webmaster) without changing settings; store results as a dated `docs/moonn-seo-growth-check-YYYY-MM-DD.md` entry.
7. `P2` Tooling hardening: keep `scripts/moonn_five_page_seo_sprint_audit.py --rendered` bounded by timeouts so the supervisor cannot hang indefinitely.

## 2026-05-27 — Supervisor Run

1. `OK` Priority URLs HTTP `200`: `https://moonn.ru/`, `/events_tp`, `/lectures1`, `/psiholog-konsultacii-moskva`, plus `sitemap.xml` and `robots.txt`.
2. `OK` Daily five-page audit artifacts created (includes rendered checks in-report):
   - `docs/moonn-five-page-seo-sprint-audit-2026-05-27.json`
   - `docs/moonn-five-page-seo-sprint-audit-2026-05-27.md`
3. `P0` Persistent AEO gap (camp page): `https://moonn.ru/podrostkovyy-lager-psihologiya` rendered answer block remains `0` (expected `1` for the sprint layer), while the sprint layer tag is present in raw HTML. Next action is still a single-page DOM/HEAD+console inspection in authenticated Chrome (Rublev profile) to locate the break (selector drift vs JS error vs loading order).
4. `P0` Source cleanup remains (approval-required for Tilda edits): placeholder text still present on camp + gallery pages; missing image `alt` remains across all five pages (notably high on consultations + reviews).
5. `P1` Raw H1 anomalies persist (SEO hygiene): raw H1 count != 1 on consultations + reviews, and is `0` on camp (rendered H1 stays `1`). Track as source/template cleanup after the AEO gap is resolved.
6. `P0` Analytics evidence still missing: no API exports and no GUI-verified aggregates collected for `2026-04-29..today` (Yandex.Metrika `96397286`, Yandex Webmaster, Google Search Console). Needs a bounded Rublev-profile GUI collection run without changing settings.
7. `P1` MIIIIPS PR #11 deploy/merge verification remains blocked: canonical repo+PR URL is still not present in this repo; record it in a doc/registry once the correct link is available.

## 2026-05-28 — Supervisor Run

1. `P0` Infra blocker (DNS): this host could not resolve `moonn.ru` (`Errno 11001 getaddrinfo failed`), so all live HTTP/robots/sitemap checks are invalid in this run.
2. `OK` Daily five-page audit artifacts created, but all pages are `http_ERROR` due to DNS (do not treat as regression evidence):
   - `docs/moonn-five-page-seo-sprint-audit-2026-05-28.json`
   - `docs/moonn-five-page-seo-sprint-audit-2026-05-28.md`
3. `P0` GUI fallback blocker: `windows-mcp` failed (`Snapshot` timeout; `Screenshot` transport closed), so bounded Rublev-profile Chrome checks could not be performed in this run.
4. `OK` Repo canon still present (local-only): `assets/moonn-five-page-seo-sprint-layer.js` exists; commit `49a093e` exists in git object database.
5. Next action: re-run the same `--rendered` audit once DNS/network is restored, then proceed with the bounded Chrome GUI investigation for the camp AEO gap and the scoped reindex for only the 5 URLs (no 83-URL batch).

## 2026-05-29 — Supervisor Run

1. `P0` Infra blocker persists: DNS for `moonn.ru` is still broken on this host (`Errno 11001 getaddrinfo failed`).
2. `OK` Daily five-page audit now fast-fails on DNS and writes explicit evidence instead of hanging:
   - `docs/moonn-five-page-seo-sprint-audit-2026-05-29.json`
   - `docs/moonn-five-page-seo-sprint-audit-2026-05-29.md`
3. `P0` Analytics evidence still missing for `2026-04-29..today`: no API exports committed, and no GUI-verified aggregates collected (needs Rublev Chrome profile on a host with working DNS).

## 2026-05-30 — Supervisor Run

1. `P0` Infra blocker persists: DNS for `moonn.ru` is still broken on this host (`Errno 11001 getaddrinfo failed`).
2. `OK` Daily five-page audit recorded (DNS-blocked, fast-fail):
   - `docs/moonn-five-page-seo-sprint-audit-2026-05-30.json`
   - `docs/moonn-five-page-seo-sprint-audit-2026-05-30.md`
3. Next action (unchanged): restore DNS / run bounded Rublev-profile GUI checks / submit scoped reindex ONLY for the 5 URLs (no 83-URL batch).

## 2026-05-31 — Supervisor Run

1. `P0` Infra blocker persists: DNS for `moonn.ru` is broken on this host (`DNS-имя не существует` / `Errno 11001 getaddrinfo failed`).
2. `OK` Daily five-page audit recorded (DNS-blocked, fast-fail):
   - `docs/moonn-five-page-seo-sprint-audit-2026-05-31.json`
   - `docs/moonn-five-page-seo-sprint-audit-2026-05-31.md`
   - `docs/moonn-five-page-seo-sprint-audit-2026-05-31-rendered.json`
   - `docs/moonn-five-page-seo-sprint-audit-2026-05-31-rendered.md`
3. `OK` Repo canon still present (local-only): `assets/moonn-five-page-seo-sprint-layer.js` exists; commit `49a093e` exists.
4. `P1` MIIIIPS PR #11 deploy/merge verification remains blocked: canonical repo+PR URL is still missing in this repo context.
5. Next action (unchanged): restore DNS / run bounded Rublev-profile GUI checks / submit scoped reindex ONLY for the 5 URLs (no 83-URL batch).

## 2026-06-01 — Supervisor Run

1. `P0` Infra blocker persists: this host still cannot resolve `moonn.ru` (PowerShell: `Этот хост неизвестен (moonn.ru:443)`; Python: `ERROR:[Errno 11001] getaddrinfo failed`).
2. `OK` Weekly privacy audit executed in fast-fail mode (DNS-blocked) and wrote dated artifacts:
   - `docs/moonn-privacy-compliance-audit-2026-06-01.json`
   - `docs/moonn-privacy-compliance-audit-2026-06-01.md`
3. `P0` Supervisor durability fix: `scripts/moonn_privacy_compliance_audit.py` now preflights `https://moonn.ru/robots.txt` and fast-fails DNS outages instead of hanging on 83 URL fetches.
4. `P0` Analytics evidence still missing for `2026-04-29..today`: no exports committed; GUI run (Rublev Chrome profile) not performed in this run; do not claim SEO success from traffic.
5. `P1` MIIIIPS PR #11 deploy/merge verification remains blocked: canonical repo+PR URL still missing; record it once available.

## 2026-06-01 — Supervisor Run

1. `P0` Infra blocker persists: DNS for `moonn.ru` is broken on this host (`Errno 11001 getaddrinfo failed`).
2. `OK` Daily five-page audit recorded (DNS-blocked, fast-fail):
   - `docs/moonn-five-page-seo-sprint-audit-2026-06-01.json`
   - `docs/moonn-five-page-seo-sprint-audit-2026-06-01.md`
3. `OK` Repo canon still present (local-only): `assets/moonn-five-page-seo-sprint-layer.js` exists; commit `49a093e` exists.
4. Next action (unchanged): restore DNS / run bounded Rublev-profile GUI checks / submit scoped reindex ONLY for the 5 URLs (no 83-URL batch).

## 2026-06-02 — Supervisor Run

1. `P0` Infra blocker persists: DNS for `moonn.ru` is still broken on this host (`Errno 11001 getaddrinfo failed`), so live HTTP/sitemap/robots/rendered checks remain invalid in this run.
2. `OK` Daily five-page audit recorded (DNS-blocked, fast-fail):
   - `docs/moonn-five-page-seo-sprint-audit-2026-06-02.json`
   - `docs/moonn-five-page-seo-sprint-audit-2026-06-02.md`
3. `OK` Repo canon still present (local-only): `assets/moonn-five-page-seo-sprint-layer.js` exists; commit `49a093e` resolves in git object database.
4. `OK` Bounded GUI evidence was captured this time:
   - GSC property `https://moonn.ru/` is accessible in Rublev/Alexander Chrome; visible metrics: `240` clicks, `14.5K` impressions, CTR `1.7%`, average position `7.3`, last update `4 hours ago`, overview indexing `40 indexed / 135 not indexed`.
   - Yandex.Metrika counter `96397286` is accessible in Rublev/Alexander Chrome, but only the default weekly slice was captured (`27 May - 2 Jun`: `53` visits, `46` visitors, `85` pageviews).
5. `P0` Analytics contract is still incomplete for the required period `2026-04-29..today`: top landing pages, search phrases, goals and full-period cuts were not yet collected.
6. `P0` Yandex.Webmaster remains blocked in practice: direct Moonn dashboard attempt landed on Yandex `404`; canonical host dashboard URL must be recorded before the next run.
7. `P1` MIIIIPS PR #11 deploy/merge verification remains blocked: canonical repo+PR URL is still missing in this repo context.
8. Next bounded action: restore DNS / finish full-period GUI collection / submit scoped reindex ONLY for the 5 URLs plus sitemap when access is confirmed (no 83-URL batch and no settings changes).

## 2026-06-03 — SEO/Growth GUI Supervisor Run

1. `P0` Infra blocker persists: this host still cannot resolve `moonn.ru` (`Errno 11001 getaddrinfo failed` / `Этот хост неизвестен`), so live HTTP, sitemap, robots and rendered DOM checks remain invalid locally.
2. `OK` GSC GUI fallback improved: property `https://moonn.ru/` is accessible in the real `Alexander` Chrome profile; current visible metrics are `245` clicks, `14.6K` impressions, CTR `1.7%`, average position `7.4`, last update `3.5 hours ago`, indexing `40 indexed / 135 not indexed`.
3. `OK` Yandex.Webmaster route is now canonicalized: use `https://webmaster.yandex.ru/site/https:moonn.ru:443/indexing/reindex/` (not the broken `/sites/` guess). Priority URLs `/`, `/events_tp`, `/lectures1`, `/psiholog-konsultacii-moskva` all show `Заявка обработана` from `08.05.2026 9:20`.
4. `P0` GSC analytics contract is still incomplete: today's GUI capture is from the default `3 months` view and does not yet include the exact requested custom period `2026-04-29..2026-06-03`, top pages export, or 4 priority URL Inspection statuses.
5. `P0` Metrika analytics contract is still incomplete: today's GUI capture stayed on the weekly slice `28 May - 3 Jun` (`105` pageviews, `78` visits, `69` visitors) and did not yet capture the requested full period, search phrases or click goals.
6. `P1` Measurement-quality incident: visible Metrika top-page tables are now polluted by supervisor/test querystrings (`?payment-click-audit=20260602`, `?hero-live-check=20260602-2`, `?verify=20260603-*`, `?cartqa*`). Future growth reads should normalize or exclude QA URLs so measurement is not biased by automation traffic.
7. `P1` MIIIIPS PR #11 deploy/merge verification remains blocked: canonical repo+PR URL is still missing in this repo context.

## 2026-06-03 — Supervisor Run

1. `P0` Infra blocker persists: DNS for `moonn.ru` is still broken on this host (`Errno 11001 getaddrinfo failed`), so live HTTP/sitemap/robots/rendered checks remain invalid in this run.
2. `OK` Daily five-page audit recorded (DNS-blocked, fast-fail):
   - `docs/moonn-five-page-seo-sprint-audit-2026-06-03.json`
   - `docs/moonn-five-page-seo-sprint-audit-2026-06-03.md`
3. `OK` Repo canon still present (local-only): `assets/moonn-five-page-seo-sprint-layer.js` exists; commit `49a093e` resolves in git object database.
4. `P0` No new analytics or reindex evidence was collected today; latest bounded GUI metrics remain the `2026-06-02` growth check, so do not treat today as a T+14/T+28 measurement step.
5. `P0` Next bounded action remains unchanged: restore DNS or move the run to a host with working resolution, then submit scoped reindex ONLY for the 5 approved URLs plus sitemap if GSC/Yandex access is available (no 83-URL batch).

## 2026-06-03 — `мунн.рф` Analytics Migration

1. `DONE` Codex automations were updated outside Git so the current live domain is `https://мунн.рф/` and `https://moonn.ru/` is treated as legacy analytics unless new evidence proves otherwise.
2. `DONE` Added migration contract:
   - `docs/moonn-rf-analytics-migration-2026-06-03.md`
   - `docs/moonn-rf-analytics-migration-2026-06-03.json`
3. `DONE` Added scoped new-domain reindex file: `docs/moonn-rf-five-page-reindex-urls-2026-06-03.txt`.
4. `DONE` Hardened local audits with `--base-url` so future supervisor runs can check `https://мунн.рф/` without rewriting historical packets:
   - `scripts/moonn_five_page_seo_sprint_audit.py`
   - `scripts/moonn_privacy_compliance_audit.py`
5. `DONE` Updated `data/site.json` current brand domain from `moonn.ru` to `мунн.рф`.
6. `P0` External cabinet action still needs authenticated GUI confirmation:
   - Google Search Console property for `https://мунн.рф/`;
   - Yandex.Webmaster host for `https://мунн.рф/`;
   - Yandex.Metrika counter `96397286` host attribution for `мунн.рф`;
   - Google Analytics / Google tag web stream for `мунн.рф`.
7. `P0` Do not claim traffic growth on `мунн.рф` from legacy `moonn.ru` GSC/Metrika data. Reports must separate `legacy-domain analytics` and `new-domain live checks`.
8. `P0` New-domain local audit found SEO blockers: five scoped pages return HTTP `200`, but are not detected in `https://мунн.рф/sitemap.xml` and still show `canonical_mismatch`. Fix Tilda/domain canonical and sitemap behavior before calling SEO migration complete.
9. `P0` New-domain privacy smoke check found `/privacy`, `/personal-data-consent`, `/cookies`, `/data-subject-request` as `404` and forms without detected checkbox signals on the first 8 URLs. This remains a legal/publication gate, not a silent SEO task.

## 2026-06-05 — `мунн.рф` Daily Supervisor

1. `P0` Canonical migration is still incomplete on all 5 live pages: current live `мунн.рф` responses keep canonical tags on legacy `https://moonn.ru/...`. Fix in Tilda Page settings SEO before any reindex claim.
2. `P0` GSC property for `мунн.рф` is still not verified for the current operator: GUI opened `Oops, you don't have access to this property` for `sc-domain:xn--l1acaw.xn--p1ai`.
3. `P0` Camp page AEO regression persists on the live domain: rendered answer block is `0` on `/podrostkovyy-lager-psihologiya`, while the other 4 pages remain `1`.
4. `P1` New-domain visibility technically improved: the five scoped URLs are now visible in `https://мунн.рф/sitemap.xml` and are not blocked by `robots.txt`, so the remaining migration blockers are canonical/property/access rather than raw reachability.
5. `P1` Source cleanup debt remains unchanged: raw placeholders on camp/gallery, missing image `alt` on all 5 pages, and raw H1 anomalies on camp/consultations/reviews.

## 2026-06-06 — `мунн.рф` Daily Supervisor

1. `P0` New-domain access blocker is now confirmed in both search cabinets: GSC still shows `Oops, you don't have access to this property` for `sc-domain:xn--l1acaw.xn--p1ai`, and Yandex.Webmaster shows `Сайт https://xn--l1acaw.xn--p1ai вам не принадлежит`. Canonical blocker text for this lane: `новая property не подтверждена, traffic migration не доказан`.
2. `P0` Canonical migration improved only partially: camp `/podrostkovyy-lager-psihologiya` now returns new-domain canonical, but the other 4 scoped URLs still expose `canonical_mismatch` to legacy `https://moonn.ru/...`.
3. `P0` Camp page remains the main quality blocker on the live domain: rendered answer block is still `0`, and raw title/description still do not match the 2026-05-21 sprint packet.
4. `OK` Technical live reachability remains good on `мунн.рф`: all 5 scoped URLs return HTTP `200`, are present in sitemap, and are not blocked by `robots.txt`. Evidence: `docs/moonn-five-page-seo-sprint-audit-2026-06-06.json`.
5. `P1` Source cleanup debt remains: gallery raw placeholders, missing image `alt` on all 5 pages, and raw H1 anomalies on camp/consultations/reviews.

## 2026-06-14 — `мунн.рф` Daily Supervisor

1. `P0` Search-console access regressed further in the Alexander profile: direct opens for both `sc-domain:xn--l1acaw.xn--p1ai` and legacy `https://moonn.ru/` now land on `Oops, you don't have access to this property`. Before interpreting traffic, restore the canonical access path or prove the permissions loss.
2. `P0` New-domain blocker wording is unchanged: `новая property не подтверждена, traffic migration не доказан`.
3. `P0` Canonical migration remains incomplete on 4 scoped live pages: gallery, exam prep, consultations and reviews still expose `canonical_mismatch` to legacy `https://moonn.ru/...`.
4. `P0` Camp page remains the main live quality blocker: rendered answer block is still `0`, and raw title/description still do not match the sprint packet.
5. `P0` Yandex.Webmaster host verification is still unproven in the current run: the direct `https://xn--l1acaw.xn--p1ai:443` route opened `404`, so a stable verified-host route still needs to be recovered.
6. `P1` Legacy analytics evidence is available only as a default weekly Metrika slice for `moonn.ru` (`8-14 Jun`: `32` pageviews, `21` visits, `20` visitors); the required custom period `2026-04-29..2026-06-14` and any host split for `мунн.рф` are still missing.
7. `P1` MIIIIPS PR `#11` deploy/merge verification remains blocked: `school.miiiips.ru` root/robots/sitemap are live `200`, but the canonical repo+PR URL is still not recorded in this repo context.
