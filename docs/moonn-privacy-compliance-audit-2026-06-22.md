# Moonn Privacy Compliance Audit — 2026-06-22

## Summary

- Scope URLs checked: `83`.
- Policy endpoints checked: `4`.
- Pages with form signals: `83`.
- Pages with risk flags: `78`.
- Live base URL: `https://мунн.рф/` (`https://xn--l1acaw.xn--p1ai/` for technical fetches).
- Preflight: `https://xn--l1acaw.xn--p1ai/robots.txt` returned `200`; no DNS-like failure was detected.
- Yandex Metrika signals were detected on `83/83` checked pages; Google Analytics signals were detected on `0/83`.

## Supervisor Finding

- `P0` Privacy endpoints are still not published on the live domain: `/privacy`, `/personal-data-consent`, `/cookies`, `/data-subject-request` return `404`.
- `P0` Form compliance is still incomplete: `78/83` checked pages expose form signals without a detected required checkbox.
- `P1` The current publication packet still contains legacy `moonn.ru` text and the unresolved operator address placeholder; do not publish it without legal/operator review.
- `P1` Because Yandex Metrika is present on all checked pages, the cookie/analytics notice remains a live-domain compliance blocker.
- `OK` No Google Analytics/gtag signal was detected by this audit.

## Policy Endpoints

- `https://xn--l1acaw.xn--p1ai/privacy` — `404`
- `https://xn--l1acaw.xn--p1ai/personal-data-consent` — `404`
- `https://xn--l1acaw.xn--p1ai/cookies` — `404`
- `https://xn--l1acaw.xn--p1ai/data-subject-request` — `404`

## Required Publication Pages

- `/privacy` — policy for personal-data processing.
- `/personal-data-consent` — consent text linked from every form checkbox.
- `/cookies` — cookies and Yandex Metrika/Webvisor notice.
- `/data-subject-request` — request/withdrawal/update/deletion procedure, or equivalent section inside `/privacy`.

## High-Risk Pages

- `https://xn--l1acaw.xn--p1ai/` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/abuse_gaslight` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/aromatherapy` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/article_diary_of_emotions` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/article_femininity` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/article_gadget_addiction` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/article_toxic_job` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/articles/eq-dlya-rukovoditeley` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/baza-znaniy-emocionalnyy-intellekt-psihologiya` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/eintellect` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/emotional-intelligence/` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/emotional-intelligence/articles` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/emotional-intelligence/articles/benefits-of-ei` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/emotional-intelligence/articles/emotional-intelligence-skills` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/emotional-intelligence/articles/what-is-emotional-intelligence` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/emotional-intelligence/articles/why-ei-matters` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/emotional-intelligence/diagnostoka-ei` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/emotional-intelligence/ei-leader-12` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/emotional-intelligence/knowledge-base` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/emotional-intelligence/knowledge-base/active-listening` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/emotional-intelligence/knowledge-base/burnout` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/emotional-intelligence/knowledge-base/emotional-contagion` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/emotional-intelligence/knowledge-base/emotional-intelligence` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/emotional-intelligence/knowledge-base/emotional-literacy` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/emotional-intelligence/knowledge-base/emotional-maturity` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/emotional-intelligence/knowledge-base/empathy` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/emotional-intelligence/knowledge-base/intrinsic-motivation` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/emotional-intelligence/knowledge-base/male-loneliness-russia` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/emotional-intelligence/knowledge-base/nonviolent-communication` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/emotional-intelligence/knowledge-base/personal-boundaries` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/emotional-intelligence/knowledge-base/psychological-safety` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/emotional-intelligence/knowledge-base/self-awareness` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/emotional-intelligence/knowledge-base/self-regulation` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/emotional-intelligence/knowledge-base/social-intelligence` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/events` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/events_tp` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/geshtalt` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/kpt` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/lectures1` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/microbiom` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/novosti` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/panicheskie_ataki` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/phytotherapy` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/platnye-treningi-seminary-programmy-tatiana-moonn` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/psiholog-konsultacii-moskva` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/psiholog_moskva` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/psihology` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/psy4psy` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/psychoanalys` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/psypodgotovka1` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/recomend` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/salt` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/schematherapy` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/selfharm` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/semeynie_konflikti_article` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/semeyniy_psiholog` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/seminar555` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/shppp333` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/speaker` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/st2` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/trauma` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/uslugi_aerofobia` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/uslugi_depression` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/uslugi_fin_blocks` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/uslugi_gtr` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/uslugi_konflikti_na_rabote` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/uslugi_lubovnaya_zavisimost` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/uslugi_obida_na_roditelei` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/uslugi_otnosheniya_v_kollektive` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/uslugi_podrostki` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/uslugi_procrastination` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/uslugi_razvod` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/uslugi_sohranit_brak` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/vacuum_cups` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/vigoranie_article` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/vospitanie_article` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/vystupleniya-lekcii-treningi-psiholog-tatiana-moonn` — `forms_without_detected_checkbox`
- `https://xn--l1acaw.xn--p1ai/water` — `forms_without_detected_checkbox`

## Gate

- Do not treat this as legal advice.
- Final publication requires confirmed operator details and legal approval.
- Do not disable Yandex/Google crawling while fixing compliance.
- Current official-source refresh used for this weekly gate: Roskomnadzor personal-data notification portal, Roskomnadzor operator registry, and the current 152-FZ consent/personal-data baseline. No legal text was published or changed.
