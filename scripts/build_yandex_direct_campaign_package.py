from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT_JSON = ROOT / "docs" / "yandex-direct-teen-intensive-package-2026-06-05.json"
OUT_MD = ROOT / "docs" / "yandex-direct-teen-intensive-package-2026-06-05.md"

LANDING_URL = "https://xn--l1acaw.xn--p1ai/podrostkovyy-lager-psihologiya"

COMMON_NEGATIVES = [
    "бесплатно",
    "скачать",
    "pdf",
    "реферат",
    "курсовая",
    "диплом",
    "презентация",
    "форум",
    "книга",
    "тест",
    "тесты",
    "вакансии",
    "работа",
    "стажировка",
    "сотрудники",
    "онлайн",
    "дистанционно",
    "вебинар",
    "запись вебинара",
    "видеоурок",
    "репетитор",
    "подготовка егэ",
    "подготовка огэ",
    "математика",
    "русский язык",
    "английский язык",
    "спорт",
    "футбол",
    "танцы",
    "робототехника",
    "программирование",
    "языковой лагерь",
    "палаточный",
    "загородный",
    "море",
    "сочи",
    "крым",
    "санаторий",
    "круглосуточный",
    "ночёвка",
    "дошкольники",
    "малыши",
    "детский сад",
    "начальная школа",
    "взрослые",
    "студенты",
    "психиатр",
    "психотерапевт",
    "клиника",
    "больница",
    "врач",
    "таблетки",
    "лекарства",
    "диагноз",
    "симптомы",
    "реабилитация",
    "экстренная помощь",
    "травма",
    "насилие",
]


def ad(title: str, title2: str, text: str, content: str) -> dict:
    return {
        "title": title,
        "title2": title2,
        "text": text,
        "href": f"{LANDING_URL}?utm_source=yandex&utm_medium=cpc&utm_campaign={{campaign_name}}&utm_content={content}_{{ad_id}}_{{phrase_id}}_{{device_type}}_{{position_type}}&utm_term={{keyword}}",
    }


