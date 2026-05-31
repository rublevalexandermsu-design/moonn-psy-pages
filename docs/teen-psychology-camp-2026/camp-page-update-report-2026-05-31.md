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

## Follow-up correction — 2026-05-31

User review found four concrete issues after publication: the header needed the camp category, the first H1 needed `Подростковый лагерь` after the colon, the mobile price badge covered Tatiana's face, and the PDF program needed hourly detail.

Changes applied and published:

- Header brand changed to `Психология без скуки (подростковый лагерь)`.
- H1 changed to `Психология без скуки: Подростковый лагерь уверенности, общения и ИИ`.
- Early payment deadline made visible as `до 15 июня` in the hero button, hero bullets, floating price badge, price card and PDF.
- Mobile CSS changed so `.floating-price` moves below the hero image instead of sitting on the face area.
- Program cards and PDF now include hourly blocks for each day: morning topic, pre-lunch practice, lunch `13:00-14:00`, afternoon practice and final reflection.
- Updated PDF pinned at commit `dab544dc761a653902e8ac793379e5a7ef5d8b8b`.
- Page artifact pinned at commit `650df456da4a02b69a53d05ff14dc9fbdb761db4`.
- Tilda loader pinned and published from commit `a63b13d`.

Follow-up verification:

- Tilda HEAD editor reopened after save: `20260531-camp-followup` present, old `20260531-camp-update` absent, page commit `650df456da4a02b69a53d05ff14dc9fbdb761db4` present.
- Live raw HTML on `https://мунн.рф/podrostkovyy-lager-psihologiya` returned `200`, contains `20260531-camp-followup`, old marker absent, page commit present, old `30000` absent.
- Live mobile render:
  - brand `Психология без скуки (подростковый лагерь)`;
  - H1 `Психология без скуки: Подростковый лагерь уверенности, общения и ИИ`;
  - `до 15 июня` visible;
  - old `15 мая` and `30 000` absent;
  - program times visible;
  - no horizontal overflow;
  - `priceBelowHeroImage=true`.
- Live desktop render: same content checks passed; no horizontal overflow.
- Updated PDF URL returned `200`, `application/pdf`, first bytes `%PDF-`, size `303277`.
- Cart still opens from `Оплатить раннюю стоимость до 15 июня` with SKU `teen-camp-2026`, price/total `40000`, and no `30000`.

## Mobile label correction and downloads — 2026-05-31

User review found that the three white hero chips on mobile should sit in the lower part of the image, not at the top.

Changes applied and published:

- Mobile-only `.hero-label` moved to the bottom area of the hero image.
- Mobile `.floating-price` is now a normal visible block between the image and Tatiana card, so it does not hide behind the speaker card or cover the face.
- Tilda loader marker: `20260531-camp-mobile-labels`.
- Page artifact commit: `4260da7`.
- Tilda loader commit: `5abe9f1`.

Verification:

- Tilda HEAD editor reopened after save: `20260531-camp-mobile-labels` present, old `20260531-camp-followup` absent, page commit `4260da7` present.
- Live raw HTML on `https://мунн.рф/podrostkovyy-lager-psihologiya` returned `200`, contains `20260531-camp-mobile-labels`, old marker absent, old `30000` absent.
- Live mobile rendered check:
  - labels are inside the image;
  - labels are above the price block;
  - price block is visible between image and speaker card;
  - no horizontal overflow.

Files copied to `C:\Users\yanta\Downloads` for Telegram/operator use:

- `moonn-teen-camp-program-2026.pdf`
- `moonn-teen-camp-poster-2026.jpg`
- `moonn-teen-camp-call-brief-2026.docx`

DOCX note: the Word brief was structurally checked with `python-docx` for title, deadline, price, schedule, calendar and contacts. `render_docx.py` could not complete because LibreOffice/soffice was not found on this host (`WinError 2`), so no LibreOffice PNG visual render gate was completed for the DOCX.

## Clickable downloads and payment deep-link — 2026-05-31

User requested that downloaded materials should not be passive files: program PDF, poster and Word brief must contain clickable actions for payment, page opening and questions.

Changes applied and published:

- Program PDF rebuilt with clickable CTA buttons near the top and in the footer:
  - `Оплатить участие` -> `https://мунн.рф/podrostkovyy-lager-psihologiya?pay=teen-camp-2026`;
  - `Страница лагеря` -> `https://мунн.рф/podrostkovyy-lager-psihologiya`;
  - `Вопрос в Telegram` -> `https://t.me/moonn_official`.
- Poster converted from passive JPG download to clickable PDF with the same three CTA links.
- Word call brief rebuilt with clickable payment/page/Telegram/material links.
- Public page materials block now downloads the pinned updated program PDF and poster PDF.
- Added a bounded payment deep-link handler: opening `?pay=teen-camp-2026` opens the existing Tilda cart for SKU `teen-camp-2026`, price `40000`. No payment settings, bank settings, legal text or personal data were changed.
- Files in `C:\Users\yanta\Downloads` were replaced with Russian operator-facing filenames:
  - `Программа подросткового лагеря Татьяны Мунн 2026.pdf`;
  - `Постер подросткового лагеря Татьяны Мунн 2026.pdf`;
  - `Памятка для созвона по подростковому лагерю Татьяны Мунн 2026.docx`.

Published pointers:

- Updated materials commit: `3e0cb73`.
- Updated page artifact commit: `15ffd51`.
- Published Tilda loader commit: `c135e00`.
- Live loader marker: `20260531-camp-clickable-downloads`.

Verification:

- GitHub/jsDelivr returned `200` for:
  - program PDF, `application/pdf`, size `92544`;
  - poster PDF, `application/pdf`, size `602828`;
  - page HTML at commit `15ffd51`;
  - Tilda loader at commit `c135e00`.
- PDF structural check with `pypdf`:
  - program PDF: `1` page, `6` link annotations, expected payment/page/Telegram URLs present;
  - poster PDF: `1` page, `3` link annotations, expected payment/page/Telegram URLs present.
- DOCX structural check:
  - payment/page/Telegram relationships present in `word/_rels/document.xml.rels`;
  - text contains `Оплатить участие`, `40 000`, `Материалы`, clickable material labels.
- Tilda HEAD persistence check after reopen:
  - `20260531-camp-clickable-downloads` present;
  - old `20260531-camp-mobile-labels` absent;
  - page commit `15ffd51` present.
- Tilda publication completed through Rublev/Alexander Chrome and showed the published URL `https://мунн.рф/podrostkovyy-lager-psihologiya`.
- Live raw HTML returned `200`, contains loader marker and page commit.
- Live rendered Playwright check:
  - mounted version `20260531-camp-clickable-downloads`;
  - `#materials` exists;
  - links render as `Скачать программу PDF` and `Скачать постер PDF`;
  - both links point to commit `3e0cb73`;
  - old `30 000` absent and no horizontal overflow.
- Live payment deep-link check:
  - `https://мунн.рф/podrostkovyy-lager-psihologiya?pay=teen-camp-2026` opens visible Tilda cart;
  - product `Психология без скуки — подростковый лагерь` present;
  - price `40000` present;
  - old `30000` absent.

Incident/rule:

- Symptom: setting the visible Tilda HEAD field through UIA or pasting into the editor did not persist after reopen.
- Root cause: the visible Ace/UIA value can diverge from Ace editor state and Tilda server submission.
- Resolution: executed the save script from the real Chrome DevTools console, then reopened the Tilda HEAD editor and verified persisted server value before publishing.
- Follow-up rule: for Tilda HEAD publication, server persistence must be checked after reopen; UI field value alone is not evidence.
