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

## Legal-safe reframe draft

After the user provided the legal-risk note for minors and day-camp style framing, a draft legal-safe reframe was prepared but not published.

Draft public name: `Психология без скуки: подростковый интенсив уверенности, общения и ИИ`.

Draft changes:

- visible page and downloadable materials reframe `лагерь`/`смена` into `интенсив`/`поток`;
- age changed to `14-17`;
- day rhythm changed from `10:00-18:00` to `10:00-14:00`;
- centralized food claim removed;
- parent/legal representative participation wording made neutral;
- PDFs and DOCX rebuilt with clickable payment/page/Telegram links preserved.

Verification:

- page draft scan found no visible `лагерь`, `смена`, `10:00-18:00`, `один приём пищи`, `родители не присутствуют`, `12-19`, `оздоров`;
- local Chrome mobile screenshot generated at `docs/teen-psychology-camp-2026/teen-intensive-legal-draft-mobile-check.png`; first viewport fits after shortening the top pill and AI card title;
- PDF/DOCX structural checks passed for old camp wording and old time/food claims;
- DOCX visual render was not run because `soffice` is not installed on this host.

Publication gate:

- Do not publish this draft until the operator confirms the real business format accepts `10:00-14:00`.
- Decide whether to keep the existing SEO URL temporarily or migrate to `/podrostkovyy-intensiv-psihologiya` with redirect.
- Rename the Tilda cart product from `подростковый лагерь` to `подростковый интенсив` only after approval, then verify live cart without submitting payment.

## Operator correction: keep 10:00-18:00

The user explicitly rejected the `10:00-14:00` change and confirmed the factual format should remain `10:00-18:00`. The draft was updated accordingly while keeping the public reframe as `подростковый интенсив`.

Updated draft:

- public naming remains `Психология без скуки: подростковый интенсив уверенности, общения и ИИ`;
- age remains `14-17`;
- day rhythm restored to `10:00-18:00`;
- visible `лагерь`/`смена` wording was not restored;
- food wording now says there is an obedenniy break and details are clarified at registration, without the old `один приём пищи` claim.

Verification:

- program PDF: 1 page, 6 clickable annotations, includes `10:00-18:00`, no `лагер`, no `10:00-14:00`, no old one-meal claim;
- poster PDF: 1 page, 3 clickable annotations, no `лагер`, no old one-meal claim;
- DOCX: payment link present, includes `10:00-18:00`, no `лагер`, no `10:00-14:00`, no old one-meal claim;
- local mobile screenshot: `docs/teen-psychology-camp-2026/teen-intensive-1018-mobile-check.png`.

Publication note:

- User approved publication with `10:00-18:00`; legal/compliance risk remains recorded because naming alone may not determine classification.

## Final publication: teen intensive 10:00-18:00 reframe

- Tilda page-specific HEAD for project `8326812`, page `140348786` was saved through authenticated Chrome; Tilda returned `The code has been saved successfully`.
- Tilda page was published; Tilda returned the public URL `https://мунн.рф/podrostkovyy-lager-psihologiya`.
- Live raw HTML check:
  - HTTP `200`;
  - contains `20260531-teen-intensive-1018`;
  - contains `68327c9`;
  - does not contain `20260531-camp-clickable-downloads`;
  - does not contain `15ffd51`;
  - contains `10:00-18:00`;
  - does not contain `10:00-14:00`.
- Live mobile screenshot saved: `docs/teen-psychology-camp-2026/teen-intensive-live-mobile-check.png`.
- Visual check from the screenshot confirms the first viewport uses the reframe `Психология без скуки (подростковый интенсив)` and shows `6 - 10 июля | 10:00 - 18:00`.

Residual risks / next gates:

- This is a public wording/content mitigation, not a legal conclusion that the format is outside the registry requirements.
- Existing URL slug still contains `lager`; keep for SEO until an alias/redirect migration is explicitly approved.
- Tilda cart product naming may still need a separate payment/product gate before renaming; payment settings were not changed in this step.

## Download/offline materials reframe

After the user noted that the downstream document packet was not fully closed, the local `Downloads` package was rebuilt/normalized.

Current user-facing files in `C:\Users\yanta\Downloads`:

