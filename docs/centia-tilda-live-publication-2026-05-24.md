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

Closed in the follow-up pass on 2026-05-24. The generated Centia Tilda manifest contains 12 page artifacts, and all 12 aliases now have Tilda page ids, native T123 records and scoped publish timestamps.

## Follow-Up Publication - 2026-05-24

### Typography Fix

- Reduced oversized generated display typography in `scripts/build_centia_site.py`.
- Rebuilt the local site and Tilda HTML blocks.
- Republished the homepage `fnt` with updated T123 content and updated Tilda page settings.
- Live browser typography smoke for `https://moonn.ru/fnt` at 1440x900:
  - hero H1 `Центия`: `172.8px`;
  - hero lead: `29.52px`;
  - first section title: `102.24px`;
  - no horizontal overflow.

### Multi-Page Tilda Publication

| Alias | Tilda page id | T123 record id | Published timestamp |
|---|---:|---:|---:|
| `fnt` | `143840376` | `2304908271` | `1779623152` |
| `fnt-kontakty` | `143856396` | `2305025801` | `1779622618` |
| `fnt-deti-7-10` | `143856886` | `2305031561` | `1779622649` |
| `fnt-o-tatyane` | `143856916` | `2305031891` | `1779622712` |
| `fnt-bron` | `143856966` | `2305032101` | `1779622743` |
| `fnt-podrostki-11-13` | `143857036` | `2305032481` | `1779622775` |
| `fnt-podrostki-14-16` | `143857056` | `2305032671` | `1779622806` |
| `fnt-podrostki-15-17` | `143857106` | `2305033041` | `1779622838` |
| `fnt-prostranstvo` | `143857136` | `2305033261` | `1779622869` |
| `fnt-raspisanie` | `143857186` | `2305033631` | `1779622901` |
| `fnt-roditelyam` | `143857196` | `2305033841` | `1779622932` |
| `fnt-vzroslym` | `143857236` | `2305034121` | `1779622963` |

### Live Verification

- Live URL check for every alias in `docs/centia-tilda/tilda-pages-manifest.json` returned HTTP `200`.
- Each live page contains a Tilda record, the expected page title text and Centia content.
- Playwright rendered `https://moonn.ru/fnt` and `https://moonn.ru/fnt-podrostki-14-16`.
- Homepage internal link check found 11 `/fnt-*` links and `0` broken links.
- The former broken route `https://moonn.ru/fnt-podrostki-14-16` now returns HTTP `200` and has H1 `Самооценка, тревога, общение`.

### QA Artifacts

- `output/centia-local-qa-2026-05-24-home-desktop.png`
- `output/centia-local-qa-2026-05-24-home-mobile.png`
- `output/centia-tilda-page-create-settings-2026-05-24.json`
- `output/centia-tilda-block-publish-2026-05-24.json`
- `output/centia-tilda-published-pages-2026-05-24.json`
- `output/centia-live-url-check-2026-05-24.json`
- `output/centia-live-qa-2026-05-24-home-desktop-typography.png`
- `output/centia-live-qa-2026-05-24-teen-page.png`

### Incident

- Symptom: after the first publication pass, clicking internal group links such as the main teen group opened a Tilda `404`.
- Root cause: the previous completion criterion stopped at the published homepage `/fnt`; it did not require a Tilda page id and publish event for every alias in the 12-page manifest.
- Fix: created the missing Tilda pages, saved correct aliases/title/SEO settings, added native T123 HTML blocks, published each page and checked every live URL.
- Follow-up rule: a Centia multi-page publication is not complete until manifest aliases, Tilda page ids, T123 record ids, publish timestamps and live URL checks all match.

## Remaining Gap

No remaining `404` gap for the 12-page Centia manifest after the follow-up pass. Future work is content/product refinement, not route completion.

## Follow-Up Rule

For Centia/Tilda work, do not call the site fully launched until every alias in `docs/centia-tilda/tilda-pages-manifest.json` has a Tilda page id, a native T123 block, saved page settings, a scoped publish event, and a live HTTP/browser check.
