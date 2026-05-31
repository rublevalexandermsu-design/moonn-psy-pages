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

## Publication Gate

Operator approved publication after returning the factual format to `10:00-18:00`. Legal/compliance risk remains recorded because naming alone may not determine classification.

Before publishing:

1. Confirm final public name.
2. Confirm whether the old URL slug containing `lager` should be kept temporarily for SEO or migrated to a new alias such as `/podrostkovyy-intensiv-psihologiya` with redirect.
3. Confirm payment product text in Tilda cart should be renamed from `подростковый лагерь` to `подростковый интенсив`.
4. Run Tilda publish via authenticated Chrome and verify live HTML/rendered page/cart/downloads.
