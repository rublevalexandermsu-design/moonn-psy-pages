# Moonn Paid Video Lectures Tilda Plan

Date: 2026-05-03
Workstream: Moonn paid video lectures
Branch: `codex/moonn-paid-video-lectures`

## 5-Point Strategic Check

1. Platform value: high. Paid recordings turn existing lectures/events into reusable products.
2. Obsolescence risk: medium. A one-off Tilda edit will break as soon as prices, videos, or access rules change.
3. Stronger architecture: use a canonical product/access manifest, then configure Tilda pages from that manifest.
4. Reuse: high. The same model can support paid lectures, courses, master classes, bundles, QR pages, and Timepad follow-up offers.
5. 3-12 month risk if done only manually: mismatched prices, orphaned YouTube links, broken buttons, support requests after payment, and no clear audit of who bought what.

## Verified Inputs

- Read-only Tilda API audit found 39 published page candidates with lecture/course/video/payment signals.
- Strongest candidates:
  - `https://moonn.ru/lectures1`, Tilda page `68295899`: likely canonical paid lecture storefront.
  - `https://moonn.ru/events_tp`, Tilda page `66814657`: 11 Timepad links, likely event/archive page.
  - `https://moonn.ru/events`, Tilda page `53668815`: public events page.
  - `https://moonn.ru/psypodgotovka1`, Tilda page `62652841`: already contains "purchase recording" signals.
  - `https://moonn.ru/seminar555`, Tilda page `57927493`: contains YouTube links and paid/seminar signals.
- Default requested price: `1300 RUB` per lecture.

## Tilda Architecture

Recommended model:

1. Product/storefront page:
   - Use `lectures1` as the first pilot storefront unless visual inspection proves another page is the real canonical page.
   - Each lecture card becomes a Tilda product with price `1300`.
   - Button text changes from `Записаться` / `Зарегистрироваться` to `Купить запись` or `Приобрести лекцию`.

2. Payment:
   - Use Tilda cart/payment stack already configured in the project.
   - For live rollout, verify which payment provider is active and whether test payments are possible.
   - Do not change production payment settings blindly.

3. Access after payment:
   - Use Tilda Members / Courses access groups.
   - Buyer is added to the correct group only after successful payment.
   - Each lecture can map to either one group per lecture or one group for the full recordings library.

4. Video viewing:
   - Create protected watch pages inside Tilda Members/Courses.
   - Place the video only on protected watch pages, not on the public sales page.
   - If videos stay on YouTube, unlisted links are not strong copy protection. Treat them as convenience, not real DRM.
   - Stronger option: use a host that supports domain restrictions, signed/private embeds, or platform-level access controls.

5. QR layer:
   - Generate QR to the canonical storefront URL, not to raw videos.
   - Put the QR image and plain URL on the storefront page.
   - Keep QR file name SEO-safe, e.g. `tatyana-munn-paid-lectures-qr.png`.

## Product Manifest

Canonical files created:

- `registry/products/paid-video-lectures.schema.json`
- `registry/products/paid-video-lectures.manifest.json`
- `registry/products/paid-video-lectures-audit-2026-05-03.json`

These files separate public page text from machine data:

- lecture title;
- source page;
- price;
- Timepad source if any;
- video URL;
- Tilda product SKU;
- Members group;
- protected watch page;
- QR target;
- current status and required user input.

## Safe Rollout Plan

1. Pilot one lecture in staging:
   - choose one lecture card on `lectures1`;
   - create a test product at `1300 RUB`;
   - create one protected watch page/group;
   - connect payment and post-payment group access;
   - test payment flow in safe/test mode or with an agreed live test payment;
   - verify buyer sees the video only after payment.

2. Scale to all selected lectures:
   - fill manifest with final video URLs;
   - create products/groups/pages in batches;
   - update buttons;
   - publish staging;
   - run visual and purchase-flow QA.

3. Production rollout:
   - only after staging proof;
   - preserve existing SEO/title/schema;
   - update `Product`, `VideoObject`, and `Course` schema;
   - request indexing after the page stabilizes.

## High-Risk Gates

Do not proceed to production until these are confirmed:

- payment provider in Tilda is active and legal for this seller;
- checkout shows correct seller/payment information;
- refund/offer/privacy documents are present and linked;
- video access after payment was tested;
- raw YouTube/private video links are not exposed on the public sales page;
- user approved live publication and live payment path.

## User Input Needed

- Final list of lectures to sell.
- Video URL for each lecture.
- Decision: one purchase per lecture or bundle/library access.
- Confirmation which Tilda payment provider should be used.
- Approval for one staging or safe live test purchase.

## Official Tilda References Checked

- Tilda customer accounts for online store: `https://help-ru.tilda.cc/online-store/customer-accounts`
- Tilda Members access after payment: `https://help-ru.tilda.cc/membership`
- Tilda courses and paid course access: `https://help-ru.tilda.cc/courses`