- `Программа подросткового интенсива Татьяны Мунн 2026.pdf`
- `Постер подросткового интенсива Татьяны Мунн 2026.pdf`
- `Памятка для созвона по подростковому интенсиву Татьяны Мунн 2026.docx`
- `Договор оказания услуг подростковый интенсив Татьяны Мунн 2026 - 30000 рублей.docx`
- `Договор оказания услуг подростковый интенсив Татьяны Мунн 2026 - 30000 рублей.pdf`
- `Договор оказания услуг подростковый интенсив Татьяны Мунн 2026 - 40000 рублей.docx`
- `Договор оказания услуг подростковый интенсив Татьяны Мунн 2026 - 40000 рублей.pdf`
- `Договор оказания услуг подростковый интенсив Татьяны Мунн 2026 - 50000 рублей.docx`
- `Договор оказания услуг подростковый интенсив Татьяны Мунн 2026 - 50000 рублей.pdf`

Contract changes:

- visible file names changed from `подростковый лагерь` to `подростковый интенсив`;
- contract subtitle changed to `подростковый психологический интенсив`;
- service wording changed from `досугово-развивающая` to `тренингово-развивающая`;
- `смена/смены` changed to `поток/периоды проведения`;
- 2026 periods aligned to the current page calendar: `6-10 июля`, `24-28 августа`, `19-20 и 26-27 сентября`, `26-30 октября`, `2-6 ноября`.

Verification:

- DOCX/PDF text extraction over the nine current `Downloads` files found no `лагер`, `смен`, `досугов`, `отдых`, `оздоров`, or `10:00-14:00`.
- Word COM export produced the three contract PDFs from the updated DOCX files.
- Full DOCX visual render through the Documents skill renderer was not available because `soffice` is not installed on this host; Word PDF export and text extraction were used as the fallback QA gate.

## PDF link incident and fixed publication

Trigger: the user opened the updated PDF files from `C:\Users\yanta\Downloads` and found that the bottom buttons `Оплатить участие` and `Страница интенсива` opened a local browser error `ERR_FILE_NOT_FOUND` instead of the intensive page/payment route. The poster also still contained the old visible phrase `лагерь уверенности, общения и ИИ`.

Root cause:

- the PDF annotations used the Cyrillic domain `https://мунн.рф/...`; in the local PDF/browser viewer this broke into an invalid local file route;
- the previous QA checked that annotations existed, but did not inspect/click the actual URI targets in the viewer;
- the poster PDF still reused an old image layer, so the visible headline was not fully revalidated after the legal reframe.

Fix:

- rebuilt the program and poster PDFs with ASCII/punycode URLs: `https://xn--l1acaw.xn--p1ai/podrostkovyy-lager-psihologiya`;
- added the payment route `?pay=teen-camp-2026` to the `Оплатить участие` PDF buttons;
- rebuilt the poster as a native PDF layout, not an old poster image, and removed visible `лагерь` wording;
- added real visible PDF buttons for `Оплатить участие`, `Страница интенсива`, `Telegram`, and `WhatsApp`;
- copied the fixed files back to `C:\Users\yanta\Downloads`;
- updated site assets to commit `64cf311`, page HTML to `0a25061`, and Tilda HEAD loader to the `20260531-teen-intensive-pdf-link-fix` marker.

Verification after fix:

- program PDF: 1 page, 6 link annotations; all page/payment links use `xn--l1acaw.xn--p1ai`, not `мунн.рф`;
- poster PDF: 1 page, 6 link annotations; all page/payment links use `xn--l1acaw.xn--p1ai`, not `мунн.рф`;
- both PDFs contain `10:00-18:00`, contain `интенсив`, and do not contain `лагер`, `смен`, `досугов`, `отдых`, `оздоров`, or `10:00-14:00`;
- PDF visual QA images saved in `docs/teen-psychology-camp-2026/pdf-qa/`;
- CDN checks returned `200` for the fixed program PDF, poster PDF, and poster JPG at commit `64cf311`;
- Tilda page-specific HEAD for project `8326812`, page `140348786` was saved in the authorized Rublev Chrome session and the page was published;
- live raw HTML for `https://мунн.рф/podrostkovyy-lager-psihologiya` returns `200`, contains `20260531-teen-intensive-pdf-link-fix`, `0a25061`, and `64cf311`, and does not contain old marker `20260531-camp-clickable-downloads`, old asset commit `ad26ae1`, or old phrase `лагерь уверенности`.

New QA rule:

- for public PDF/Word materials, existence of buttons is not enough; every generated file must pass link-target QA: extract annotations, verify ASCII/punycode URLs, verify expected payment/page/Telegram/WhatsApp targets, render visually, and scan for obsolete legal/public wording before reporting completion.

## 2026-06-02 01:25 MSK — Custdev Speech/Exam Offer Published and Verified

Scope: public teen intensive page and downloadable materials after custdev feedback.

User request:

