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
