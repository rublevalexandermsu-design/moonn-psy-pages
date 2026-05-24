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
