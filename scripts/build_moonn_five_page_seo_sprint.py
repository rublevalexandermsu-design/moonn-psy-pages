from __future__ import annotations

import csv
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
ASSETS = ROOT / "assets"
RUN_DATE = datetime.now(timezone.utc).date().isoformat()

PACKET_JSON = DOCS / f"moonn-five-page-seo-packets-{RUN_DATE}.json"
PACKET_MD = DOCS / f"moonn-five-page-seo-packets-{RUN_DATE}.md"
PACKET_CSV = DOCS / f"moonn-five-page-seo-packets-{RUN_DATE}.csv"
LEDGER_JSON = DOCS / f"moonn-five-page-seo-change-ledger-{RUN_DATE}.json"
LEDGER_MD = DOCS / f"moonn-five-page-seo-change-ledger-{RUN_DATE}.md"
LEDGER_CSV = DOCS / f"moonn-five-page-seo-change-ledger-{RUN_DATE}.csv"
REINDEX_TXT = DOCS / f"moonn-five-page-reindex-urls-{RUN_DATE}.txt"
HEAD_SNIPPET = DOCS / f"moonn-five-page-seo-sprint-head-snippet-{RUN_DATE}.html"
ASSET_JS = ASSETS / "moonn-five-page-seo-sprint-layer.js"


PERSON_ID = "https://xn--l1acaw.xn--p1ai/#tatiana-munn"
WEBSITE_ID = "https://xn--l1acaw.xn--p1ai/#website"
YANDEX_SERVICES_PROFILE = "https://uslugi.yandex.ru/profile/TatyanaKumskovamunn-948629"
YCLIENTS_URL = "https://n461584.yclients.com/"


