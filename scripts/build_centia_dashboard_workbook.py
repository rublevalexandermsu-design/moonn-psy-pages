from __future__ import annotations

import json
import re
from pathlib import Path

from openpyxl import Workbook
from openpyxl.chart import BarChart, PieChart, Reference
from openpyxl.formatting.rule import FormulaRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation


ROOT = Path(__file__).resolve().parents[1]
CONTEXT_PATH = Path(r"C:\Users\yanta\Downloads\centia_chat_context_for_codex.json")
MANIFEST_PATH = ROOT / "docs" / "centia-tilda" / "tilda-pages-manifest.json"
OUTPUT_PATH = ROOT / "output" / "centia-studio-dashboard-2026-05-24.xlsx"

GREEN = "294633"
DEEP = "172015"
GOLD = "C8A45D"
SURFACE = "F8F5ED"
LIGHT_GREEN = "E6EEE6"
LIGHT_GOLD = "F2E7CC"
WHITE = "FFFFFF"
MUTED = "66715F"
RED = "C75D4D"
YELLOW = "F7D46A"


def clean_price(value: str) -> int:
    numbers = [int(re.sub(r"\D", "", part)) for part in re.findall(r"\d[\d\s]*", value)]
    if not numbers:
        return 0
    return max(numbers)


def setup_sheet(ws, title: str, subtitle: str = "") -> None:
    ws.sheet_view.showGridLines = False
    ws.freeze_panes = "A4"
    ws["A1"] = title
    ws["A1"].font = Font(name="Arial", size=18, bold=True, color=WHITE)
    ws["A1"].fill = PatternFill("solid", fgColor=GREEN)
    ws["A1"].alignment = Alignment(vertical="center")
    ws.row_dimensions[1].height = 30
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=8)
    if subtitle:
        ws["A2"] = subtitle
        ws["A2"].font = Font(name="Arial", size=10, color=MUTED)
        ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=8)
    for col in range(1, 13):
        ws.column_dimensions[get_column_letter(col)].width = 18


def style_table(ws, header_row: int, first_col: int, last_col: int, last_row: int) -> None:
    thin = Side(style="thin", color="D8D2C3")
    for cell in ws[header_row][first_col - 1 : last_col]:
        cell.font = Font(name="Arial", bold=True, color=WHITE)
        cell.fill = PatternFill("solid", fgColor=GREEN)
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = Border(top=thin, bottom=thin, left=thin, right=thin)
    for row in ws.iter_rows(min_row=header_row + 1, max_row=last_row, min_col=first_col, max_col=last_col):
        for cell in row:
            cell.fill = PatternFill("solid", fgColor=WHITE)
            cell.border = Border(top=thin, bottom=thin, left=thin, right=thin)
            cell.alignment = Alignment(vertical="top", wrap_text=True)


def set_widths(ws, widths: dict[str, int]) -> None:
    for col, width in widths.items():
        ws.column_dimensions[col].width = width


def add_status_validation(ws, cell_range: str) -> None:
    dv = DataValidation(type="list", formula1='"Не начато,В работе,Готово,Блокер,Ожидает"', allow_blank=True)
    ws.add_data_validation(dv)
    dv.add(cell_range)


def add_priority_validation(ws, cell_range: str) -> None:
    dv = DataValidation(type="list", formula1='"P0,P1,P2,P3"', allow_blank=True)
    ws.add_data_validation(dv)
    dv.add(cell_range)


def add_status_rules(ws, cell_range: str) -> None:
    ws.conditional_formatting.add(
        cell_range,
        FormulaRule(formula=[f'EXACT({cell_range.split(":")[0]},"Готово")'], fill=PatternFill("solid", fgColor=LIGHT_GREEN)),
    )
    ws.conditional_formatting.add(
        cell_range,
        FormulaRule(formula=[f'EXACT({cell_range.split(":")[0]},"Блокер")'], fill=PatternFill("solid", fgColor="F4C7C3")),
    )
    ws.conditional_formatting.add(
        cell_range,
        FormulaRule(formula=[f'EXACT({cell_range.split(":")[0]},"В работе")'], fill=PatternFill("solid", fgColor=LIGHT_GOLD)),
    )