PACKAGE = {
    "meta": {
        "date": "2026-06-05",
        "scope": "api_ready_draft_package",
        "landing_url": LANDING_URL,
        "owner_confirmation_required": [
            "creating campaigns in Direct",
            "sending ads to moderation",
            "starting campaigns",
            "changing payment or balance settings",
            "enabling retargeting",
        ],
        "landing_facts": {
            "age": "14-17",
            "dates": "6-10 июля 2026",
            "time": "10:00-18:00",
            "address": "Москва, Сущёвский Вал, 56",
            "price": "40 000 ₽",
        },
    },
    "campaigns": [
        {
            "name": "Search_Hot_Teen_Intensive",
            "type": "search",
            "daily_budget_rub_recommended": 3500,
            "api_status": "prepare_paused_only",
            "groups": [
                {
                    "name": "подростковый интенсив",
                    "daily_budget_rub_source": 1500,
                    "keywords": [
                        "подростковый интенсив москва",
                        "интенсив для подростков москва",
                        "летний интенсив для подростков",
                        "городской интенсив для подростков",
                        "интенсив для подростков 14 17",
                        "подростковый интенсив речи",
                    ],
                    "group_negatives": ["онлайн", "бесплатно", "скачать", "вебинар", "логопед", "дефектолог"],
                    "ads": [
                        ad("Подростковый интенсив", "Москва, 6-10 июля", "Речь, общение, эмоции и ИИ. Очная группа 14-17 лет.", "s01"),
                        ad("Интенсив для подростков", "10:00-18:00", "5 дней в центре Москвы. Камерная группа и практика общения.", "s02"),
                        ad("Летний интенсив 14-17", "Сущёвский Вал, 56", "Подростки тренируют речь, диалог и участие в группе.", "s03"),
                        ad("Интенсив без скуки", "Речь, общение, ИИ", "Практический формат для подростков 14-17 лет в Москве.", "s04"),
                        ad("Интенсив Татьяны Мунн", "Для подростков", "Очная программа: речь, уверенность, общение и эмоции.", "s05"),
                        ad("Городской интенсив", "Без ночёвки", "Днём занятия, вечером подросток дома. Москва, 6-10 июля.", "s06"),
                    ],
                },
                {
                    "name": "психологический лагерь",
                    "daily_budget_rub_source": 1200,
                    "keywords": [
                        "психологический лагерь для подростков москва",
                        "городской психологический лагерь подростки",
                        "психологический интенсив для подростков",
                        "летний психологический лагерь подростки",
                    ],
                    "group_negatives": ["клиника", "врач", "психиатр", "загородный", "санаторий", "палаточный", "море"],
                    "ads": [
                        ad("Психологический лагерь", "Для подростков", "Городской формат: речь, эмоции, общение и ИИ-практика.", "s07"),
                        ad("Лагерь для подростков", "Москва, июль", "5 дней очных занятий в камерной группе 10-12 человек.", "s08"),
                        ad("Городской лагерь 14-17", "С 6 по 10 июля", "Практика общения, речи и эмоций в центре Москвы.", "s09"),
                        ad("Психологический интенсив", "10-12 участников", "Спокойная программа для подростков: диалог, речь, эмоции.", "s10"),
                        ad("Лагерь без ночёвки", "Москва, центр", "Городской интенсив 14-17 лет. Посмотрите программу.", "s11"),
                    ],
                },
                {
                    "name": "курс для подростков",
                    "daily_budget_rub_source": 800,
                    "keywords": [
                        "курс для подростков москва",
                        "курс общения для подростков",
                        "курс уверенности для подростков",
                        "курс речи для подростков",
                    ],
                    "group_negatives": ["онлайн", "бесплатно", "видео", "егэ", "огэ", "логопед", "дефектолог"],
                    "ads": [
                        ad("Курс для подростков", "Москва, июль", "Речь, общение, эмоции и ИИ-практика за 5 дней.", "s12"),
                        ad("Курс общения 14-17", "Очная группа", "Диалоги, задания и практика выступления в малой группе.", "s13"),
                        ad("Курс уверенной речи", "Для подростков", "Практика речи и участия в обсуждении. 5 дней очно.", "s14"),
                        ad("Летний курс 14-17", "6-10 июля", "Камерный формат: общение, эмоции, речь и ИИ.", "s15"),
                        ad("Занятия для подростков", "Очный формат", "5 дней практики в Москве. Группа 10-12 человек.", "s16"),
                    ],
                },
            ],
        },
        {
            "name": "Search_Parents_Teens",
            "type": "search",
            "daily_budget_rub_recommended": 2400,
            "api_status": "prepare_paused_only",
            "groups": [
                {
                    "name": "родители подростков",
                    "daily_budget_rub_source": 700,
                    "keywords": [
                        "родителям подростков москва",
                        "куда отправить подростка летом москва",
                        "что делать подростку летом москва",
                        "подросток 14 лет занятия москва",
                        "подросток 15 лет занятия москва",
                        "подросток 16 лет занятия москва",
                    ],
                    "group_negatives": ["форум", "книга", "бесплатно", "идеи дома", "секция", "спорт", "онлайн"],
                    "ads": [
                        ad("Идея на июль", "Для подростка 14-17", "Городской интенсив в Москве: речь, эмоции, общение, ИИ.", "s29"),
                    ],
                },
                {
                    "name": "каникулы для подростка Москва",
                    "daily_budget_rub_source": 900,
                    "keywords": [
                        "каникулы для подростка москва",
                        "летние каникулы подросток москва",
                        "городской лагерь для подростков москва",
                        "летний городской лагерь подростки",
                    ],
                    "group_negatives": ["море", "сочи", "крым", "санаторий", "бесплатно", "лагерь с ночевкой", "круглосуточный"],
                    "ads": [
                        ad("Каникулы для подростка", "Москва, 5 дней", "Очная программа без ночёвки. Группа 10-12 человек.", "s30"),
                    ],
                },
                {
                    "name": "занятия для подростков Москва",
                    "daily_budget_rub_source": 700,
                    "keywords": [
                        "занятия для подростков москва",
                        "развивающие занятия для подростков москва",
                        "летние занятия для подростков москва",
                        "группа для подростков москва",
                    ],
                    "group_negatives": ["спорт", "танцы", "английский", "робототехника", "малыши", "дошкольники", "онлайн", "клиника", "врач"],
                    "ads": [
                        ad("Летние занятия 14-17", "Центр Москвы", "Подростковый интенсив речи, общения, эмоций и ИИ.", "s31"),
                        ad("Занятия для подростков", "6-10 июля", "Живая программа в группе: речь, диалог, эмоции, ИИ.", "s32"),
                    ],
                },
            ],
        },
        {
            "name": "Search_EI_Communication_Stress",
            "type": "search",
            "daily_budget_rub_recommended": 2100,
            "api_status": "prepare_paused_only",
            "groups": [
                {
                    "name": "эмоциональный интеллект подростки",
                    "daily_budget_rub_source": 600,
                    "keywords": [
                        "эмоциональный интеллект подростки",
                        "развитие эмоционального интеллекта подростков",
                        "занятия эмоции подростки",
                        "эмоции и общение подростки",
                    ],
                    "group_negatives": ["книга", "тест", "бесплатно", "онлайн", "клиника", "врач", "диагноз"],
                    "ads": [
                        ad("Эмоции и общение", "Для подростков", "Упражнения, карточки эмоций, диалог и ИИ-практика.", "s17"),
                        ad("Эмоциональный интеллект", "Подростки 14-17", "Практика общения и понимания эмоций в небольшой группе.", "s18"),
                        ad("Навыки общения", "Москва, июль", "Речь, эмоции и командные задания в очном формате.", "s19"),
                        ad("Практика эмоций", "В группе 10-12", "Спокойные упражнения и обсуждения для подростков 14-17.", "s20"),
                    ],
                },
                {
                    "name": "подросток стресс",
                    "daily_budget_rub_source": 500,
                    "keywords": [
                        "подросток стресс после экзаменов",
                        "разгрузка после экзаменов подросток",
                        "занятия после экзаменов подростки",
                        "летняя разгрузка для подростка",
                    ],
                    "group_negatives": ["врач", "таблетки", "клиника", "санаторий", "егэ подготовка", "огэ подготовка", "бесплатно"],
                    "ads": [
                        ad("После экзаменов", "Летний формат", "Речь, общение и мягкая разгрузка после учебного года.", "s21"),
                        ad("Лето после экзаменов", "5 дней очно", "Городской интенсив с практикой общения, речи и ИИ.", "s22"),
                        ad("Спокойный июль 14-17", "Москва", "Днём занятия, вечером подросток дома. Группа 10-12.", "s23"),
                    ],
                },
                {
                    "name": "подросток общение",
                    "daily_budget_rub_source": 600,
                    "keywords": [
                        "подросток общение занятия",
                        "навыки общения для подростков",
                        "занятия по общению для подростков москва",
                        "коммуникативные навыки подростки",
                    ],
                    "group_negatives": ["форум", "книга", "бесплатно", "онлайн", "тест"],
                    "ads": [
                        ad("Общение для подростков", "Практика в группе", "Диалог, командные задания и обратная связь.", "s24"),
                        ad("Навыки общения 14-17", "Москва", "Интенсив речи, эмоций и ИИ-практики. 6-10 июля.", "s25"),
                        ad("Группа общения", "Для подростков", "Небольшая группа и понятная программа на 5 дней.", "s26"),
                    ],
                },
                {
                    "name": "подросток неуверенность",
                    "daily_budget_rub_source": 400,
                    "keywords": [
                        "подросток неуверенность занятия",
                        "уверенная речь подросток",
                        "уверенность у подростка курс",
                        "тренинг уверенности для подростков москва",
                    ],
                    "group_negatives": ["врач", "клиника", "психиатр", "логопед", "дефектолог", "взрослые", "онлайн", "бесплатно"],
                    "ads": [
                        ad("Уверенная речь", "Для подростков", "Практика выступления и диалога в спокойной группе.", "s27"),
                        ad("Практика уверенности", "5 дней очно", "Речь, общение и участие в группе без перегруза.", "s28"),
                    ],
                },
            ],
        },
        {
            "name": "RSYA_Parents_Teens",
            "type": "network",
            "daily_budget_rub_recommended": 1800,
            "api_status": "creative_assets_required_before_api_upload",
            "groups": [
                {"name": "родители подростков", "daily_budget_rub_source": 1000, "keywords": ["родители подростков"], "ads": []},
                {"name": "каникулы / июль", "daily_budget_rub_source": 800, "keywords": ["каникулы подростки июль москва"], "ads": []},
            ],
        },
        {
            "name": "RSYA_Soft_Education",
            "type": "network",
            "daily_budget_rub_recommended": 1300,
            "api_status": "creative_assets_required_before_api_upload",
            "groups": [
                {"name": "речь / общение / эмоции", "daily_budget_rub_source": 800, "keywords": ["речь общение эмоции подростки"], "ads": []},
                {"name": "ИИ-практика", "daily_budget_rub_source": 500, "keywords": ["ИИ практика подростки образование"], "ads": []},
            ],
        },
    ],
    "retargeting": {
        "status": "do_not_create_before_metrika_goals_and_consent_check",
        "segments": ["посетители без заявки", "начали оплату без успеха"],
    },
    "common_negative_keywords": COMMON_NEGATIVES,
}