PAGES = [
    {
        "key": "teen_camp",
        "url": "https://xn--l1acaw.xn--p1ai/podrostkovyy-lager-psihologiya",
        "alias": "podrostkovyy-lager-psihologiya",
        "sourcePageId": "140348786",
        "role": "commercial_event",
        "funnelRole": "lead_and_payment",
        "priority": "P0",
        "title": "Подростковый психологический лагерь в Москве | Татьяна Мунн",
        "description": "Подростковый психологический лагерь в Москве: эмоции, уверенность, общение, тревожность и камерная группа с психологом МГУ Татьяной Мунн.",
        "targetH1": "Подростковый психологический лагерь в Москве",
        "intent": "Родитель ищет безопасную практическую программу для подростка, а не общую психологическую статью.",
        "hypothesis": "Сужение страницы под родителя подростка и запросы про психологический лагерь даст больше релевантных показов и кликов, чем общий блок с программой.",
        "targetQueries": [
            "подростковый психологический лагерь Москва",
            "лагерь для подростков психология",
            "тревожность и общение подростков",
            "психологический лагерь для подростков",
        ],
        "issues": ["missing_h1_raw", "placeholder_text", "needs_cta_goal"],
        "allowedLiveChanges": ["seo_metadata", "rendered_h1", "faq_aeo_block", "click_goals"],
        "blockedLiveChanges": ["price", "payment_provider", "legal_text", "personal_data"],
        "schemaTypes": ["WebPage", "Event", "FAQPage", "BreadcrumbList"],
        "answerBlock": {
            "heading": "Кому подходит психологический лагерь",
            "items": [
                "Подростку 12+ трудно общаться, он стесняется, тревожится или избегает новых ситуаций.",
                "Родителю важно дать ребёнку практику общения, уверенности и понимания эмоций в небольшой группе.",
                "Формат подходит как первый мягкий шаг перед индивидуальной консультацией или программой развития навыков.",
            ],
            "cta": "Уточнить участие",
            "ctaGoal": "moonn_seo_teen_camp_contact",
        },
        "faq": [
            {
                "question": "Что даёт подростковый психологический лагерь?",
                "answer": "Он помогает подростку безопасно потренировать общение, уверенность, понимание эмоций и взаимодействие со сверстниками в небольшой группе.",
            },
            {
                "question": "Кому подходит этот формат?",
                "answer": "Формат подходит родителям подростков, которые видят тревожность, стеснение, сложности общения или снижение уверенности.",
            },
            {
                "question": "Можно ли сначала уточнить детали?",
                "answer": "Да, перед участием можно написать Татьяне Мунн в Telegram или WhatsApp и обсудить возраст подростка, ожидания и формат.",
            },
        ],
    },
    {
        "key": "art_gallery",
        "url": "https://xn--l1acaw.xn--p1ai/kartiny-tatiany-munn",
        "alias": "kartiny-tatiany-munn",
        "sourcePageId": "140864526",
        "role": "trust_and_product",
        "funnelRole": "trust_and_art_purchase",
        "priority": "P1",
        "title": "Картины Татьяны Мунн | галерея, арт и персональный код",
        "description": "Галерея картин Татьяны Мунн: авторские работы, визуальный код, интерьерный арт и контакт для выбора картины или обсуждения заказа.",
        "targetH1": "Галерея картин Татьяны Мунн",
        "intent": "Посетитель смотрит личный стиль, доверие, визуальный продукт и способ выбрать работу.",
        "hypothesis": "Галерея лучше работает как доверительный и продуктовый слой, если отделить арт-интент от общей психологии и добавить понятный CTA.",
        "targetQueries": [
            "картины Татьяны Мунн",
            "галерея Татьяны Мунн",
            "авторские картины психолога",
            "энергетические картины Татьяна Мунн",
        ],
        "issues": ["needs_art_intent", "needs_cta_goal"],
        "allowedLiveChanges": ["seo_metadata", "faq_aeo_block", "click_goals"],
        "blockedLiveChanges": ["prices", "payment_provider", "unsupported_art_claims"],
        "schemaTypes": ["CollectionPage", "ItemList", "FAQPage", "BreadcrumbList"],
        "answerBlock": {
            "heading": "Как выбрать картину",
            "items": [
                "Откройте галерею и выберите работу, которая эмоционально откликается по цвету, форме и настроению.",
                "Если нужна помощь с выбором, можно написать Татьяне и обсудить задачу: интерьер, подарок или личная история.",
                "Галерея усиливает доверие к авторскому стилю Татьяны Мунн, но не является медицинским или терапевтическим обещанием.",
            ],
            "cta": "Обсудить картину",
            "ctaGoal": "moonn_seo_art_contact",
        },
        "faq": [
            {
                "question": "Можно ли купить картину Татьяны Мунн?",
                "answer": "Да, страницу нужно использовать как галерею и точку контакта: посетитель выбирает работу и уточняет доступность или заказ.",
            },
            {
                "question": "Это психологическая услуга?",
                "answer": "Нет, галерея является отдельным авторским арт-направлением и доверительным слоем сайта.",
            },
        ],
    },
    {
        "key": "exam_support",
        "url": "https://xn--l1acaw.xn--p1ai/psypodgotovka1",
        "alias": "psypodgotovka1",
        "sourcePageId": "62652841",
        "role": "commercial_service",
        "funnelRole": "lead",
        "priority": "P0",
        "title": "Экзамены без паники: психологическая подготовка к ОГЭ и ЕГЭ",
        "description": "Экзамены без паники: психологическая подготовка подростков к ОГЭ, ЕГЭ и сессии, работа со стрессом, тревогой и уверенностью.",
        "targetH1": "Экзамены без паники: психологическая подготовка к ОГЭ и ЕГЭ",
        "intent": "Родитель или подросток ищет помощь перед экзаменами, а не общий текст о подготовке.",
        "hypothesis": "Уточнение под ОГЭ/ЕГЭ и тревогу перед экзаменами увеличит CTR по низко- и среднечастотным запросам.",
        "targetQueries": [
            "подготовка к ЕГЭ без паники",
            "стресс перед экзаменом",
            "психологическая подготовка к ОГЭ",
            "как справиться с тревогой перед экзаменом",
        ],
        "issues": ["needs_intent_refocus", "needs_cta_goal"],
        "allowedLiveChanges": ["seo_metadata", "faq_aeo_block", "click_goals"],
        "blockedLiveChanges": ["medical_claims", "guaranteed_exam_result"],
        "schemaTypes": ["WebPage", "ProfessionalService", "FAQPage", "BreadcrumbList"],
        "answerBlock": {
            "heading": "Что делать, если экзамены вызывают панику",
            "items": [
                "Сначала важно снизить телесное напряжение и вернуть ощущение контроля, а не просто заставлять подростка больше учиться.",
                "На консультации разбираются тревога, страх ошибки, давление родителей, стеснение и сценарии поведения на экзамене.",
                "Цель страницы - привести родителя или подростка к понятному шагу: коротко описать ситуацию и записаться на консультацию.",
            ],
            "cta": "Записаться на консультацию",
            "ctaGoal": "moonn_seo_exam_consult",
        },
        "faq": [
            {
                "question": "Помогает ли психологическая подготовка к ЕГЭ и ОГЭ?",
                "answer": "Она не заменяет учебную подготовку, но помогает снизить тревогу, собраться, справляться со страхом ошибки и спокойнее проходить экзаменационный период.",
            },
            {
                "question": "Когда лучше обращаться?",
                "answer": "Лучше обращаться заранее, но даже короткая работа перед экзаменом может помочь подростку структурировать тревогу и план действий.",
            },
        ],
    },
    {
        "key": "consultations",
        "url": "https://xn--l1acaw.xn--p1ai/psiholog-konsultacii-moskva",
        "alias": "psiholog-konsultacii-moskva",
        "sourcePageId": "135430346",
        "role": "main_commercial_service",
        "funnelRole": "lead",
        "priority": "P0",
        "title": "Психолог в Москве и онлайн | консультации Татьяны Мунн",
        "description": "Психолог в Москве и онлайн: консультации Татьяны Мунн, психолога МГУ, для взрослых, подростков и родителей при тревоге, стрессе и отношениях.",
        "targetH1": "Психолог в Москве и онлайн: консультации Татьяны Мунн",
        "intent": "Пользователь ищет личную консультацию психолога, способ записи и понятные направления работы.",
        "hypothesis": "Разделение интентов взрослые/подростки/онлайн/Москва и один H1 должны улучшить релевантность коммерческих запросов.",
        "targetQueries": [
            "психолог подростку",
            "психолог онлайн",
            "психолог в Москве",
            "психолог МГУ",
            "консультация психолога Татьяна Мунн",
        ],
        "issues": ["multiple_h1_raw", "needs_cta_goal"],
        "allowedLiveChanges": ["seo_metadata", "rendered_h1", "faq_aeo_block", "click_goals"],
        "blockedLiveChanges": ["medical_claims", "guarantees", "prices"],
        "schemaTypes": ["ProfessionalService", "FAQPage", "BreadcrumbList"],
        "answerBlock": {
            "heading": "С чем можно обратиться",
            "items": [
                "Тревога, стресс, отношения, эмоциональное напряжение, подростковые сложности и вопросы родителей.",
                "Формат можно выбрать под задачу: очно в Москве или онлайн, если удобнее начать дистанционно.",
                "Первый шаг - коротко описать ситуацию и выбрать удобный способ записи.",
            ],
            "cta": "Выбрать время консультации",
            "ctaGoal": "moonn_seo_consult_booking",
        },
        "faq": [
            {
                "question": "Можно ли записаться онлайн?",
                "answer": "Да, консультацию можно провести онлайн или очно в Москве, если такой формат подходит вашей ситуации.",
            },
            {
                "question": "Работает ли Татьяна Мунн с подростками?",
                "answer": "Да, отдельный фокус сайта - подростки, родители, экзаменационный стресс, общение и уверенность.",
            },
        ],
    },
    {
        "key": "reviews",
        "url": "https://xn--l1acaw.xn--p1ai/otzivi",
        "alias": "otzivi",
        "sourcePageId": "81167556",
        "role": "trust",
        "funnelRole": "trust_to_lead",
        "priority": "P0",
        "title": "Отзывы о психологе Татьяне Мунн | проверяемые источники",
        "description": "Отзывы о психологе Татьяне Мунн: проверяемые источники, Яндекс Услуги, лекции, консультации и подтверждения опыта без искусственных рейтингов.",
        "targetH1": "Отзывы о психологе Татьяне Мунн",
        "intent": "Пользователь проверяет доверие перед записью на консультацию.",
        "hypothesis": "Страница отзывов должна поднимать доверие и переходы к записи, а не пытаться конкурировать как общая SEO-статья.",
        "targetQueries": [
            "Татьяна Мунн отзывы",
            "психолог Татьяна Мунн отзывы",
            "Татьяна Мунн Яндекс Услуги",
            "отзывы о психологе Татьяне Мунн",
        ],
        "issues": ["multiple_h1_raw", "raw_head_cleanup", "needs_trust_cta_goal"],
        "allowedLiveChanges": ["seo_metadata", "rendered_h1", "faq_aeo_block", "click_goals"],
        "blockedLiveChanges": ["fake_rating", "aggregate_rating", "full_review_mirror_without_gate"],
        "schemaTypes": ["ProfilePage", "ItemList", "FAQPage", "BreadcrumbList"],
        "answerBlock": {
            "heading": "Как проверять отзывы",
            "items": [
                "Смотрите не только текст отзыва, но и источник: Яндекс Услуги, мероприятия, публичные лекции и внешние профили.",
                "На странице сохраняется осторожная позиция: без искусственного рейтинга, накрученных чисел и неподтверждённых обещаний.",
                "Если отзывы совпадают с вашим запросом, следующий шаг - перейти к консультации или задать вопрос напрямую.",
            ],
            "cta": "Перейти к записи",
            "ctaGoal": "moonn_seo_reviews_to_booking",
        },
        "faq": [
            {
                "question": "Где проверить отзывы о Татьяне Мунн?",
                "answer": "Основной проверяемый внешний источник - профиль Татьяны Мунн на Яндекс Услугах, а также публичные страницы мероприятий и профили.",
            },
            {
                "question": "Почему на странице нет искусственного рейтинга?",
                "answer": "Рейтинг и aggregateRating не публикуются без отдельного legal/platform gate, чтобы не создавать неподтверждённые SEO-сигналы.",
            },
        ],
    },
]