def main() -> None:
    context = json.loads(CONTEXT_PATH.read_text(encoding="utf-8"))
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    programs = context["start_program_lineup"]
    pricing = context["pricing_model_discussed"]
    schedule = context["schedule_strategy"]["recommended_weekly_schedule"]
    channels = context["marketing_plan_discussed"]["channels"]

    wb = Workbook()
    default = wb.active
    wb.remove(default)

    dashboard = wb.create_sheet("00 Dashboard")
    goals = wb.create_sheet("01 Цели KPI")
    funnel = wb.create_sheet("02 Воронка")
    programs_ws = wb.create_sheet("03 Программы")
    schedule_ws = wb.create_sheet("04 Расписание")
    revenue = wb.create_sheet("05 Выручка")
    tasks = wb.create_sheet("06 Задачи запуска")
    seo = wb.create_sheet("07 Контент SEO")
    marketing = wb.create_sheet("08 Маркетинг")
    crm = wb.create_sheet("09 CRM заявки")
    room = wb.create_sheet("10 Пространство")
    incidents = wb.create_sheet("11 Инциденты")
    sources = wb.create_sheet("12 Источники")

    setup_sheet(dashboard, "Центия: операционный дашборд запуска", "Google Sheets слой управления студией у Марьиной Рощи")
    dashboard["A4"] = "KPI"
    dashboard["B4"] = "Значение"
    dashboard["C4"] = "Комментарий"
    kpis = [
        ("Live страниц", '=COUNTIF(\'07 Контент SEO\'!G:G,"Live")', "Все Tilda-страницы должны быть опубликованы"),
        ("Заполнение групп", '=TEXT(AVERAGE(\'05 Выручка\'!H4:H9),"0%")', "Средний план заполнения"),
        ("Плановая выручка/мес", '=SUM(\'05 Выручка\'!I4:I9)', "При текущих ценах и заполнении"),
        ("Готовность задач", '=TEXT(COUNTIF(\'06 Задачи запуска\'!E:E,"Готово")/COUNTA(\'06 Задачи запуска\'!A4:A100),"0%")', "По задачам запуска"),
        ("Блокеры", '=COUNTIF(\'06 Задачи запуска\'!E:E,"Блокер")+COUNTIF(\'11 Инциденты\'!E:E,"Открыт")', "Открытые риски"),
    ]
    for idx, row in enumerate(kpis, start=5):
        for col, value in enumerate(row, start=1):
            dashboard.cell(idx, col, value)
    style_table(dashboard, 4, 1, 3, 9)
    set_widths(dashboard, {"A": 24, "B": 22, "C": 48, "E": 22, "F": 18, "G": 18, "H": 18})
    dashboard["E4"] = "Принцип из ролика"
    dashboard["E5"] = "Убрать хаос через один дашборд: задачи, бизнес, контент и деньги видны на одной панели."
    dashboard["E5"].alignment = Alignment(wrap_text=True, vertical="top")
    dashboard["E5"].fill = PatternFill("solid", fgColor=LIGHT_GOLD)
    dashboard["E5"].border = Border(left=Side(style="thin", color="D8D2C3"), right=Side(style="thin", color="D8D2C3"), top=Side(style="thin", color="D8D2C3"), bottom=Side(style="thin", color="D8D2C3"))

    setup_sheet(goals, "Цели и KPI", "Контроль запуска, продаж и качества")
    goals_rows = [
        ["Цель", "Метрика", "Целевое значение", "Текущий статус", "Период", "Источник"],
        ["Запустить сайт", "12 live-страниц", "12", "Готово", "май 2026", "Tilda + manifest"],
        ["Набрать первые группы", "Брони мест", "30+", "В работе", "июнь-сентябрь", "CRM заявки"],
        ["Выйти на стартовую выручку", "Грязная выручка/мес", "350 000-500 000 ₽", "План", "сентябрь-октябрь", "Контекст проекта"],
        ["Сделать маркетинг управляемым", "Каналы с UTM и лид-учётом", "8+", "В работе", "июнь", "Маркетинг"],
        ["Держать публикации чистыми", "Ошибки live/404", "0", "Готово", "постоянно", "QA"],
    ]
    for row in goals_rows:
        goals.append(row)
    style_table(goals, 3, 1, 6, goals.max_row)
    set_widths(goals, {"A": 30, "B": 28, "C": 22, "D": 16, "E": 18, "F": 24})

    setup_sheet(funnel, "Воронка запуска", "От канала до абонемента")
    funnel_rows = [
        ["Канал", "Охват", "Переходы", "Лиды", "Пробные", "Брони", "Абонементы", "Конверсия лид->бронь", "Комментарий"],
        ["Яндекс Бизнес / Карты", 0, 0, 0, 0, 0, 0, '=IF(D2=0,"",F2/D2)', "Гео-спрос рядом с Марьиной Рощей"],
        ["2ГИС", 0, 0, 0, 0, 0, 0, '=IF(D3=0,"",F3/D3)', "Локальная выдача"],
        ["Timepad", 0, 0, 0, 0, 0, 0, '=IF(D4=0,"",F4/D4)', "События и лекции"],
        ["Локальные чаты", 0, 0, 0, 0, 0, 0, '=IF(D5=0,"",F5/D5)', "Районные родители"],
        ["VK", 0, 0, 0, 0, 0, 0, '=IF(D6=0,"",F6/D6)', "Посты и таргет"],
        ["Яндекс Директ", 0, 0, 0, 0, 0, 0, '=IF(D7=0,"",F7/D7)', "Платный тест"],
        ["Новая Лига", 0, 0, 0, 0, 0, 0, '=IF(D8=0,"",F8/D8)', "Внутренняя аудитория клуба"],
    ]
    for row in funnel_rows:
        funnel.append(row)
    style_table(funnel, 3, 1, 9, funnel.max_row)
    set_widths(funnel, {"A": 28, "B": 12, "C": 12, "D": 12, "E": 12, "F": 12, "G": 14, "H": 20, "I": 34})
    for row in range(4, funnel.max_row + 1):
        funnel[f"H{row}"].number_format = "0%"

    setup_sheet(programs_ws, "Программы", "Линейка групп и продуктовые параметры")
    programs_ws.append(["ID", "Программа", "Аудитория", "Формат", "Длительность", "Частота", "Размер группы", "Страница", "Сообщение"])
    for program in programs:
        programs_ws.append([
            program["id"],
            program["name"],
            program["audience"],
            program["format"],
            program["duration"],
            program["frequency"],
            program["group_size"],
            "https://moonn.ru/" + next((p["recommended_alias"] for p in manifest["pages"] if p["source"].endswith(program["page"])), ""),
            program["core_message"],
        ])
    style_table(programs_ws, 3, 1, 9, programs_ws.max_row)
    set_widths(programs_ws, {"A": 28, "B": 34, "C": 26, "D": 30, "E": 16, "F": 18, "G": 16, "H": 38, "I": 58})

    setup_sheet(schedule_ws, "Расписание", "Стартовое расписание сентября-октября")
    schedule_ws.append(["День", "Время", "Программа", "Тип", "Статус", "Комментарий"])
    for item in schedule:
        schedule_ws.append([item["day"], item["time"], item["program"], "Регулярная группа", "План", ""])
    for weekend in context["schedule_strategy"]["weekend_use"]:
        schedule_ws.append(["Суббота/воскресенье", "11:00-18:00", weekend, "Событие", "Идея", "Заполнять после выбора дат"])
    style_table(schedule_ws, 3, 1, 6, schedule_ws.max_row)
    set_widths(schedule_ws, {"A": 22, "B": 16, "C": 46, "D": 22, "E": 14, "F": 38})

    setup_sheet(revenue, "Выручка", "Плановая экономика групп")
    revenue.append(["Программа", "Аудитория", "Мест", "Цена абонемента", "Цена пробной", "Частота", "План заполнения", "Заполнение %", "Плановая выручка", "Комментарий"])
    price_map = {
        "children_7_10_emotions_communication": pricing["children_7_10"],
        "teens_11_13_confidence": pricing["teens"],
        "teens_14_16_selfesteem_anxiety_communication": pricing["teens"],
        "teens_15_17_stress_exams_future": pricing["teens"],
        "parent_club": pricing["parent_club"],
        "adults_stress_burnout_selfregulation": pricing["adults"],
    }
    for idx, program in enumerate(programs, start=4):
        prices = price_map[program["id"]]
        monthly = clean_price(prices.get("monthly", prices.get("one_time", "0")))
        trial = clean_price(prices.get("trial", prices.get("one_time", "0")))
        seats = max([int(n) for n in re.findall(r"\d+", program["group_size"])])
        revenue.append([program["name"], program["audience"], seats, monthly, trial, program["frequency"], round(seats * 0.7), f"=G{idx}/C{idx}", f"=G{idx}*D{idx}", program["core_message"]])
    style_table(revenue, 3, 1, 10, revenue.max_row)
    set_widths(revenue, {"A": 34, "B": 26, "C": 10, "D": 18, "E": 16, "F": 18, "G": 16, "H": 14, "I": 18, "J": 48})
    for row in range(4, revenue.max_row + 1):
        revenue[f"D{row}"].number_format = '#,##0 "₽"'
        revenue[f"E{row}"].number_format = '#,##0 "₽"'
        revenue[f"H{row}"].number_format = "0%"
        revenue[f"I{row}"].number_format = '#,##0 "₽"'

    chart = BarChart()
    chart.title = "Плановая выручка по программам"
    chart.y_axis.title = "₽ / месяц"
    chart.x_axis.title = "Программа"
    data = Reference(revenue, min_col=9, min_row=3, max_row=revenue.max_row)
    cats = Reference(revenue, min_col=1, min_row=4, max_row=revenue.max_row)
    chart.add_data(data, titles_from_data=True)
    chart.set_categories(cats)
    chart.height = 8
    chart.width = 18
    revenue.add_chart(chart, "L2")

    setup_sheet(tasks, "Задачи запуска", "Единый task tracker студии")
    task_rows = [
        ["Направление", "Задача", "Ответственный", "Приоритет", "Статус", "Дедлайн", "Следующее действие", "Артефакт"],
        ["Сайт", "Проверить все live URL и кнопки", "Codex", "P0", "Готово", "2026-05-24", "Мониторить при изменениях", "https://moonn.ru/fnt"],
        ["Сайт", "Поддерживать 12 страниц без 404", "Codex", "P0", "Готово", "2026-05-24", "Добавить в регулярный QA", "manifest"],
        ["Бронь", "Выбрать финальную механику заявки/оплаты", "Татьяна/команда", "P0", "В работе", "2026-06-05", "Решить YCLIENTS/Timepad/форма", "Бронь"],
        ["CRM", "Вести все заявки в листе CRM", "Администратор", "P0", "Не начато", "2026-06-01", "Назначить ответственного", "09 CRM заявки"],
        ["Маркетинг", "Запустить карточки Яндекс/2ГИС", "Маркетинг", "P1", "Не начато", "2026-06-10", "Подготовить фото и описания", "08 Маркетинг"],
        ["Маркетинг", "Собрать первые события Timepad", "Маркетинг", "P1", "Не начато", "2026-06-12", "Выбрать 2 лекции", "02 Воронка"],
        ["Контент", "Сделать контент-план на 4 недели", "Контент", "P1", "В работе", "2026-06-03", "Утвердить рубрики", "07 Контент SEO"],
        ["Операции", "Закупить мебель первого этапа", "Команда", "P1", "Не начато", "2026-07-01", "Сверить бюджет", "10 Пространство"],
        ["Legal", "Проверить формы, оферту, согласие", "Ответственный", "P0", "В работе", "2026-06-15", "Связать с формой заявки", "Compliance"],
        ["Финансы", "Обновлять план/факт выручки еженедельно", "Администратор", "P1", "Не начато", "еженедельно", "Ввести факт продаж", "05 Выручка"],
    ]
    for row in task_rows:
        tasks.append(row)
    style_table(tasks, 3, 1, 8, tasks.max_row)
    set_widths(tasks, {"A": 18, "B": 40, "C": 18, "D": 12, "E": 14, "F": 14, "G": 42, "H": 26})
    add_status_validation(tasks, f"E4:E{tasks.max_row}")
    add_priority_validation(tasks, f"D4:D{tasks.max_row}")
    add_status_rules(tasks, f"E4:E{tasks.max_row}")

    setup_sheet(seo, "Контент и SEO", "Live-страницы, статусы, canonical")
    seo.append(["Страница", "Title", "Description", "Alias", "URL", "Тип", "Статус", "Следующая проверка"])
    for item in manifest["pages"]:
        page_type = "Главная" if item["recommended_alias"] == "fnt" else "Посадочная"
        seo.append([
            item["source"].replace("dist/centia/", ""),
            item["title"],
            item["description"],
            item["recommended_alias"],
            "https://moonn.ru/" + item["recommended_alias"],
            page_type,
            "Live",
            "после правок контента",
        ])
    style_table(seo, 3, 1, 8, seo.max_row)
    set_widths(seo, {"A": 24, "B": 42, "C": 58, "D": 24, "E": 42, "F": 14, "G": 12, "H": 24})
    add_status_validation(seo, f"G4:G{seo.max_row}")

    setup_sheet(marketing, "Маркетинг", "Каналы, офферы и UTM")
    marketing.append(["Канал", "Главный оффер", "URL/место", "KPI", "Статус", "Комментарий"])
    offers = context["marketing_plan_discussed"]["content_offers"]
    for idx, channel in enumerate(channels):
        marketing.append([channel, offers[idx % len(offers)], "", "Лиды / брони", "Не начато", ""])
    style_table(marketing, 3, 1, 6, marketing.max_row)
    set_widths(marketing, {"A": 30, "B": 48, "C": 28, "D": 20, "E": 14, "F": 34})
    add_status_validation(marketing, f"E4:E{marketing.max_row}")

    setup_sheet(crm, "CRM заявки", "Единая таблица лидов и оплат")
    crm.append(["Дата", "Имя", "Контакт", "Сегмент", "Источник", "Интерес", "Статус", "Следующий шаг", "Ответственный", "Сумма", "Комментарий"])
    for row in range(2, 42):
        crm.append(["", "", "", "", "", "", "Новый", "", "", "", ""])
    style_table(crm, 3, 1, 11, crm.max_row)
    set_widths(crm, {"A": 14, "B": 20, "C": 26, "D": 26, "E": 22, "F": 34, "G": 16, "H": 34, "I": 18, "J": 14, "K": 38})
    dv_crm = DataValidation(type="list", formula1='"Новый,Связаться,Пробная,Бронь,Оплатил,Отказ,Пауза"', allow_blank=True)
    crm.add_data_validation(dv_crm)
    dv_crm.add(f"G4:G{crm.max_row}")
    for row in range(4, crm.max_row + 1):
        crm[f"J{row}"].number_format = '#,##0 "₽"'

    setup_sheet(room, "Пространство", "Помещение, закупки и форматы")
    room.append(["Категория", "Позиция/факт", "Количество/размер", "Статус", "Комментарий"])
    room.append(["Помещение", "Площадь", context["room_and_interior"]["room_size"], "Факт", ""])
    for item in context["room_and_interior"]["furniture_plan"]:
        room.append(["Закупки", item, "", "План", ""])
    for item in context["room_and_interior"]["transformable_formats"]:
        room.append(["Формат", item, "", "План", ""])
    style_table(room, 3, 1, 5, room.max_row)
    set_widths(room, {"A": 18, "B": 44, "C": 24, "D": 14, "E": 40})

    setup_sheet(incidents, "Инциденты", "Ошибки, причины и правила")
    incident_rows = [
        ["Дата", "Симптом", "Root cause", "Решение", "Статус", "Follow-up rule"],
        ["2026-05-24", "Tilda T153/SoundCloud вместо HTML", "Перепутан tplid 123 с блоком T123", "Использовать tplid 131", "Закрыт", "Перед добавлением блока проверять template registry"],
        ["2026-05-24", "Внутренние ссылки вели на 404", "Была опубликована только /fnt, не все manifest aliases", "Созданы и опубликованы 12 Tilda pages", "Закрыт", "Multi-page done только после проверки всех alias"],
        ["2026-05-24", "Шрифт выглядел слишком крупным", "Генератор держал слишком агрессивные clamp/vw", "Снижены display font-size overrides", "Закрыт", "Перед публикацией нужен visual QA на 100% zoom"],
    ]
    for row in incident_rows:
        incidents.append(row)
    style_table(incidents, 3, 1, 6, incidents.max_row)
    set_widths(incidents, {"A": 14, "B": 36, "C": 44, "D": 42, "E": 14, "F": 48})

    setup_sheet(sources, "Источники", "Provenance и что обновлять")
    source_rows = [
        ["Источник", "Проверено", "Что взято", "URL/путь", "Обновлять когда"],
        ["YouTube Shorts / RITM", "2026-05-24", "Идея шаблонов Google Sheets для устранения хаоса", "https://youtube.com/shorts/dgpCSYY6P6I", "при смене референса"],
        ["YouTube oEmbed", "2026-05-24", "Название ролика и канал RITM", "https://www.youtube.com/oembed?url=https://youtube.com/shorts/dgpCSYY6P6I&format=json", "если ролик удалён/изменён"],
        ["Centia context JSON", "2026-05-24", "Программы, цены, расписание, маркетинг, помещение", str(CONTEXT_PATH), "при новом контексте чата"],
        ["Tilda manifest", "2026-05-24", "12 страниц, titles, descriptions, aliases", str(MANIFEST_PATH), "при изменении страниц"],
        ["Live site", "2026-05-24", "Опубликованные URL", "https://moonn.ru/fnt", "после каждой публикации"],
    ]
    for row in source_rows:
        sources.append(row)
    style_table(sources, 3, 1, 5, sources.max_row)
    set_widths(sources, {"A": 26, "B": 16, "C": 44, "D": 68, "E": 30})

    pie_data_start = tasks.max_row + 3
    tasks[f"A{pie_data_start}"] = "Статус"
    tasks[f"B{pie_data_start}"] = "Количество"
    for offset, status in enumerate(["Готово", "В работе", "Не начато", "Блокер", "Ожидает"], start=1):
        tasks[f"A{pie_data_start + offset}"] = status
        tasks[f"B{pie_data_start + offset}"] = f'=COUNTIF(E:E,A{pie_data_start + offset})'
    pie = PieChart()
    pie.title = "Статусы задач"
    pie.add_data(Reference(tasks, min_col=2, min_row=pie_data_start, max_row=pie_data_start + 5), titles_from_data=True)
    pie.set_categories(Reference(tasks, min_col=1, min_row=pie_data_start + 1, max_row=pie_data_start + 5))
    pie.height = 7
    pie.width = 10
    tasks.add_chart(pie, "J2")

    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for cell in row:
                cell.font = cell.font.copy(name="Arial")
                cell.alignment = cell.alignment.copy(wrap_text=True, vertical=cell.alignment.vertical or "top")
        ws.auto_filter.ref = ws.dimensions if ws.max_row > 1 and ws.max_column > 1 else None

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    wb.save(OUTPUT_PATH)
    print(OUTPUT_PATH)


if __name__ == "__main__":
    main()
