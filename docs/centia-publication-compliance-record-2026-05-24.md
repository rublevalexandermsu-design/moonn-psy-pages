# Centia Publication Compliance Record

Date: 2026-05-24
Scope: local source/build preparation for Centia studio pages
Decision: public live publication not approved yet

## Checked Sources

- 152-FZ personal data baseline: https://www.consultant.ru/document/cons_doc_LAW_61801/
- Roskomnadzor personal-data consent reminder: https://42.rkn.gov.ru/p32026/p32474/
- 436-FZ child-protection information baseline: https://www.consultant.ru/document/cons_doc_LAW_108808/
- 38-FZ advertising baseline: https://www.consultant.ru/document/cons_doc_LAW_58968/
- Internet advertising identifier requirements: https://www.consultant.ru/document/cons_doc_LAW_436054/040b729435c0f0d37888c98e00ad05cb2e82b540/

## Risk Flags

- The site targets children and teenagers, so public copy must stay neutral, non-alarming and age-appropriate.
- Contact/booking forms can collect personal data. Before live launch, the production route needs privacy policy, consent text, operator identity, purpose of processing and withdrawal contact.
- Paid booking and abonement copy can become advertising/sales material. External advertising campaigns may require ad-labeling/ERID flow depending on placement.
- The studio address is described as a location signal, but exact public address should be confirmed before publication.

## Current Safe State

- No DNS/CNAME or live Tilda publication was changed in this step.
- The local build uses a path deployment model: `/centia/`.
- Visible public pages must not contain internal developer notes, local paths, GPT/AI generation markers or payment placeholders.

## Launch Gate

Before live launch, confirm:

- production domain: preferably `centia.moonn.ru`, or same-domain path on `moonn.ru` if Tilda/domain architecture allows it without conflicts;
- exact operator/legal identity for personal-data policy;
- final studio address and map link;
- contact form backend and consent checkbox behavior;
- whether paid booking links go through Tilda, Timepad, Yandex Business or another provider;
- whether any external ad campaign needs ERID/ad marking.
