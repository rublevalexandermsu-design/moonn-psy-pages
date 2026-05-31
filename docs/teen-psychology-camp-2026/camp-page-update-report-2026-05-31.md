# Camp page update report — 2026-05-31

Workstream: Moonn Tilda camp page content/pricing update.
Branch: `codex/moonn-camp-page-update`.
Page: `https://moonn.ru/podrostkovyy-lager-psihologiya`.
Tilda page id: `140348786`.

## Scope

Updated the teen camp landing page package, poster, PDF and homepage banner copy for the new offer and stronger positioning.

## Content changes

- Renamed the public offer to `Психология без скуки: уверенность, общение и ИИ`.
- Replaced old pricing with:
  - early payment: `40 000 ₽`;
  - standard price: `50 000 ₽` shown as crossed-out where appropriate.
- Removed active use of the expired `15 мая` deadline from the public page.
- Changed group size from `3-5` to `10-12`.
- Replaced the black-and-white author block image with the color camp hero image.
- Added an early AI teaser and kept the full neural-network practice block.
- Added the `Первые шаги молодого психолога` block and connected it to the day-by-day program.
- Added food block: one meal per program day, 13:00-14:00 lunch window, breaks and food restrictions note.
- Added shift calendar for July, late August, September, October and November/profession orientation.
- Added loyalty block: `5 000 ₽` bonus after referred participant payment/start, with organizer confirmation.
- Added multiple pay/reserve CTAs; local cart markers show `40000`.

## Updated artifacts

- `docs/teen-psychology-camp-2026/tilda-page-final.html`
- `docs/teen-psychology-camp-2026/tilda-html-block-final.html`
- `docs/teen-psychology-camp-2026/tilda-head-loader-final.html`
- `docs/teen-psychology-camp-2026/tilda-head-injection-final.html`
- `docs/teen-psychology-camp-2026/tilda-page-template-with-placeholders.html`
- `docs/teen-psychology-camp-2026/homepage-teen-camp-head-snippet.html`
- `docs/teen-psychology-camp-2026/homepage-head-combined-final.html`
- `assets/teen-psychology-camp-2026/moonn-home-teen-camp-banner.js`
- `assets/teen-psychology-camp-2026/teen-psychology-camp-tatyana-moonn-poster-2026.jpg`
- `assets/teen-psychology-camp-2026/teen-psychology-camp-tatyana-moonn-program-2026.pdf`
- `docs/teen-psychology-camp-2026/camp-page-update-checklist-2026-05-31.md`

## Local verification

- `rg` delivery scan passed for working publication files: no old `30 000`, `30000`, `3-5`, `3 - 5`, `15 мая`.
- Rendered desktop browser check passed:
  - no old price;
  - no old group size;
  - no expired deadline;
  - no runtime refs to the black-and-white `psychologist-msu` author image;
  - food, calendar, loyalty, AI teaser and profession track present;
  - `6` order links;
  - cart price marker `40000`.
- Rendered mobile browser check `390x844` passed:
  - no horizontal overflow;
  - no old price;
  - `6` order links.

## Open gates

- Push to GitHub and pin CDN URLs to the new commit hash.
- Publish `tilda-head-loader-final.html` through Rublev Chrome/Tilda.
- Verify live rendered page and cart after Tilda publication.
- Do not change T-Bank/bank settings or legal/payment terms beyond the explicit public offer update.
