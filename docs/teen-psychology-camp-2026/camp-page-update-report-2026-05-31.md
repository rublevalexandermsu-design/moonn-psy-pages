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

- GitHub push completed for branch `codex/moonn-camp-page-update`.
- CDN URLs pinned to current commits:
  - page artifact: `1aab5c887ee048e03c37fc6103dd6b3ed080fc7c`;
  - Tilda loader: `0ad7940`;
  - poster image: `978847c0d1283d5347ce0e1c2c38d7ee219b7f8c`.
- `tilda-head-loader-final.html` was published through Rublev Chrome/Tilda for page `140348786`.
- Live rendered page and cart were verified after Tilda publication.
- No T-Bank/bank settings, legal texts, personal data, registrar settings or unrelated domains were changed.

## Live publication verification

- Tilda HEAD editor was reopened after saving. Server-side editor value contained `20260531-camp-update`, `40000`, commit `1aab5c887ee`, and did not contain old `20260523-offer-visual-ai` or `30000`.
- Live raw HTML on `https://мунн.рф/podrostkovyy-lager-psihologiya` returned `200`, contained `20260531-camp-update`, `40000`, commit `1aab5c887ee`, and did not contain old `30000`.
- Live rendered check on `https://мунн.рф/podrostkovyy-lager-psihologiya`:
  - H1: `Психология без скуки: уверенность, общение и ИИ`;
  - mounted version: `20260531-camp-update`;
  - old `30 000` absent;
  - `40 000`, `50 000`, group `10-12`, food, calendar, loyalty and AI blocks present;
  - no horizontal overflow;
  - author image uses the color poster asset from commit `978847c0d1283d5347ce0e1c2c38d7ee219b7f8c`.
- Live cart check passed without payment submission:
  - native Tilda cart record and `tcart__addProduct` are present;
  - click on `Оплатить раннюю стоимость` opens the Tilda cart;
  - product: `Психология без скуки — подростковый лагерь`;
  - SKU: `teen-camp-2026`;
  - price/total: `40000`;
  - `30000` absent.

## Incident and rule

- Symptom: first GUI paste into the Tilda HEAD editor visually showed the new loader, but after publishing the live page still had the old loader, and reopening `editheadcode` showed the old server value.
- Root cause: Tilda's Ace editor can show a changed accessibility/UI value without reliably updating the internal Ace model submitted to the server.
- Resolution: used authenticated Rublev Chrome with address-bar `javascript:` execution to set `aceeditor_head`, dispatch editor events, save through Tilda, reopen the editor and verify persisted server value before publishing.
- Follow-up rule: for Tilda HEAD/Ace edits, do not treat visible field content as proof. Required gate is: save through Ace model, reopen editor, verify marker in server value, publish scoped page, verify live raw HTML, verify rendered browser and cart if payment CTAs are touched.

## Remaining notes

- `moonn.ru` is still not resolvable from this host; `мунн.рф` is the verified continuity domain for this publication.
- The live cart still displays native Tilda default labels `Your Name`, `Your Email`, `Your Phone`. This is not part of the requested price/content update; it should be handled as a separate form/localization task if needed.