def render_markdown(package: dict) -> str:
    lines = [
        "# Yandex Direct teen intensive campaign package",
        "",
        f"- Landing: {package['meta']['landing_url']}",
        "- Status: API-ready draft package; owner confirmation required before creation/moderation/start.",
        "",
        "## Campaigns",
        "",
    ]
    for campaign in package["campaigns"]:
        lines.append(f"### {campaign['name']}")
        lines.append(f"- Type: {campaign['type']}")
        lines.append(f"- Recommended daily budget: {campaign['daily_budget_rub_recommended']} RUB")
        lines.append(f"- API status: {campaign['api_status']}")
        for group in campaign["groups"]:
            lines.append(f"- Group: {group['name']} ({len(group.get('keywords', []))} keywords, {len(group.get('ads', []))} ads)")
        lines.append("")
    total_budget = sum(item["daily_budget_rub_recommended"] for item in package["campaigns"] if item["api_status"] != "do_not_create")
    lines.extend(
        [
            "## Launch Gates",
            "",
            f"- Sum of recommended daily budgets, without retargeting: {total_budget} RUB/day.",
            "- Retargeting is blocked until Metrika goals and consent are checked.",
            "- RSYA requires final image assets before API upload.",
            "- No campaign should be started without owner approval.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    OUT_JSON.write_text(json.dumps(PACKAGE, ensure_ascii=False, indent=2), encoding="utf-8")
    OUT_MD.write_text(render_markdown(PACKAGE), encoding="utf-8")
    print(OUT_JSON)
    print(OUT_MD)
    print(json.dumps({
        "campaigns": len(PACKAGE["campaigns"]),
        "search_groups": sum(len(c["groups"]) for c in PACKAGE["campaigns"] if c["type"] == "search"),
        "network_groups": sum(len(c["groups"]) for c in PACKAGE["campaigns"] if c["type"] == "network"),
        "search_ads": sum(len(g.get("ads", [])) for c in PACKAGE["campaigns"] for g in c["groups"]),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