def graph_for(page: dict) -> dict:
    url = page["url"]
    graph: list[dict] = [
        {
            "@type": "Person",
            "@id": PERSON_ID,
            "name": "Татьяна Мунн",
            "alternateName": ["Кумскова Татьяна Михайловна", "Татьяна Мунн (Кумскова)", "Tatiana Moonn"],
            "jobTitle": "Психолог МГУ, эксперт по эмоциональному интеллекту",
            "url": "https://xn--l1acaw.xn--p1ai/",
            "sameAs": [
                "https://xn--l1acaw.xn--p1ai/",
                "https://moonn.timepad.ru/events/",
                "https://miiiips.ru/author-tatyana-munn-kumskova.html",
                YANDEX_SERVICES_PROFILE,
                "https://istina.msu.ru/workers/816305440/",
                "https://psyjournals.ru/authors/15337",
            ],
            "knowsAbout": [
                "психология подростков",
                "эмоциональный интеллект",
                "тревога",
                "стресс перед экзаменом",
                "отношения",
                "саморегуляция",
            ],
        },
        {
            "@type": "WebSite",
            "@id": WEBSITE_ID,
            "url": "https://xn--l1acaw.xn--p1ai/",
            "name": "Татьяна Мунн",
            "publisher": {"@id": PERSON_ID},
            "inLanguage": "ru-RU",
        },
        {
            "@type": "WebPage",
            "@id": f"{url}#webpage",
            "url": url,
            "name": page["title"],
            "description": page["description"],
            "isPartOf": {"@id": WEBSITE_ID},
            "about": {"@id": PERSON_ID},
            "author": {"@id": PERSON_ID},
            "inLanguage": "ru-RU",
            "keywords": page["targetQueries"],
        },
        {
            "@type": "BreadcrumbList",
            "@id": f"{url}#breadcrumbs",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Главная", "item": "https://xn--l1acaw.xn--p1ai/"},
                {"@type": "ListItem", "position": 2, "name": page["targetH1"], "item": url},
            ],
        },
        {
            "@type": "FAQPage",
            "@id": f"{url}#faq",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": item["question"],
                    "acceptedAnswer": {"@type": "Answer", "text": item["answer"]},
                }
                for item in page["faq"]
            ],
        },
    ]

    if page["key"] == "teen_camp":
        graph.append(
            {
                "@type": "Event",
                "@id": f"{url}#event",
                "name": page["targetH1"],
                "url": url,
                "description": page["description"],
                "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
                "eventStatus": "https://schema.org/EventScheduled",
                "startDate": "2026-07-06",
                "endDate": "2026-07-10",
                "location": {
                    "@type": "Place",
                    "name": "Москва, Цветной бульвар",
                    "address": {"@type": "PostalAddress", "addressLocality": "Москва", "addressCountry": "RU"},
                },
                "organizer": {"@id": PERSON_ID},
                "performer": {"@id": PERSON_ID},
            }
        )
    elif page["key"] in {"exam_support", "consultations"}:
        graph.append(
            {
                "@type": "ProfessionalService",
                "@id": f"{url}#service",
                "name": page["targetH1"],
                "url": url,
                "provider": {"@id": PERSON_ID},
                "areaServed": ["Москва", "Онлайн"],
                "description": page["description"],
            }
        )
    elif page["key"] == "reviews":
        graph.append(
            {
                "@type": "ProfilePage",
                "@id": f"{url}#reviews-profile",
                "name": page["targetH1"],
                "url": url,
                "mainEntity": {"@id": PERSON_ID},
                "sameAs": YANDEX_SERVICES_PROFILE,
            }
        )
    elif page["key"] == "art_gallery":
        graph.append(
            {
                "@type": "CollectionPage",
                "@id": f"{url}#gallery",
                "name": page["targetH1"],
                "url": url,
                "about": {"@id": PERSON_ID},
                "description": page["description"],
            }
        )
    return {"@context": "https://schema.org", "@graph": graph}


