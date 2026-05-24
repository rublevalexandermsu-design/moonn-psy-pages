# Centia Tilda Live Publication - 2026-05-24

## Scope

- Project: Centia studio under the Moonn ecosystem.
- Tilda project: `8326812` (`Moonn.ru` / `moonn.ru`).
- Workstream branch: `codex/studia`.
- Published page: `143840376`.
- Published alias: `fnt`.
- Live URL: `https://moonn.ru/fnt`.

## What Was Applied

- Removed the accidental SoundCloud/T153 record that had been created by using the wrong template id.
- Added the correct native Tilda HTML block:
  - Tilda template id: `131`.
  - Tilda block code: `T123`.
  - Record id: `2304908271`.
- Saved the generated Centia homepage HTML block from `docs/centia-tilda/index-tilda-html-block.html`.
- Updated page settings:
  - Page title: `Центия — психологические группы у Марьиной Рощи`.
  - Page alias: `fnt`.
  - SEO title: `Центия — психологические группы для детей и взрослых в Марьиной Роще`.
  - Canonical URL: `https://moonn.ru/fnt`.

## Verification

- Tilda published URL returned: `https://moonn.ru/fnt`.
- Live HTTP check:
  - HTTP status: `200`.
  - HTML contains `Центия`.
  - HTML contains the T123 record id `rec2304908271`.
  - HTML does not contain `AVICII`.
  - HTML does not contain `SoundCloud`.
  - `<title>` is `Центия — психологические группы для детей и взрослых в Марьиной Роще`.
- Tilda API export after publish:
  - page id `143840376`;
  - alias `fnt`;
  - published timestamp `1779620215`;
  - content contains `Центия`;
  - content does not contain `AVICII` or `SoundCloud`.
- Browser visual check in Google Chrome profile `Alexander`:
  - live hero rendered as the Centia page, not Tilda code;
  - semantic group image cards rendered on the live page;
  - navigation/header rendered on `moonn.ru/fnt`.
- Playwright live smoke output:
  - `output/centia-live-qa-2026-05-24/summary.json`;
  - `output/centia-live-qa-2026-05-24/desktop.png`;
  - `output/centia-live-qa-2026-05-24/mobile.png`.

## Remaining Gap

The generated Centia Tilda manifest contains 12 page artifacts, but only the homepage alias `fnt` is live in Tilda right now. The following aliases returned HTTP `404` after the homepage publication:

- `fnt-kontakty`
- `fnt-deti-7-10`
- `fnt-o-tatyane`
- `fnt-bron`
- `fnt-podrostki-11-13`
- `fnt-podrostki-14-16`
- `fnt-podrostki-15-17`
- `fnt-prostranstvo`
- `fnt-raspisanie`
- `fnt-roditelyam`
- `fnt-vzroslym`

## Follow-Up Rule

For Centia/Tilda work, do not call the site fully launched until every alias in `docs/centia-tilda/tilda-pages-manifest.json` has a Tilda page id, a native T123 block, saved page settings, a scoped publish event, and a live HTTP/browser check.
