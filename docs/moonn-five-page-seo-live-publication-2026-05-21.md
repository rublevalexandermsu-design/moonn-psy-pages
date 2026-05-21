# Moonn Five-Page SEO/AEO Live Publication — 2026-05-21

## Scope

- Branch: `codex/moonn-seo-audit`
- Tilda project: `8326812`
- Chrome context: authenticated Alexander/Rublev Chrome window.
- URLs:
  - `https://moonn.ru/podrostkovyy-lager-psihologiya`
  - `https://moonn.ru/kartiny-tatiany-munn`
  - `https://moonn.ru/psypodgotovka1`
  - `https://moonn.ru/psiholog-konsultacii-moskva`
  - `https://moonn.ru/otzivi`

## Applied

- SEO title, description and canonical were saved in Tilda page settings for all five pages.
- Page-specific Tilda HEAD was updated through `editheadcode` / `aceeditor_head` for all five pages.
- The five-page AEO/FAQ/schema layer is loaded from:
  - `https://cdn.jsdelivr.net/gh/rublevalexandermsu-design/moonn-psy-pages@49a093e/assets/moonn-five-page-seo-sprint-layer.js`
- Only the five scoped pages were published.
- No prices, payment provider settings, legal text, personal data, fake ratings or full review mirroring were changed.

## Evidence

- SEO settings rollout local log: `output/tilda-five-page-seo-settings-ui-rollout-2026-05-21.json`
  - first pass: five saved page settings, `0` errors;
  - second pass: five saved + published page settings, `0` errors.
- HEAD layer rollout local log: `output/tilda-five-page-head-layer-ui-rollout-2026-05-21.json`
  - five page-specific HEAD saves and publishes, `0` errors.
- Persistent evidence:
  - `docs/moonn-five-page-seo-sprint-audit-2026-05-21.json`
  - `docs/moonn-five-page-seo-sprint-audit-2026-05-21.md`
  - `docs/moonn-five-page-seo-change-ledger-2026-05-21.json`
  - `docs/moonn-five-page-seo-change-ledger-2026-05-21.md`

## Live Verification

- All five URLs return `200`.
- All five URLs are present in sitemap.
- None of the five URLs is blocked by robots.txt.
- Raw live HTML contains `moonn-five-page-seo-sprint-layer.js` and commit `49a093e` on all five URLs.
- Rendered browser audit:
  - H1 count: `1` on all five pages;
  - AEO answer block count: `1` on all five pages;
  - rendered placeholder hits: `0` on all five pages.

## Remaining Source-Level Cleanup

- Raw HTML still has missing image alt attributes on all five pages.
- Raw HTML still reports old H1 structure on camp, consultations and reviews, although rendered H1 is corrected.
- Raw HTML still contains placeholder strings on camp/gallery, although rendered output hides them.

## Next Step

- Submit only the five URLs in `docs/moonn-five-page-reindex-urls-2026-05-21.txt` plus sitemap through Google Search Console/Yandex Webmaster.
- Then collect T+14/T+28 page/query evidence in GSC and Yandex.Metrika before judging SEO impact.