def asset_payload() -> dict:
    return {
        "/" + page["alias"]: {
            "key": page["key"],
            "title": page["title"],
            "description": page["description"],
            "targetH1": page["targetH1"],
            "targetQueries": page["targetQueries"],
            "answerBlock": page["answerBlock"],
            "faq": page["faq"],
            "schema": graph_for(page),
        }
        for page in PAGES
    }


def build_asset_js() -> str:
    payload = json.dumps(asset_payload(), ensure_ascii=False, separators=(",", ":"))
    return f"""(function() {{
  var PAGES = {payload};
  var GOAL_COUNTER = 96397286;
  function normPath(path) {{
    path = path || "/";
    if (path.length > 1 && path.endsWith("/")) path = path.slice(0, -1);
    return path;
  }}
  function currentConfig() {{
    return PAGES[normPath(window.location.pathname || "/")] || null;
  }}
  function textNorm(value) {{
    return (value || "").replace(/\\s+/g, " ").trim().toLowerCase();
  }}
  function replaceTag(el, tag) {{
    if (!el || el.tagName.toLowerCase() === tag) return el;
    var next = document.createElement(tag);
    Array.prototype.slice.call(el.attributes || []).forEach(function(attr) {{ next.setAttribute(attr.name, attr.value); }});
    next.innerHTML = el.innerHTML;
    el.parentNode.replaceChild(next, el);
    return next;
  }}
  function setMeta(name, content) {{
    if (!content) return;
    var selector = name.indexOf("og:") === 0 ? 'meta[property="' + name + '"]' : 'meta[name="' + name + '"]';
    var attr = name.indexOf("og:") === 0 ? "property" : "name";
    var meta = document.querySelector(selector);
    if (!meta) {{
      meta = document.createElement("meta");
      meta.setAttribute(attr, name);
      document.head.appendChild(meta);
    }}
    meta.setAttribute("content", content);
  }}
  function setSchema(config) {{
    var script = document.getElementById("moonn-five-page-seo-schema-jsonld");
    if (!script) {{
      script = document.createElement("script");
      script.type = "application/ld+json";
      script.id = "moonn-five-page-seo-schema-jsonld";
      document.head.appendChild(script);
    }}
    script.text = JSON.stringify(config.schema);
    script.setAttribute("data-moonn-five-page-schema", config.key);
  }}
  function ensureSingleH1(config) {{
    var h1s = Array.prototype.slice.call(document.querySelectorAll("h1"));
    var keep = h1s.find(function(h) {{ return textNorm(h.textContent).indexOf(textNorm(config.targetH1).slice(0, 28)) !== -1; }});
    if (!keep) {{
      var candidates = Array.prototype.slice.call(document.querySelectorAll("h2,h3,.t-title,.t-heading,.tn-atom,[field='title'],[field='btitle']"));
      keep = candidates.find(function(el) {{ return textNorm(el.textContent).indexOf(textNorm(config.targetH1).slice(0, 18)) !== -1; }});
    }}
    if (!keep) {{
      var anchor = document.querySelector("#allrecords") || document.body;
      keep = document.createElement("h1");
      keep.textContent = config.targetH1;
      keep.className = "moonn-seo-main-h1";
      keep.setAttribute("data-moonn-seo-sprint", "h1");
      if (anchor.firstChild) anchor.insertBefore(keep, anchor.firstChild); else anchor.appendChild(keep);
    }} else {{
      keep = replaceTag(keep, "h1");
    }}
    Array.prototype.slice.call(document.querySelectorAll("h1")).forEach(function(h) {{
      if (h !== keep) replaceTag(h, "h2");
    }});
  }}
  function hidePlaceholders() {{
    var bad = ["Book design", "Your Name", "Your Email", "Html code will be here"];
    Array.prototype.slice.call(document.body.querySelectorAll("*")).forEach(function(node) {{
      if (!node.children.length) {{
        var text = (node.textContent || "").trim();
        if (bad.indexOf(text) !== -1) node.style.display = "none";
      }}
    }});
  }}
  function ensureImageAlts(config) {{
    var fallback = config.targetH1 + " - Татьяна Мунн";
    Array.prototype.slice.call(document.querySelectorAll("img")).forEach(function(img, index) {{
      var current = (img.getAttribute("alt") || "").trim();
      if (current) return;
      img.setAttribute("alt", fallback + (index ? " " + (index + 1) : ""));
      img.setAttribute("data-moonn-seo-alt", "auto");
    }});
  }}
  function ensureAnswerBlock(config) {{
    if (document.getElementById("moonn-five-page-answer-block")) return;
    var root = document.createElement("section");
    root.id = "moonn-five-page-answer-block";
    root.className = "moonn-five-page-answer-block";
    root.setAttribute("data-moonn-seo-sprint", config.key);
    var items = config.answerBlock.items.map(function(item) {{ return "<li>" + item + "</li>"; }}).join("");
    var faq = config.faq.map(function(item) {{
      return "<details><summary>" + item.question + "</summary><p>" + item.answer + "</p></details>";
    }}).join("");
    root.innerHTML =
      '<div class="moonn-five-page-answer-inner">' +
      '<p class="moonn-five-page-kicker">Коротко по запросу</p>' +
      '<h2>' + config.answerBlock.heading + '</h2>' +
      '<ul>' + items + '</ul>' +
      '<a class="moonn-five-page-cta" href="#moonn-contact" data-moonn-goal="' + config.answerBlock.ctaGoal + '">' + config.answerBlock.cta + '</a>' +
      '<div class="moonn-five-page-faq">' + faq + '</div>' +
      '</div>';
    var target = document.querySelector("main") || document.querySelector("#allrecords") || document.body;
    if (target.firstChild) target.insertBefore(root, target.firstChild.nextSibling); else target.appendChild(root);
  }}
  function bindGoals() {{
    if (document.documentElement.dataset.moonnFivePageGoals === "1") return;
    document.documentElement.dataset.moonnFivePageGoals = "1";
    document.addEventListener("click", function(event) {{
      var link = event.target && event.target.closest ? event.target.closest("a,button") : null;
      if (!link) return;
      var href = (link.getAttribute("href") || "").toLowerCase();
      var goal = link.getAttribute("data-moonn-goal") || "";
      if (!goal) {{
        if (href.indexOf("t.me/") !== -1 || href.indexOf("telegram") !== -1) goal = "moonn_seo_click_telegram";
        else if (href.indexOf("wa.me/") !== -1 || href.indexOf("whatsapp") !== -1) goal = "moonn_seo_click_whatsapp";
        else if (href.indexOf("yclients") !== -1 || href.indexOf("n461584") !== -1) goal = "moonn_seo_click_yclients";
        else if (href.indexOf("#order:") === 0) goal = "moonn_seo_click_tilda_order";
        else if (href.indexOf("uslugi.yandex.ru") !== -1) goal = "moonn_seo_click_yandex_reviews";
      }}
      if (goal && typeof window.ym === "function") {{
        try {{ window.ym(GOAL_COUNTER, "reachGoal", goal); }} catch (error) {{}}
      }}
    }}, true);
  }}
  function apply() {{
    var config = currentConfig();
    if (!config || !document.body) return;
    document.title = config.title;
    setMeta("description", config.description);
    setMeta("og:title", config.title);
    setMeta("og:description", config.description);
    setSchema(config);
    ensureSingleH1(config);
    hidePlaceholders();
    ensureImageAlts(config);
    ensureAnswerBlock(config);
    bindGoals();
  }}
  function installStyle() {{
    if (document.getElementById("moonn-five-page-seo-style")) return;
    var style = document.createElement("style");
    style.id = "moonn-five-page-seo-style";
    style.textContent = [
      ".moonn-seo-main-h1{{max-width:1120px;margin:24px auto 12px;padding:0 20px;font:700 42px/1.08 Inter,Arial,sans-serif;color:#172044;}}",
      ".moonn-five-page-answer-block{{padding:26px 0;background:#f8fbff;border-top:1px solid rgba(30,64,175,.10);border-bottom:1px solid rgba(30,64,175,.10);}}",
      ".moonn-five-page-answer-inner{{width:min(1120px,calc(100% - 32px));margin:0 auto;color:#172044;font-family:Inter,Arial,sans-serif;}}",
      ".moonn-five-page-kicker{{margin:0 0 8px;color:#3157b7;font-size:14px;font-weight:700;text-transform:uppercase;letter-spacing:.04em;}}",
      ".moonn-five-page-answer-inner h2{{margin:0 0 14px;font-size:28px;line-height:1.18;color:#172044;}}",
      ".moonn-five-page-answer-inner ul{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;margin:0 0 18px;padding:0;list-style:none;}}",
      ".moonn-five-page-answer-inner li{{border:1px solid rgba(30,64,175,.14);background:#fff;border-radius:8px;padding:14px 16px;font-size:16px;line-height:1.45;}}",
      ".moonn-five-page-cta{{display:inline-flex;align-items:center;justify-content:center;min-height:44px;padding:0 18px;border-radius:8px;background:#2348b7;color:#fff!important;text-decoration:none;font-weight:700;}}",
      ".moonn-five-page-faq{{margin-top:20px;display:grid;gap:10px;}}",
      ".moonn-five-page-faq details{{background:#fff;border:1px solid rgba(30,64,175,.14);border-radius:8px;padding:12px 14px;}}",
      ".moonn-five-page-faq summary{{cursor:pointer;font-weight:700;}}",
      ".moonn-five-page-faq p{{margin:10px 0 0;font-size:15px;line-height:1.5;color:#405070;}}",
      "@media(max-width:760px){{.moonn-seo-main-h1{{font-size:30px}}.moonn-five-page-answer-inner ul{{grid-template-columns:1fr}}.moonn-five-page-answer-inner h2{{font-size:23px}}}}"
    ].join("\\n");
    document.head.appendChild(style);
  }}
  function boot() {{
    installStyle();
    apply();
    var tries = 0;
    var timer = window.setInterval(function() {{
      tries += 1;
      apply();
      if (tries > 12) window.clearInterval(timer);
    }}, 700);
    if (window.MutationObserver && document.body) {{
      var observer = new MutationObserver(function() {{ apply(); }});
      observer.observe(document.body, {{childList: true, subtree: true}});
      window.setTimeout(function() {{ observer.disconnect(); }}, 12000);
    }}
  }}
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
  else boot();
  window.addEventListener("load", apply);
}})();
"""


