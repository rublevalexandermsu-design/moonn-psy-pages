# Teen intensive Direct landing preflight

Date: 2026-06-04
Tilda project: 8326812
Tilda page: 140348786
Live URL: https://xn--l1acaw.xn--p1ai/podrostkovyy-lager-psihologiya
Branch: codex/moonn-camp-page-update

## Page changes completed in Git

- Removed the remaining Direct preflight risks from the canonical Tilda package:
  - no `Book design` placeholder in source;
  - no raw `Your Name`, `Your Email`, `Your Phone`, `Payment method`, `Checkout` labels in the page source;
  - phone placeholder changed to `+7 (999) 999-99-99`;
  - non-verifiable `4 места из 12` scarcity text replaced with stable `группа 10-12 / до 12`;
  - primary first-screen CTA is `Оставить заявку`;
  - secondary first-screen CTA is `Посмотреть программу`;
  - dates now include `6-10 июля 2026`;
  - public domain canonical/OG/schema URLs use `https://xn--l1acaw.xn--p1ai/podrostkovyy-lager-psihologiya`;
  - Event schema includes `typicalAgeRange: 14-17` and PeopleAudience 14-17;
  - page emits Metrika `reachGoal` events for lead click, Telegram, WhatsApp, phone, program, PDF download, and payment start;
  - explicit personal-data/participation consent text added near hero and final CTA;
  - mobile phone link `tel:+79777770303` added.

## Commits

- `7c3e190` - Complete teen camp Direct landing preflight
- `356431d` - Point teen camp loader to Direct preflight version

The branch was pushed to GitHub.

## Verified

CDN check for `@7c3e190` returned HTTP 200 and confirmed:

- `6-10 июля 2026`: present;
- `Book design`: absent;
- `4 места`: absent;
- `+7 (999) 999-99-99`: present;
- Metrika goal strings `click_telegram`, `payment_start`, `click_phone`: present;
- public canonical domain `xn--l1acaw.xn--p1ai`: present.

Tilda HEAD editor UIA state was read after replacement:

- page-specific HEAD field contained `@7c3e190`;
- page-specific HEAD field contained `direct-preflight`;
- page-specific HEAD field did not contain `@44ebc4f`.

## Blocker

Final Tilda publish was not verified in this pass because Windows repeatedly switched to the lock-screen / no-active-window state. The page-specific HEAD field was updated and saved through the authenticated Chrome session, but the live page still returned the old loader:

- live `@7c3e190`: false;
- live `20260604-teen-intensive-direct-preflight`: false;
- live `@44ebc4f`: true;
- live `20260604-teen-intensive-direct-cta`: true.

## Next action

After the Windows desktop is unlocked and stable:

1. Open `https://tilda.ru/page/?pageid=140348786&projectid=8326812`.
2. Click `Опубликовать`.
3. Verify live HTML contains `@7c3e190` and `20260604-teen-intensive-direct-preflight`.
4. Re-run rendered browser checks for:
   - first-screen CTAs;
   - Russian checkout labels and phone mask;
   - Telegram / WhatsApp / phone links;
   - mobile widths 360 / 390 / 414 px;
   - absence of `Book design`, English checkout labels, and `4 места`.

