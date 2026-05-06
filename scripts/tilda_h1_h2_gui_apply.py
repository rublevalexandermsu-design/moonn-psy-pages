import argparse
import json
import time
from pathlib import Path

from pywinauto import Desktop, mouse
from pywinauto.keyboard import send_keys


PROJECT_ID = "8326812"


def chrome_window():
    candidates = []
    for window in Desktop(backend="uia").windows(title_re=".*Google Chrome.*"):
        try:
            address = address_bar(window).window_text()
        except Exception:
            address = ""
        candidates.append((window, address))
    for window, address in candidates:
        title = window.window_text()
        if "tilda.ru" in address and ("Moonn.ru" in title or "Tilda" in title):
            window.restore()
            window.set_focus()
            time.sleep(0.5)
            return window
    for window, address in candidates:
        if "tilda.ru" in address:
            window.restore()
            window.set_focus()
            time.sleep(0.5)
            return window
    raise RuntimeError("Authenticated Google Chrome Tilda window not found")


def address_bar(win):
    for edit in win.descendants(control_type="Edit"):
        try:
            if edit.element_info.automation_id == "view_1012":
                return edit
        except Exception:
            continue
    edits = win.descendants(control_type="Edit")
    if edits:
        return edits[0]
    raise RuntimeError("Chrome address bar edit control not found")


def navigate(win, page_id: str, rec_id: str):
    url = f"https://tilda.ru/page/?pageid={page_id}&projectid={PROJECT_ID}#rec{rec_id}"
    win.set_focus()
    bar = address_bar(win)
    bar.set_focus()
    bar.set_edit_text(url)
    send_keys("{ENTER}")
    time.sleep(6.0)


def find_button(win, name: str, predicate):
    candidates = []
    for element in win.descendants(control_type="Button"):
        try:
            if name not in (element.window_text() or ""):
                continue
            rect = element.rectangle()
            if predicate(rect):
                candidates.append(element)
        except Exception:
            continue
    if not candidates:
        return None
    return sorted(candidates, key=lambda item: (item.rectangle().top, item.rectangle().left))[0]


def open_block_settings(win):
    # The block-level Settings button is on the left side; page-level Settings is on the top right.
    for _ in range(4):
        button = find_button(
            win,
            "Настройки",
            lambda rect: rect.left < 420 and 120 < rect.top < 420,
        )
        if button:
            button.click_input()
            time.sleep(1.0)
            return True
        mouse.move(coords=(150, 260))
        time.sleep(0.2)
        mouse.click(button="left", coords=(95, 270))
        time.sleep(0.4)
    return False


def choose_heading_tag(win, tag: str):
    # Scroll the left settings panel until the SEO heading-tag field is visible near the bottom.
    for _ in range(9):
        combos = []
        for element in win.descendants(control_type="ComboBox"):
            rect = element.rectangle()
            if rect.left < 260 and rect.top > 250:
                combos.append(element)
        if combos:
            combo = sorted(combos, key=lambda item: item.rectangle().top)[-1]
            combo.click_input()
            time.sleep(0.4)
            option = None
            for element in win.descendants(control_type="ListItem"):
                if element.window_text().strip().upper() == tag.upper():
                    option = element
                    break
            if option:
                option.click_input()
                time.sleep(0.5)
                return True
        mouse.scroll(coords=(120, 760), wheel_dist=-5)
        time.sleep(0.5)
    return False


def save_and_close_settings(win):
    button = find_button(
        win,
        "Сохранить и закрыть",
        lambda rect: rect.left < 420 and rect.top < 230,
    )
    if not button:
        return False
    button.click_input()
    time.sleep(2.0)
    return True


def publish_page(win):
    button = find_button(
        win,
        "Опубликовать",
        lambda rect: rect.left > 900 and rect.top < 240,
    )
    if not button:
        return False
    button.click_input()
    time.sleep(5.0)
    # Close the published-link popup if it is present. Do not open the public page here.
    close_button = find_button(
        win,
        "Закрыть",
        lambda rect: 1100 < rect.left < 1500 and 220 < rect.top < 380,
    )
    if close_button:
        close_button.click_input()
        time.sleep(0.7)
    return True


def apply_action(win, action: dict) -> dict:
    result = {
        "url": action["url"],
        "pageId": action["pageId"],
        "recId": action["recId"],
        "setTag": action["setTag"],
        "visibleSignal": action.get("visibleSignal"),
        "status": "started",
    }
    navigate(win, action["pageId"], action["recId"])
    if not open_block_settings(win):
        result["status"] = "failed"
        result["error"] = "block_settings_button_not_found"
        return result
    if not choose_heading_tag(win, action["setTag"]):
        result["status"] = "failed"
        result["error"] = "heading_tag_field_not_found"
        return result
    if not save_and_close_settings(win):
        result["status"] = "failed"
        result["error"] = "save_and_close_not_found"
        return result
    if not publish_page(win):
        result["status"] = "failed"
        result["error"] = "publish_button_not_found"
        return result
    result["status"] = "applied_and_published"
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Apply Moonn H1/H2 block tags through the real Chrome Tilda UI.")
    parser.add_argument("--plan", default="docs/moonn-h1-h2-ui-apply-plan-2026-05-06.json")
    parser.add_argument("--report", default="docs/moonn-h1-h2-ui-apply-report-2026-05-06.json")
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--limit", type=int, default=0)
    args = parser.parse_args()

    plan = json.loads(Path(args.plan).read_text(encoding="utf-8"))
    actions = plan["actions"][args.start :]
    if args.limit:
        actions = actions[: args.limit]
    win = chrome_window()
    results = []
    for index, action in enumerate(actions, start=args.start + 1):
        print(f"[{index}/{len(plan['actions'])}] {action['setTag']} {action['url']} rec{action['recId']}")
        try:
            result = apply_action(win, action)
        except Exception as error:
            result = {
                "url": action["url"],
                "pageId": action["pageId"],
                "recId": action["recId"],
                "setTag": action["setTag"],
                "status": "failed",
                "error": repr(error),
            }
        print(json.dumps(result, ensure_ascii=False))
        results.append(result)
        Path(args.report).write_text(
            json.dumps(
                {
                    "version": 1,
                    "createdAt": "2026-05-06",
                    "sourcePlan": args.plan,
                    "start": args.start,
                    "limit": args.limit,
                    "results": results,
                },
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        if result["status"] != "applied_and_published":
            break
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