def packet_payload() -> dict:
    return {
        "version": 1,
        "createdAt": datetime.now(timezone.utc).isoformat(),
        "project": "Moonn / Tatyana Munn site",
        "workstream": "Moonn SEO/AEO growth five-page sprint",
        "branch": "codex/moonn-seo-audit",
        "measurementContract": {
            "baseline": "Use GSC/Yandex.Metrika/Yandex Webmaster exports or GUI evidence before live edits.",
            "reviewWindows": ["T+3", "T+14", "T+28", "T+56"],
            "successMetric": "CTR >= 2.5-3% on target queries with 100+ impressions, plus tracked consultation/contact goals.",
        },
        "pages": [
            {
                **page,
                "seo": {
                    "title": page["title"],
                    "description": page["description"],
                    "canonical": page["url"],
                    "h1": {"targetH1": page["targetH1"], "action": "keep_or_render_single_h1"},
                    "imageAltPattern": f"{page['targetH1']} — Татьяна Мунн",
                },
                "jsonLd": graph_for(page),
            }
            for page in PAGES
        ],
    }


def ledger_payload() -> dict:
    now = datetime.now(timezone.utc).isoformat()
    return {
        "version": 1,
        "createdAt": now,
        "status": "baseline_and_change_contract_created",
        "sourceReport": "docs/moonn-seo-growth-check-2026-05-20.md",
        "pages": [
            {
                "url": page["url"],
                "pageId": page["sourcePageId"],
                "baselineDate": RUN_DATE,
                "hypothesis": page["hypothesis"],
                "targetQueries": page["targetQueries"],
                "changesPlanned": [
                    "seo_title_description_canonical",
                    "single_h1",
                    "faq_aeo_block",
                    "page_specific_schema",
                    "metrika_click_goals",
                ],
                "changesApplied": [],
                "reindexDate": None,
                "tPlus3": None,
                "tPlus14": None,
                "tPlus28": None,
                "tPlus56": None,
                "blockers": [
                    "Official API exports were blocked earlier; use Chrome Rublev GUI if API access is still unavailable.",
                    "Metrika page-level report was previously collapsed to homepage and needs separate verification.",
                ],
            }
            for page in PAGES
        ],
    }


