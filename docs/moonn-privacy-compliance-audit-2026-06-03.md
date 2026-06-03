# Moonn Privacy Compliance Audit — 2026-06-03

## Summary

- Scope URLs checked: `8`.
- Policy endpoints checked: `4`.
- Pages with form signals: `8`.
- Pages with risk flags: `8`.

## Policy Endpoints

- `https://мунн.рф/privacy` — `404`
- `https://мунн.рф/personal-data-consent` — `404`
- `https://мунн.рф/cookies` — `404`
- `https://мунн.рф/data-subject-request` — `404`

## Required Publication Pages

- `/privacy` — policy for personal-data processing.
- `/personal-data-consent` — consent text linked from every form checkbox.
- `/cookies` — cookies and Yandex Metrika/Webvisor notice.
- `/data-subject-request` — request/withdrawal/update/deletion procedure, or equivalent section inside `/privacy`.

## High-Risk Pages

- `https://мунн.рф/` — `forms_without_detected_checkbox`
- `https://мунн.рф/abuse_gaslight` — `forms_without_detected_checkbox`
- `https://мунн.рф/aromatherapy` — `forms_without_detected_checkbox`
- `https://мунн.рф/article_diary_of_emotions` — `forms_without_detected_checkbox`
- `https://мунн.рф/article_femininity` — `forms_without_detected_checkbox`
- `https://мунн.рф/article_gadget_addiction` — `forms_without_detected_checkbox`
- `https://мунн.рф/article_toxic_job` — `forms_without_detected_checkbox`
- `https://мунн.рф/articles/eq-dlya-rukovoditeley` — `forms_without_detected_checkbox`

## Gate

- Do not treat this as legal advice.
- Final publication requires confirmed operator details and legal approval.
- Do not disable Yandex/Google crawling while fixing compliance.
