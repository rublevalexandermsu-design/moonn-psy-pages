# Teen intensive Direct landing preflight

Date: 2026-06-04
Tilda project: 8326812
Tilda page: 140348786
Live URL: https://xn--l1acaw.xn--p1ai/podrostkovyy-lager-psihologiya
Branch: codex/moonn-camp-page-update

## Page changes completed in Git

- Removed the remaining Direct preflight risks from the canonical Tilda package:
  - no `Book design` placeholder in source;
  - no raw `Your Name`, `Your Email`, `Your Phone`, `Checkout` labels in the page source;
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

## 2026-06-05 live publication completed

Tilda page-specific HEAD for page `140348786` was saved through the authenticated Rublev/Alexander Chrome session using the page's internal `aceeditor_head` editor. Tilda save marker:

- `HEAD_UI_SAVED_140348786_14280`.

The page was then published from `https://tilda.ru/page/?pageid=140348786&projectid=8326812`.

Live raw HTML verification on `https://xn--l1acaw.xn--p1ai/podrostkovyy-lager-psihologiya` returned:

- HTTP status: `200`;
- `@7c3e190`: present;
- `20260604-teen-intensive-direct-preflight`: present;
- old `@44ebc4f`: absent;
- old `20260604-teen-intensive-direct-cta`: absent;
- `Book design`: absent;
- `4 места`: absent;
- public canonical URL for `xn--l1acaw.xn--p1ai`: present.

Rendered browser check opened the public page in Chrome and confirmed the new mounted content is visible, including:

- group-size copy `10-12`;
- address `Сущёвский Вал, 56`;
- date range `6 по 10 июля 2026`;
- no visible first-screen `4 места` scarcity claim.

Remaining checks before ad spend:

- Telegram, WhatsApp and phone click events in Metrika;

## Incident note

The first 2026-06-05 GUI attempt used accessibility/UIA field replacement. The field visually showed the new loader, but Tilda did not persist it after Save because the site's JavaScript editor state was not updated. The working rule is to update `aceeditor_head` directly and dispatch editor/textarea events before clicking Save; do not treat UIA readback alone as proof of Tilda persistence.

## 2026-06-05 native ST100 checkout cleanup

The native Tilda cart record `rec2252909191` / ST100 was edited through the authenticated Rublev/Alexander Chrome session and published.

Live raw HTML verification after publication:

- `Your Name`: `0`;
- `Your Email`: `0`;
- `Your Phone`: `0`;
- `Checkout`: `0`;
- `Book design`: `0`;
- `+1(000)000-0000`: `0`;
- `Имя родителя`: `1`;
- `Телефон`: `1`;
- `Оплатить участие`: `1`;
- `+7 (999) 999-99-99`: `3`.

Rendered checkout verification in Playwright with `locale=ru-RU` and `?pay=teen-camp-2026`:

- `Payment method`: `0`;
- `Способ оплаты`: `1`;
- `Your Name`: `0`;
- `Имя родителя`: `1`;
- `Your Phone`: `0`;
- `+1(000)000-0000`: `0`;
- `+7 (999) 999-99-99`: `1`;
- `Checkout`: `0`;
- `Перейти к оплате`: `1`.

Screenshot artifact: `output/teen-camp-rendered-checkout-2026-06-05.png`.

Residual raw-source caveat:

- One raw `Payment method` string remains inside Tilda's native payment-system group generated by ST100 when two payment variants are connected.
- The rendered checkout is localized by the existing teen-camp cart runtime repair layer.
- Removing the raw native `Payment method` completely would require changing the payment-method configuration or replacing the native Tilda cart, which is a payment-risk change and must stay behind a separate approval gate.

## 2026-06-05 mobile/link preflight

Rendered Playwright checks completed for desktop and mobile widths `414`, `390`, `360`.

Desktop `1365x900`:

- horizontal overflow: `false`;
- Telegram links: present;
- WhatsApp links: present;
- mobile phone link: `tel:+79777770303` present;
- `Оставить заявку`: `2`;
- `Посмотреть программу`: `1`;
- old visible texts `Book design`, `Your Name`, `Your Email`, `Your Phone`, `Checkout`, `4 места`: absent;
- key texts `6 по 10 июля 2026`, `Сущёвский Вал, 56`, `14-17`, `40 000`: present.

Mobile `414x896`, `390x844`, `360x740`:

- horizontal overflow: `false` on all three widths;
- Telegram links: `11`;
- WhatsApp links: `2`;
- mobile phone link: `1`;
- `Оставить заявку`: `2`;
- `Посмотреть программу`: `1`;
- old visible texts `Book design`, `Your Name`, `Your Email`, `Your Phone`, `Checkout`, `4 места`: absent;
- key texts `6 по 10 июля 2026`, `Сущёвский Вал, 56`, `14-17`, `40 000`: present.

Screenshot artifacts:

- `output/teen-camp-preflight-1365.png`;
- `output/teen-camp-preflight-414.png`;
- `output/teen-camp-preflight-390.png`;
- `output/teen-camp-preflight-360.png`;
- `output/teen-camp-checkout-preflight-2026-06-05b.png`.

Remaining gated item:

- Full raw-source removal of the single native `Payment method` string requires changing the payment-method setup. Tilda documentation says when two or more payment systems are connected, buyers can choose a payment method in the shopping cart; this site currently has T-Bank card payment and T-Bank installment enabled. Disabling one method or replacing native ST100 is a payment-path change and requires a separate money gate.