def write_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_packet_md(payload: dict) -> None:
    lines = [
        f"# Moonn Five-Page SEO/AEO Packets — {RUN_DATE}",
        "",
        "- Branch: `codex/moonn-seo-audit`",
        "- Scope: five homepage-linked commercial/trust pages.",
        "- Safety: no price, payment-provider, legal text, personal data, fake rating or full review mirroring changes.",
        "",
        "## Pages",
        "",
    ]
    for page in payload["pages"]:
        lines.extend(
            [
                f"### {page['url']}",
                "",
                f"- Tilda page id: `{page['sourcePageId']}`",
                f"- Priority: `{page['priority']}`",
                f"- Funnel role: `{page['funnelRole']}`",
                f"- Title: `{page['seo']['title']}`",
                f"- Description: `{page['seo']['description']}`",
                f"- Canonical: `{page['seo']['canonical']}`",
                f"- H1: `{page['seo']['h1']['targetH1']}`",
                f"- Target queries: {', '.join('`' + q + '`' for q in page['targetQueries'])}",
                f"- Schema types: {', '.join('`' + t + '`' for t in page['schemaTypes'])}",
                f"- Allowed: {', '.join('`' + t + '`' for t in page['allowedLiveChanges'])}",
                f"- Blocked: {', '.join('`' + t + '`' for t in page['blockedLiveChanges'])}",
                "",
            ]
        )
    PACKET_MD.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_ledger_md(payload: dict) -> None:
    lines = [
        f"# Moonn Five-Page SEO Change Ledger — {RUN_DATE}",
        "",
        "Append-only ledger for measuring SEO/AEO changes against GSC, Yandex.Metrika and Yandex Webmaster.",
        "",
        "## Review Windows",
        "",
        "- T0: baseline before live edits.",
        "- T+3: technical/live verification.",
        "- T+14: early impressions/CTR movement.",
        "- T+28: CTR/click assessment.",
        "- T+56: scale or pivot decision.",
        "",
        "## Entries",
        "",
    ]
    for page in payload["pages"]:
        lines.extend(
            [
                f"### {page['url']}",
                "",
                f"- Tilda page id: `{page['pageId']}`",
                f"- Baseline date: `{page['baselineDate']}`",
                f"- Hypothesis: {page['hypothesis']}",
                f"- Target queries: {', '.join('`' + q + '`' for q in page['targetQueries'])}",
                "- Changes planned: `seo_title_description_canonical`, `single_h1`, `faq_aeo_block`, `page_specific_schema`, `metrika_click_goals`",
                "- Changes applied: pending live publication",
                "- Reindex date: pending",
                "- T+3/T+14/T+28/T+56: pending",
                "",
            ]
        )
    LEDGER_MD.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_csvs(packet: dict, ledger: dict) -> None:
    with PACKET_CSV.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=[
                "url",
                "pageId",
                "priority",
                "role",
                "funnelRole",
                "title",
                "description",
                "h1",
                "targetQueries",
                "schemaTypes",
            ],
        )
        writer.writeheader()
        for page in packet["pages"]:
            writer.writerow(
                {
                    "url": page["url"],
                    "pageId": page["sourcePageId"],
                    "priority": page["priority"],
                    "role": page["role"],
                    "funnelRole": page["funnelRole"],
                    "title": page["seo"]["title"],
                    "description": page["seo"]["description"],
                    "h1": page["seo"]["h1"]["targetH1"],
                    "targetQueries": " | ".join(page["targetQueries"]),
                    "schemaTypes": " | ".join(page["schemaTypes"]),
                }
            )
    with LEDGER_CSV.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=[
                "url",
                "pageId",
                "baselineDate",
                "hypothesis",
                "targetQueries",
                "changesApplied",
                "reindexDate",
                "tPlus3",
                "tPlus14",
                "tPlus28",
                "tPlus56",
            ],
        )
        writer.writeheader()
        for page in ledger["pages"]:
            writer.writerow(
                {
                    "url": page["url"],
                    "pageId": page["pageId"],
                    "baselineDate": page["baselineDate"],
                    "hypothesis": page["hypothesis"],
                    "targetQueries": " | ".join(page["targetQueries"]),
                    "changesApplied": " | ".join(page["changesApplied"]),
                    "reindexDate": page["reindexDate"] or "",
                    "tPlus3": page["tPlus3"] or "",
                    "tPlus14": page["tPlus14"] or "",
                    "tPlus28": page["tPlus28"] or "",
                    "tPlus56": page["tPlus56"] or "",
                }
            )


