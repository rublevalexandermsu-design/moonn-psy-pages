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
