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

1. `P0` Tilda publication gate: open authenticated Chrome/Tilda and apply `docs/moonn-five-page-seo-packets-2026-05-21.json` through `scripts/tilda_page_seo_settings_ui_rollout.py --mode pages --limit 5`; publish only the five scoped pages after checking backups.
2. `P0` HEAD/AEO gate: after commit hash is known, add `docs/moonn-five-page-seo-sprint-head-snippet-2026-05-21.html` to the approved Tilda head layer so `assets/moonn-five-page-seo-sprint-layer.js` can render answer blocks, FAQ/schema and click goals.
3. `P0` Technical T+3 check: rerun `scripts/moonn_five_page_seo_sprint_audit.py --packet docs/moonn-five-page-seo-packets-2026-05-21.json --rendered` and require 200, sitemap true, robots false, one rendered H1, updated title/description, schema present and no visible placeholders.
4. `P0` Reindex scope: submit only `docs/moonn-five-page-reindex-urls-2026-05-21.txt` and sitemap in Google Search Console/Yandex Webmaster after live publication; do not resubmit all 83 URLs.
5. `P1` Measurement: collect T+14/T+28 GSC and Yandex.Metrika page/query evidence for the five URLs and write results into `docs/moonn-five-page-seo-change-ledger-2026-05-21.json`.
6. `P1` Content cluster: prepare the next 20-40 support pages/FAQ/cases around parents of teenagers, exam anxiety, communication and self-esteem only after the five-page technical layer is green.
7. `P2` Image alt source cleanup: replace remaining missing alt attributes on the five pages at source/Tilda level; current audit still sees raw missing alt on all five.