def write_head_snippet() -> None:
    HEAD_SNIPPET.write_text(
        "\n".join(
            [
                "<!-- moonn-five-page-seo-sprint-layer:start -->",
                '<script defer src="https://cdn.jsdelivr.net/gh/rublevalexandermsu-design/moonn-psy-pages@__COMMIT__/assets/moonn-five-page-seo-sprint-layer.js"></script>',
                "<!-- moonn-five-page-seo-sprint-layer:end -->",
            ]
        )
        + "\n",
        encoding="utf-8",
    )


def main() -> int:
    DOCS.mkdir(exist_ok=True)
    ASSETS.mkdir(exist_ok=True)
    packet = packet_payload()
    ledger = ledger_payload()
    write_json(PACKET_JSON, packet)
    write_json(LEDGER_JSON, ledger)
    write_packet_md(packet)
    write_ledger_md(ledger)
    write_csvs(packet, ledger)
    REINDEX_TXT.write_text("\n".join(page["url"] for page in PAGES) + "\n", encoding="utf-8")
    ASSET_JS.write_text(build_asset_js(), encoding="utf-8")
    write_head_snippet()
    print(
        json.dumps(
            {
                "packet": str(PACKET_JSON.relative_to(ROOT)),
                "ledger": str(LEDGER_JSON.relative_to(ROOT)),
                "asset": str(ASSET_JS.relative_to(ROOT)),
                "pages": len(PAGES),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