- Add early-page emphasis on public speaking / confident speech, easier communication, relaxation after exams, and expert blocks.
- Keep existing useful content; integrate new meanings visually and without deleting the current offer.
- Update the downloadable poster, program PDF, and call brief DOCX.
- Verify that file buttons work and that payment opens correctly.
- Publish through the authorized Rublev/Alexander Chrome Tilda session.

Implemented content changes:

- Hero and first blocks now position the offer as `Психология без скуки: подростковый интенсив речи, уверенности, общения и ИИ`.
- Added a first-screen card: `Ораторское мастерство без сцены через силу`.
- Added a dedicated block: `Ораторское мастерство, лёгкость в общении и разгрузка после экзаменов`.
- Added concrete custdev-driven benefits: easier first contact, expressing thoughts, speaking in a small group, relaxation after ЕГЭ/ОГЭ, and expert blocks.
- Price rationale now explains the 50 000 ₽ standard cost through expanded format, personal guidance, materials, small group and possible invited experts.
- Program wording updated: speech/self-presentation is part of the communication day; materials mention exams and expert blocks.

Published Tilda state:

- Tilda page-specific HEAD for project `8326812`, page `140348786` was updated in the Rublev/Alexander Chrome profile and the page was published.
- Live URL checked: `https://мунн.рф/podrostkovyy-lager-psihologiya`.
- Raw live HTML check returned HTTP `200` and contains:
  - `20260601-teen-intensive-custdev-speech`;
  - page commit `9159906`;
  - asset commit `52d2a5e`;
  - speech/oratory wording;
  - post-exam wording.
- Raw live HTML no longer contains the old marker `20260531-teen-intensive-pdf-link-fix`, old asset commit `64cf311`, visible phrase `лагерь уверенности`, or `10:00-14:00`.
- Browser render check confirmed the live page shows the updated hero, `Речь` navigation item, `Ораторское мастерство без сцены через силу`, the post-exam bullets, and the expert-block card.
- Safe checkout check: opening `?pay=teen-camp-2026` opens the Tilda cart with item `Психология без скуки — подростковый интенсив`, amount `40 000 ₽`, and T-Bank payment methods. No customer data was entered and no payment submit was clicked.

Download files rebuilt and placed in `C:\Users\yanta\Downloads`:

- `Программа подросткового интенсива Татьяны Мунн 2026.pdf`
- `Постер подросткового интенсива Татьяны Мунн 2026.pdf`
- `Памятка для созвона по подростковому интенсиву Татьяны Мунн 2026.docx`

Download/file verification:

- Program PDF: 9 link annotations; contains speech/exams/experts; no stale `лагер`, `смен`, `досугов`, `оздоров`, or `10:00-14:00`.
- Poster PDF: 6 link annotations; contains speech/exams/experts; no stale `лагер`, `смен`, `досугов`, `оздоров`, or `10:00-14:00`.
- DOCX call brief: contains speech/exams/experts and active links to the page, payment route, Telegram, and materials anchor.
- PDF page/payment URLs use ASCII punycode `https://xn--l1acaw.xn--p1ai/...`, not Cyrillic-domain annotations, to avoid the earlier local `ERR_FILE_NOT_FOUND` failure.

Incident / QA rule:

- First Tilda HEAD edit appeared visually pasted and the page was published, but raw live HTML still served the old loader. The live marker check caught this before final handoff.
- Root cause: relying on the visible Tilda editor state is insufficient; the server-side HEAD value may not persist from a normal paste until the editor emits the right input/change state and save completes.
- Fix used in this run: programmatic bookmarklet setter updated textarea/Ace state, then Tilda save and page publish were repeated.
- New gate: for future Tilda HEAD changes, completion requires all three checks: reopened/saved editor state or no unsaved warning, Tilda publish confirmation, and raw live HTML marker check with the expected content/asset commits.

Residual notes:

- `moonn.ru` DNS remains a separate domain-recovery issue; this publication was verified on the active fallback domain `мунн.рф` / `xn--l1acaw.xn--p1ai`.
- Payment was verified only up to cart/form opening; actual payment submission remains a money gate and was not executed.
- Completion email was sent to `rublevalexandermsu@gmail.com` with a ZIP of the three updated files; Gmail message id: `19e855570a578e4b`.

## 2026-06-02 20:36 MSK — Soft-Lead CRO Layer and Flicker Hotfix

Scope: public teen intensive page, page-specific Tilda HEAD loader.

Implemented CRO changes:

