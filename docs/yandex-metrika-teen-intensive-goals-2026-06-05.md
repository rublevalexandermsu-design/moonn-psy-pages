# Yandex Metrika Goals - Teen Intensive

Date: 2026-06-05

Counter: `96397286`

Landing: `https://xn--l1acaw.xn--p1ai/podrostkovyy-lager-psihologiya`

## API Status

Current local OAuth token is valid for Yandex Direct but does not have Yandex Metrika rights.

Checked endpoints:

- `https://api-metrika.yandex.net/management/v1/counters` -> `403`
- `https://api-metrika.yandex.net/management/v1/counter/96397286/goals` -> `403`

No Metrika goals were created through API in this pass.

## Existing Automatic Goals

Observed in the Metrika GUI:

- Auto form submission goal.
- Auto messenger click goal.
- Auto social click goal.
- Auto phone click goal.
- Several Yandex Business auto button-click goals.

These are useful as a fallback, but they are not clean enough for Direct optimization because they are generic and do not isolate the teen intensive funnel.

## Required Explicit JavaScript Goals

| Goal name | Type | Purpose |
|---|---|---|
| `lead_click` | JavaScript event | Visitor clicked primary application CTA. |
| `lead_submit` | JavaScript event | Visitor successfully submitted a lead form. |
| `click_telegram` | JavaScript event | Visitor clicked Telegram CTA. |
| `click_whatsapp` | JavaScript event | Visitor clicked WhatsApp CTA. |
| `click_phone` | JavaScript event | Visitor clicked phone link. |
| `program_view` | JavaScript event | Visitor clicked / moved to the program section. |
| `pdf_download` | JavaScript event | Visitor opened a PDF/downloadable material. |
| `payment_start` | JavaScript event | Visitor opened the Tilda/T-Bank checkout from the page. |
| `payment_submit` | JavaScript event | Visitor submitted the checkout form. |
| `payment_success` | JavaScript event | Tilda checkout success signal / visible success box. |

## Page Instrumentation Status

The canonical Tilda HTML now fires:

- `lead_click`
- `lead_submit`
- `click_telegram`
- `click_whatsapp`
- `click_phone`
- `program_view`
- `pdf_download`
- `payment_start`
- `payment_submit`
- `payment_success`

Implementation files:

- `docs/teen-psychology-camp-2026/tilda-page-final.html`
- `docs/teen-psychology-camp-2026/tilda-html-block-final.html`

## Creation Path

Preferred path: create the above goals through Metrika API after OAuth receives Metrika management rights.

Scripted path:

```powershell
python scripts\yandex_metrika_create_teen_goals.py --secret registry\local-secrets\yandex-metrika-oauth.local.json
python scripts\yandex_metrika_create_teen_goals.py --secret registry\local-secrets\yandex-metrika-oauth.local.json --apply
```

The first command is a dry run. The second command creates only missing goals and skips existing ones.

Fallback path: create manually in the GUI:

1. Open `https://metrika.yandex.ru/goals?id=96397286`.
2. Click `Добавить цель`.
3. Choose `JavaScript-событие`.
4. Use exact goal name from the table above.
5. Save.
6. Repeat for each goal.
7. Test clicks on the live page and verify hits in Metrika.

## Launch Gate

Do not use automatic Direct optimization to conversions until explicit teen-intensive goals exist and at least click goals are manually tested.

If goals cannot be created before first traffic test, launch only a very small manual-control test and optimize by observed visits/clicks, not by CPA automation.
