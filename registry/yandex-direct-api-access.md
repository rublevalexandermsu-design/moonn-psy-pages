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
