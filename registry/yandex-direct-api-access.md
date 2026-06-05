# Yandex Direct API access log

## 2026-06-05

- Project: Moonn / teen intensive advertising preflight.
- Application: `Сентея`.
- Application ID: stored in Yandex OAuth cabinet and local operator notes; do not duplicate client secret in this registry.
- Direct login shown in API settings: `yantaria`.
- API settings page: `Настройки API - Мои заявки`.
- User submitted a full-access API request on 2026-06-05.
- Request list status after submission: `новая`.
- Requested access type: `полный`.
- OAuth token exists locally in ignored file `registry/local-secrets/yandex-direct-oauth.local.json`.
- API smoke test after submission still returns error `58` / `Незавершенная регистрация`: Yandex requires waiting for request confirmation.

Next check:

1. Wait until the request status changes from `новая`.
2. Repeat a safe `clients.get` smoke test without printing tokens.
3. If approved, proceed to read-only campaign/account discovery before creating or changing campaigns.
4. Regenerate the exposed OAuth client secret after the working access path is confirmed.

## 2026-06-05 approval check

- User reported that the request status changed to `одобрена`.
- Safe API smoke test result:
  - endpoint: `https://api.direct.yandex.com/json/v5/clients`;
  - method: `clients.get`;
  - HTTP status: `200`;
  - API result: OK;
  - visible client login: `yantaria`.
- Note: the first post-approval smoke test failed with API error `8000` because `SelectionCriteria` is not a valid parameter for `clients.get`; the corrected request with only `FieldNames: ["Login"]` succeeded.

Next action:

1. Regenerate the exposed OAuth client secret in Yandex ID after this access path is stable.
2. Run read-only Direct account discovery: campaigns, ad groups, ads, keywords, funds/status.
3. Do not create or modify campaigns until the landing/payment/Metрика launch gate is closed.

## 2026-06-05 read-only discovery and draft package

- Read-only Direct discovery was run through API for login `yantaria`.
- Current Direct account state:
  - campaigns: `0`;
  - ad groups: `0`;
  - ads: `0`;
  - keywords: `0`;
  - API errors: none.
- Discovery artifact: `output/yandex-direct-readonly-discovery-2026-06-05.json`.
- GPT export used for context: `C:\Users\yanta\Downloads\chat_export_yandex_direct.json`.
- API-ready draft package generated:
  - JSON: `docs/yandex-direct-teen-intensive-package-2026-06-05.json`;
  - Markdown: `docs/yandex-direct-teen-intensive-package-2026-06-05.md`;
  - campaigns: `5`;
  - search groups: `10`;
  - network groups: `4`;
  - search text ads: `32`.
- Validation:
  - basic text limits passed for search ads: title <= 56, title2 <= 30, text <= 81.
- Launch boundary:
  - Do not create/start campaigns, send ads to moderation, enable retargeting, or change money-path settings without explicit owner confirmation.
  - Retargeting remains blocked until Metrika goals and consent checks are complete.
  - RSYA upload remains blocked until final image assets are selected/generated and approved.

## 2026-06-05 safe campaign shells created

- User requested campaign creation and landing-page readiness recheck before Yandex Direct launch.
- Landing raw HTML preflight with UTM test URL:
  - HTTP status: `200`;
  - `40000`: present;
  - `6-10 июля` / `6–10 июля`: present;
  - `2026`: present;
  - `10:00-18:00`: present;
  - `Сущёвский Вал, 56`: present;
  - `14-17`: present;
  - `Имя родителя`, `Email`, `Телефон`, `+7 (999) 999-99-99`, `Оплатить участие`: present;
  - `Book design`, `Your Name`, `Your Email`, `Your Phone`, `Checkout`: absent;
  - Metrika counter detected: `96397286`;
  - residuals: one native Tilda `Payment method`, Tilda platform label markup.
- Campaign creation script:
  - `scripts/yandex_direct_create_safe_campaign_shells.py`.
- First attempted create requests were rejected by API and created no objects:
  - enum typo `ADD_METRIKA_TAG` corrected to `ADD_METRICA_TAG`;
  - incompatible all-`SERVING_OFF` strategy corrected;
  - `DailyBudget` removed from shell creation because API only allows it with manual strategies.
- Created campaign shells:
  - `Search_Hot_Teen_Intensive`: `710503508`;
  - `Search_Parents_Teens`: `710503509`;
  - `Search_EI_Communication_Stress`: `710503510`;
  - `RSYA_Parents_Teens`: `710503511`;
  - `RSYA_Soft_Education`: `710503512`.
- Post-create Direct discovery:
  - campaigns: `5`;
  - ad groups: `0`;
  - ads: `0`;
  - keywords: `0`;
  - each created campaign status from post-state: `DRAFT`, `State: OFF`.
- Safety boundary:
  - No ad groups, ads, keywords, creatives, retargeting segments, campaign start, payment changes, or moderation launch were created.
  - Budgets must be set/confirmed at final launch stage; shell creation used strategy-level limits only because API rejected `DailyBudget` with the chosen non-manual strategy.
- Creative prompt artifact:
  - `docs/yandex-direct-rsya-photo-prompts-2026-06-05.md`.