- Added first-screen soft CTA: `Бесплатный 15-минутный созвон до оплаты`.
- Added FOMO marker: `Осталось 4 места из 12`.
- Replaced the primary hero and final CTA from immediate purchase language to `Записаться на бесплатный созвон`; payment remains available as a secondary action.
- Added parent-risk FAQ items for phones/gadgets and safety/atmosphere.
- Added expert-positioning support: `Юнгианский подход и практическая подача`.
- Clarified price rationale: 50 000 ₽ standard cost is explained by personal guidance, small group, materials, speech practice, AI block and possible invited experts.

Published state:

- Page content commit: `78c2c6a`.
- Initial loader commit: `86eac43`.
- Flicker hotfix loader commit: `64b013b`.
- Tilda project/page: `8326812` / `140348786`.
- Live URL: `https://мунн.рф/podrostkovyy-lager-psihologiya`.

Incident:

- Symptom reported by user: first screen was blinking; a form/layer looked like it was flashing underneath the hero.
- Root cause: the Tilda HEAD loader mounted the injected page multiple times: initial load, delayed load at `1200ms`, and delayed load at `3500ms`. This was originally a defensive retry, but after the new CRO blocks it caused visible remount/flicker and possible overlap with the underlying Tilda form/cart layer.
- Fix: added `teen-camp-loader-guard`, `didMount`, `mountedVersion`, and removed the `3500ms` remount. The remaining `1200ms` retry exits if the first mount already succeeded.

Verification after hotfix:

- Raw live HTML returns HTTP `200`.
- Raw live HTML contains marker `20260602-teen-intensive-soft-lead-fomo`.
- Raw live HTML contains `teen-camp-loader-guard` and `didMount`.
- Raw live HTML contains exactly one `setTimeout(loadAndMount...)` occurrence.
- Raw live HTML does not contain old commit `@9159906/` or old retry `setTimeout(loadAndMount, 3500)`.
- Browser smoke-test sampled the page at `0.8s`, `1.5s`, `2.5s`, `4.2s`, and `6.2s`; all samples showed the same mounted version, opacity `1`, the correct H1, soft CTA and `4 места из 12`.

New QA rule:

- For Tilda pages driven by a HEAD loader, raw marker checks are necessary but not sufficient. Completion also requires a timed render stability check across the first 5-6 seconds to catch delayed remount/flicker caused by loader retries.

## 2026-06-02 20:52 MSK — CTA and Form Audit

Scope: public teen intensive page after the flicker hotfix.

Checked live page:

- URL: `https://мунн.рф/podrostkovyy-lager-psihologiya`.
- Mounted version: `20260602-teen-intensive-soft-lead-fomo`.
- Visible anchors/buttons discovered: navigation anchors, Telegram CTAs, WhatsApp CTAs, Telegram share, five payment CTAs, PDF downloads, privacy links.

External/link checks:

- `https://t.me/moonn_official` returned HTTP `200`.
- `https://t.me/share/url?...` returned HTTP `200`.
- `https://wa.me/79777770303` returned HTTP `200`.
- Program PDF returned HTTP `200`, `application/pdf`.
- Poster PDF returned HTTP `200`, `application/pdf`.
- `/politic` returned HTTP `200`.

Payment CTA checks:

- `Оплатить раннюю стоимость до 15 июня`: opens Tilda cart, shows `40 000`, order text and visible `Перейти к оплате`.
- `Оплатить место`: opens Tilda cart, shows `40 000`, order text and visible `Перейти к оплате`.
- `Оплатить`: opens Tilda cart, shows `40 000`, order text and visible `Перейти к оплате`.
- `Оплатить участие`: opens Tilda cart, shows `40 000`, order text and visible `Перейти к оплате`.
- `Оплатить сейчас`: opens Tilda cart, shows `40 000`, order text and visible `Перейти к оплате`.

Form check:

- The only real form detected on the page is Tilda `Cart`.
- Visible fields inside the opened cart: `Name`, `Email`, phone, payment method radios, personal-data consent checkbox.
- Test fill check passed with explicit test data: name/email/phone fields fill correctly, consent checkbox checks, submit button remains visible.
- No form was submitted: `Перейти к оплате` is a money/payment flow, so sending it is a payment gate.

Operational finding:

- The public copy now says `Записаться на бесплатный созвон`, but technically that CTA goes to Telegram/WhatsApp, not to a separate Tilda CRM lead form. This is acceptable for messaging, but weak for analytics because Tilda cannot count a clean `free_call_request` goal unless a separate form or click-goal is configured.

Recommended next bounded step:

- Add a dedicated non-payment Tilda form or click-goals for `free_call_telegram`, `free_call_whatsapp`, `payment_cart_open`, and `pdf_download`, then verify that the заявки reach Telegram/Tilda CRM. This should be a separate gated change because it affects forms, personal data and analytics routing.
