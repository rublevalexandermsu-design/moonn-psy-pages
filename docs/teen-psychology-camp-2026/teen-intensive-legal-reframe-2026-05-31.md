# Teen Intensive Legal Reframe - 2026-05-31

## Scope

Public-facing youth program page and downloadable materials for `https://мунн.рф/podrostkovyy-lager-psihologiya`.

## Reason

The previous public framing used camp-like terms and facts: `лагерь`, `смена`, `10:00-18:00`, centralized food, and independent day presence. For minors under 18 this creates a legal/compliance risk if the offer is interpreted as children's recreation/day camp format rather than psychological/developmental classes.

Reference sources checked on 2026-05-31:

- 124-ФЗ / Article 1 mirrors current legal definition of a child as a person under 18: `https://constitution.garant.ru/act/right/179146/chapter/1cafb24d049dcd1e7707a22d98e9858f/`.
- МОСГОРТУР registry page states that day camps with children staying more than four hours and organized food belong in the registry contour: `https://mosgortur.ru/lagerya_moskvy`.

## Draft Decision

Working public name:

`Психология без скуки: подростковый интенсив уверенности, общения и ИИ`

Draft public format:

- psychological and developmental classes for teenagers 14-17;
- 6-10 July 2026;
- Moscow, Tsvetnoy Boulevard;
- 10:00-18:00 daily, per explicit operator confirmation;
- group 10-12 teenagers;
- obedenniy break and pauses are mentioned; exact food conditions are to be confirmed at registration;
- participation conditions are confirmed with the parent/legal representative.

## Changed Draft Artifacts

- `docs/teen-psychology-camp-2026/tilda-page-template-with-placeholders.html`
- `docs/teen-psychology-camp-2026/tilda-page-final.html`
- `docs/teen-psychology-camp-2026/tilda-html-block-final.html`
- `docs/teen-psychology-camp-2026/tilda-head-loader-final.html`
- `docs/teen-psychology-camp-2026/tilda-head-injection-final.html`
- `scripts/build_teen_camp_downloads.py`
- `assets/teen-psychology-camp-2026/teen-psychology-camp-tatyana-moonn-program-2026.pdf`
- `assets/teen-psychology-camp-2026/teen-psychology-camp-tatyana-moonn-poster-2026.pdf`
- `docs/teen-psychology-camp-2026/teen-psychology-camp-call-brief-2026.docx`
- `docs/teen-psychology-camp-2026/asset-manifest.json`

## Verification

- Draft page/package scan found no visible `лагерь`, `смена`, `10:00-14:00`, `один приём пищи`, `родители не присутствуют`, `12-19`, `оздоров`.
- Program PDF: 1 page, 6 clickable annotations, no `лагер`, includes `10:00-18:00`, no old food claim.
- Poster PDF: 1 page, 3 clickable annotations, no `лагер`, no old food claim.
- DOCX structural check: payment/page links present, no `лагер`, includes `10:00-18:00`, no old food claim.
- Local Chrome mobile screenshot: `docs/teen-psychology-camp-2026/teen-intensive-1018-mobile-check.png`.
- DOCX visual render gate was not run because `soffice` is not available on this host.

## Publication Result

Operator approved publication after returning the factual format to `10:00-18:00`. Legal/compliance risk remains recorded because naming alone may not determine classification.

Published through authenticated Tilda/Chrome on 2026-05-31:

1. Tilda HEAD for page `140348786` was saved; Tilda returned `The code has been saved successfully`.
2. Page was published in Tilda; Tilda returned the live URL `https://мунн.рф/podrostkovyy-lager-psihologiya`.
3. Live raw HTML verification:
   - HTTP `200`;
   - contains loader marker `20260531-teen-intensive-1018`;
   - contains page commit `68327c9`;
   - does not contain old marker `20260531-camp-clickable-downloads`;
   - does not contain old commit `15ffd51`;
   - contains `10:00-18:00`;
   - does not contain `10:00-14:00`.
4. Live mobile screenshot:
   - `docs/teen-psychology-camp-2026/teen-intensive-live-mobile-check.png`;
   - first viewport shows `Психология без скуки (подростковый интенсив)` and `10:00-18:00`.

Remaining gates:

1. Decide whether the old URL slug containing `lager` should be kept temporarily for SEO or migrated to a new alias such as `/podrostkovyy-intensiv-psihologiya` with redirect.
2. Rename the Tilda cart product from `подростковый лагерь` to `подростковый интенсив` only after explicit payment/product approval, then verify live cart without submitting payment.

## Downstream Document Packet

The offline/download packet in `C:\Users\yanta\Downloads` was also normalized after publication:

- program PDF: `Программа подросткового интенсива Татьяны Мунн 2026.pdf`;
- poster PDF: `Постер подросткового интенсива Татьяны Мунн 2026.pdf`;
- call brief DOCX: `Памятка для созвона по подростковому интенсиву Татьяны Мунн 2026.docx`;
- contracts DOCX/PDF for `30 000`, `40 000`, and `50 000` rubles under the `подростковый интенсив` name.

Text QA over DOCX/PDF files found no visible `лагер`, `смен`, `досугов`, `отдых`, `оздоров`, or `10:00-14:00`. Contract PDFs were exported from the updated DOCX files through Word COM.

## Follow-up: PDF Link And Poster QA Incident

After user review, the two downloadable public materials required a second correction:

- PDF buttons that pointed to the Cyrillic domain `мунн.рф` opened `ERR_FILE_NOT_FOUND` in the local viewer;
- the poster still had the old visible phrase `лагерь уверенности, общения и ИИ`;
- the first pass confirmed that buttons existed, but did not fully validate their click targets and visible text after the reframe.

Corrected state:

- program PDF and poster PDF now use punycode URL targets: `https://xn--l1acaw.xn--p1ai/podrostkovyy-lager-psihologiya`;
- payment buttons use `https://xn--l1acaw.xn--p1ai/podrostkovyy-lager-psihologiya?pay=teen-camp-2026`;
- poster wording is `подростковый интенсив уверенности, общения и ИИ`;
- poster and program both include real PDF link annotations for page/payment/contact actions;
- live Tilda loader was republished with marker `20260531-teen-intensive-pdf-link-fix`.

Compliance/QA rule added: public materials for this workstream must be checked both as text and as clickable artifacts. PDF annotations must not use raw Cyrillic domains; use ASCII/punycode targets to avoid broken local viewer behavior.
