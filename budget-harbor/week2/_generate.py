#!/usr/bin/env python3
"""Budget Harbor Co — Christmas drop (Nov 15 & 17) + Week 2 drafts (Nov 23–29).

Reuses week-1 slide templates (hook, content, statement, mockup, still, CTA, pin).
Does not schedule anything. Host on branch budget-harbor-week2, then schedule
only the Nov 15 and Nov 17 Christmas posts.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

SPEC = importlib.util.spec_from_file_location(
    "bh_week1_gen", "/workspace/budget_harbor_social/week1/_generate.py"
)
g = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(g)

hook_slide = g.hook_slide
content_slide = g.content_slide
statement_slide = g.statement_slide
mockup_slide = g.mockup_slide
still_slide = g.still_slide
cta_slide = g.cta_slide
pin_image = g.pin_image
contact_sheet = g.contact_sheet
save = g.save
load_img = g.load_img
render_pair = g.render_pair
contain = g.contain
Image = g.Image

ROOT = Path("/workspace/budget_harbor_social/week2")
MOCK = Path("/workspace/digital-products/mockups")
PREV = Path("/workspace/digital-products/previews")

IG = g.IG
TT = g.TT
PIN = g.PIN


def crop_readable(im: Image.Image, max_ratio: float = 0.90) -> Image.Image:
    """Keep the top of a sheet screenshot (title + EXAMPLE DATA + first rows)."""
    im = im.convert("RGB")
    w, h = im.size
    if h > w * max_ratio:
        return im.crop((0, 0, w, int(w * max_ratio)))
    return im


def sheet_slide(size, image: Image.Image, headline: str, caption: str = "Example data shown"):
    return mockup_slide(size, headline, crop_readable(image), caption=caption)


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")


def write_pin_copy(folder: Path, title: str, description: str, url: str) -> None:
    write_text(
        folder / "pin" / "copy.txt",
        f"TITLE:\n{title}\n\nDESCRIPTION:\n{description}\n\n{url}\n\nLISTING URL:\n{url}\n",
    )


def write_caption(folder: Path, text: str) -> None:
    write_text(folder / "caption.txt", text)


def build_post(folder: Path, makers, pin, contact_title: str, caption: str, pin_copy: dict):
    igs = []
    for i, fn in enumerate(makers, 1):
        pig, _ = render_pair(fn, folder, f"{i:02d}")
        igs.append(pig)
    pin_path = save(pin, folder / "pin" / "pin.png")
    contact_sheet(igs, contact_title, folder / "contact.png", pin_path)
    write_caption(folder, caption)
    write_pin_copy(folder, pin_copy["title"], pin_copy["description"], pin_copy["url"])
    return folder.name


def build_all():
    # --- product art ---
    m06 = load_img(MOCK / "06_Christmas_Budget_Gift_Tracker_mockup.png")
    m07 = load_img(MOCK / "07_Savings_Challenge_Tracker_mockup.png")
    m08 = load_img(MOCK / "08_Bill_Tracker_Calendar_mockup.png")
    m09 = load_img(MOCK / "09_Net_Worth_Tracker_mockup.png")
    m10 = load_img(MOCK / "10_Couples_Family_Budget_mockup.png")
    m11 = load_img(MOCK / "11_Small_Business_Bookkeeping_mockup.png")
    m12 = load_img(MOCK / "12_Self_Employed_Tax_Tracker_mockup.png")
    m13 = load_img(MOCK / "13_Pricing_Calculator_Etsy_Sellers_mockup.png")
    mB2 = load_img(MOCK / "B2_New_Year_Money_Reset_Bundle_mockup.png")
    mB3 = load_img(MOCK / "B3_Small_Business_Bundle_mockup.png")

    p06_dash = load_img(PREV / "06_Christmas_Budget_Dashboard.png")
    p06_people = load_img(PREV / "06b_People_Gift_Budgets.png")
    p06_gifts = load_img(PREV / "06c_Gift_List.png")
    p06_exp = load_img(PREV / "06d_Holiday_Expenses.png")
    p06_check = load_img(PREV / "06e_Holiday_Checklist.png")

    p07_dash = load_img(PREV / "07_Savings_Challenge_Dashboard.png")
    p07_52 = load_img(PREV / "07b_52_Week_Challenge.png")
    p07_env = load_img(PREV / "07c_10K_100_Envelope_Challenge.png")
    p07_nosp = load_img(PREV / "07d_No_Spend_Calendar.png")

    p08_dash = load_img(PREV / "08_Bill_Dashboard.png")
    p08_list = load_img(PREV / "08b_Bill_List.png")
    p08_cal = load_img(PREV / "08c_Bill_Calendar.png")

    p09_dash = load_img(PREV / "09_Net_Worth_Dashboard.png")
    p09_acct = load_img(PREV / "09b_Accounts.png")
    p09_trend = load_img(PREV / "09c_Monthly_Balances.png")

    p10_dash = load_img(PREV / "10_Household_Dashboard.png")
    p10_split = load_img(PREV / "10b_Setup_Split.png")
    p10_settle = load_img(PREV / "10e_Settle_Up.png")

    p11_dash = load_img(PREV / "11_Business_Dashboard.png")
    p11_pl = load_img(PREV / "11e_Monthly_PL.png")

    p12_dash = load_img(PREV / "12_Tax_Dashboard.png")
    p12_ded = load_img(PREV / "12d_Deductions.png")
    p12_q = load_img(PREV / "12g_Quarterly_Taxes.png")

    p13_price = load_img(PREV / "13_Price_a_Product.png")
    p13_mat = load_img(PREV / "13c_Materials_Library.png")
    p13_fees = load_img(PREV / "13e_Etsy_Fee_Calculator.png")

    U06 = "https://www.etsy.com/listing/4617048643"
    U07 = "https://www.etsy.com/listing/4617057350"
    U08 = "https://www.etsy.com/listing/4617050273"
    U09 = "https://www.etsy.com/listing/4617050661"
    U10 = "https://www.etsy.com/listing/4617050965"
    U11 = "https://www.etsy.com/listing/4617058724"
    U12 = "https://www.etsy.com/listing/4617051585"
    U13 = "https://www.etsy.com/listing/4617051915"
    UB2 = "https://www.etsy.com/listing/4617059670"
    UB3 = "https://www.etsy.com/listing/4617060022"

    built = []

    # ======================================================================
    # DROP A — Sun Nov 15, 12:00 PM ET — January-statement hook
    # ======================================================================
    d = ROOT / "drop_sun15_january_statement"

    def a1(sz):
        return hook_slide(sz, ["Don't wait for", "January's statement."])

    def a2(sz):
        return statement_slide(
            sz,
            "See what you've spent before the bill arrives.",
            "Plan every person, every gift, and every party in one sheet — with a live countdown to Christmas.",
        )

    def a3(sz):
        return content_slide(
            sz,
            "What's in the tracker.",
            kicker="Google Sheets + Excel  ·  instant download  ·  no macros",
            bullets=[
                "Holiday budget vs. spent across 10 categories",
                "People tab: up to 40 people, each with a gift budget",
                "Gift list with planned vs. actual cost and status",
                "Holiday expenses, a checklist, and a card list",
            ],
            footnote="Change the year to reuse it next Christmas. Example data is included.",
        )

    def a4(sz):
        return sheet_slide(sz, p06_dash, "Budget vs. spent, with a countdown.")

    def a5(sz):
        return mockup_slide(
            sz,
            "Christmas Budget & Gift Tracker.",
            m06,
            caption="Product mockup  ·  Example data shown",
            badge="$3.99  ·  GOOGLE SHEETS + EXCEL",
        )

    def a6(sz):
        return cta_slide(
            sz,
            "Christmas Budget & Gift Tracker",
            "$3.99",
            points=["Google Sheets + Excel", "No macros  ·  Instant download"],
            extra="A tracker — not a promise you'll stay under budget.",
            thumb=m06,
        )

    cap_a = """Don't wait for January's statement.

I just added a Christmas Budget & Gift Tracker to Budget Harbor Co, my Etsy shop of Google Sheets and Excel money spreadsheets.

Set a holiday budget, split it across gifts, food, decorations, parties, and travel, and see budget vs. spent as you go. There's a people tab, a gift list with planned vs. actual cost and status (Idea → Ordered → Bought → Wrapped → Given), a holiday expenses log, a checklist, and a card list. Change the year to reuse it next Christmas.

$3.99. Google Sheets + Excel. No macros. Instant download. Example data is included so you can see how it works.

Link in bio, or search Budget Harbor Co on Etsy.

#BudgetHarborCo #ChristmasBudget #GiftTracker #HolidayBudget #GoogleSheets #ExcelTemplate #ChristmasPlanner #EtsyShop"""

    pin_a = pin_image(
        ["Don't wait for", "January's statement."],
        "Christmas Budget & Gift Tracker",
        "$3.99",
        None,
        "Google Sheets + Excel  ·  Instant download",
        m06,
    )
    built.append(
        build_post(
            d,
            [a1, a2, a3, a4, a5, a6],
            pin_a,
            "Sun Nov 15  ·  Christmas tracker  ·  12:00 PM ET",
            cap_a,
            {
                "title": "Christmas Budget & Gift Tracker Spreadsheet | $3.99",
                "description": "Plan the holiday in one Google Sheets or Excel file: a holiday budget vs. spent dashboard, a people tab, a gift list with planned vs. actual cost and status, a holiday expenses log, a checklist, and a card list. Live countdown to Christmas. Change the year to reuse it. No macros. Instant download. Example data included. $3.99 at Budget Harbor Co on Etsy.",
                "url": U06,
            },
        )
    )

    # ======================================================================
    # DROP B — Tue Nov 17, 6:00 PM ET — who's still on your list
    # ======================================================================
    d = ROOT / "drop_tue17_whos_on_your_list"

    def b1(sz):
        return hook_slide(sz, ["Who's still on", "your list?"], variant="cream")

    def b2(sz):
        return statement_slide(
            sz,
            "Every person. Every gift. One sheet.",
            "Up to 40 people, each with a gift budget — planned cost, spent, what's left, and who's still shopping.",
        )

    def b3(sz):
        return sheet_slide(sz, p06_people, "See who's still shopping.")

    def b4(sz):
        return sheet_slide(
            sz,
            p06_gifts,
            "Idea, ordered, bought, wrapped, given.",
        )

    def b5(sz):
        return content_slide(
            sz,
            "The gift list does the tracking.",
            bullets=[
                "Up to 80 gifts with planned vs. actual cost",
                "Where to buy, arrival date, and status",
                "Over/under flags are automatic",
                "A card list for sent and received",
            ],
            footnote="Example data shown. This is a tracker, not a promise you'll spend less.",
        )

    def b6(sz):
        return cta_slide(
            sz,
            "Christmas Budget & Gift Tracker",
            "$3.99",
            points=["Google Sheets + Excel", "No macros  ·  Instant download"],
            extra="Link in bio, or search Budget Harbor Co on Etsy.",
            thumb=m06,
        )

    cap_b = """Who's still on your list?

I built a Christmas Budget & Gift Tracker so you can see every person, every gift, and what's left to buy — before the holiday rush buries the list.

Up to 40 people, each with a gift budget. A gift list of up to 80 items with planned vs. actual cost, where to buy, arrival date, and status: Idea → Ordered → Bought → Wrapped → Given. Over/under flags are automatic. There's also a holiday budget dashboard, an expenses log, a checklist, and a card list.

$3.99. Google Sheets + Excel. No macros. Instant download. Example data included.

Link in bio, or search Budget Harbor Co on Etsy.

#BudgetHarborCo #GiftList #ChristmasBudget #HolidayPlanner #GoogleSheets #ExcelTemplate #GiftTracker #EtsyShop"""

    pin_b = pin_image(
        ["Who's still on", "your list?"],
        "Christmas Budget & Gift Tracker",
        "$3.99",
        None,
        "Google Sheets + Excel  ·  Instant download",
        m06,
    )
    built.append(
        build_post(
            d,
            [b1, b2, b3, b4, b5, b6],
            pin_b,
            "Tue Nov 17  ·  Christmas list angle  ·  6:00 PM ET",
            cap_b,
            {
                "title": "Christmas Gift List Tracker for Google Sheets and Excel | $3.99",
                "description": "See who's still on your holiday list. The Christmas Budget & Gift Tracker has a people tab (up to 40, each with a gift budget) and a gift list with planned vs. actual cost, store, arrival date, and status from Idea to Given. Also includes a holiday budget dashboard, expenses log, checklist, and card list. Google Sheets + Excel. $3.99 at Budget Harbor Co on Etsy.",
                "url": U06,
            },
        )
    )

    # ======================================================================
    # WEEK 2 — Mon Nov 23 — Christmas angle 3 (plan before you buy)
    # ======================================================================
    d = ROOT / "01_mon23_plan_before_you_buy"

    def c1(sz):
        return hook_slide(sz, ["Plan the gifts", "before you buy."])

    def c2(sz):
        return statement_slide(
            sz,
            "One budget for the whole holiday.",
            "Gifts, food, decorations, parties, travel — set a total, split it across 10 categories, and watch budget vs. spent.",
        )

    def c3(sz):
        return sheet_slide(sz, p06_dash, "A live countdown, and a live total.")

    def c4(sz):
        return sheet_slide(sz, p06_exp, "Everything that isn't a gift, logged too.")

    def c5(sz):
        return content_slide(
            sz,
            "Reuse it next Christmas.",
            bullets=[
                "Change the year and start a fresh plan",
                "Holiday checklist with overdue and this-week flags",
                "Card list for sent and received",
                "Google Sheets and Excel, no macros",
            ],
        )

    def c6(sz):
        return cta_slide(
            sz,
            "Christmas Budget & Gift Tracker",
            "$3.99",
            points=["Google Sheets + Excel", "No macros  ·  Instant download"],
            thumb=m06,
        )

    cap_c = """Plan the gifts before you buy.

The Christmas Budget & Gift Tracker from Budget Harbor Co keeps the whole holiday in one spreadsheet: a budget vs. spent dashboard with a live countdown, a people tab, a gift list, a holiday expenses log, a checklist, and a card list.

Set a total, split it across 10 categories, and see what's left as you go. Change the year to reuse it next Christmas.

$3.99. Google Sheets + Excel. No macros. Instant download. Example data included.

Link in bio, or search Budget Harbor Co on Etsy.

#BudgetHarborCo #ChristmasBudget #HolidayBudget #GiftTracker #GoogleSheets #ExcelTemplate #ChristmasPlanner #EtsyShop"""

    pin_c = pin_image(
        ["Plan the gifts", "before you buy."],
        "Christmas Budget & Gift Tracker",
        "$3.99",
        None,
        "Google Sheets + Excel  ·  Instant download",
        m06,
    )
    built.append(
        build_post(
            d,
            [c1, c2, c3, c4, c5, c6],
            pin_c,
            "Mon Nov 23  ·  Christmas tracker  ·  12:00 PM ET  ·  NOT YET SCHEDULED",
            cap_c,
            {
                "title": "Holiday Budget Spreadsheet: Plan Gifts Before You Buy | $3.99",
                "description": "Plan the gifts before you buy. Christmas Budget & Gift Tracker for Google Sheets and Excel: holiday budget vs. spent across 10 categories, a live countdown, people and gift lists, expenses, a checklist, and a card list. Reuse it next year. $3.99 at Budget Harbor Co on Etsy.",
                "url": U06,
            },
        )
    )

    # ======================================================================
    # WEEK 2 — Tue Nov 24 — Savings Challenge
    # ======================================================================
    d = ROOT / "02_tue24_savings_challenge"

    def d1(sz):
        return hook_slide(sz, ["Four savings challenges.", "One spreadsheet."])

    def d2(sz):
        return statement_slide(
            sz,
            "Pick the one that fits your budget.",
            "Or run them side by side. A 52-week challenge, a $10K / 100-envelope challenge you can scale to your goal, a no-spend calendar, and up to 8 custom goals.",
        )

    def d3(sz):
        return content_slide(
            sz,
            "What's inside.",
            bullets=[
                "52-week: increasing, decreasing, or the same each week",
                "$10K / 100-envelope, or the classic $1–$100 version",
                "No-spend calendar with a monthly percentage",
                "Custom goals with targets, deadlines, and monthly deposits",
            ],
            footnote="A tracker for the plan you choose — not a promise you'll hit a set amount.",
        )

    def d4(sz):
        return sheet_slide(sz, p07_dash, "Every challenge, side by side.")

    def d5(sz):
        return mockup_slide(
            sz,
            "Savings Challenge Tracker.",
            m07,
            caption="Product mockup  ·  Example data shown",
            badge="$4.99  ·  GOOGLE SHEETS + EXCEL",
        )

    def d6(sz):
        return cta_slide(
            sz,
            "Savings Challenge Tracker",
            "$4.99",
            points=["Google Sheets + Excel", "No macros  ·  Instant download"],
            extra="Four challenges in one file. You set the goal.",
            thumb=m07,
        )

    cap_d = """Four savings challenges. One spreadsheet.

I built a Savings Challenge Tracker for Budget Harbor Co so you can pick the challenge that fits your budget — or run a few at once.

• 52-week challenge: choose a start date, a week-1 amount, and a style (increasing, decreasing, or the same every week)
• $10K / 100-envelope challenge, scaled to your goal, or the classic $1–$100 version
• No-spend calendar, with a monthly no-spend percentage
• Up to 8 custom goals with targets, deadlines, and monthly deposits
• A dashboard that puts every challenge side by side

$4.99. Google Sheets + Excel. No macros. Instant download. Example data included. This is a tracker for the plan you choose, not a promise you'll hit a set amount.

Link in bio, or search Budget Harbor Co on Etsy.

#BudgetHarborCo #SavingsChallenge #52WeekChallenge #NoSpend #GoogleSheets #ExcelTemplate #SavingsTracker #EtsyShop"""

    pin_d = pin_image(
        ["Four savings challenges.", "One spreadsheet."],
        "Savings Challenge Tracker",
        "$4.99",
        None,
        "Google Sheets + Excel  ·  Instant download",
        m07,
    )
    built.append(
        build_post(
            d,
            [d1, d2, d3, d4, d5, d6],
            pin_d,
            "Tue Nov 24  ·  Savings Challenge  ·  12:00 PM ET  ·  NOT YET SCHEDULED",
            cap_d,
            {
                "title": "52-Week, 10K Envelope & No-Spend Savings Challenge Tracker | $4.99",
                "description": "Four savings challenges in one Google Sheets or Excel file: a 52-week challenge, a $10K / 100-envelope challenge you can scale to your goal, a no-spend calendar, and up to 8 custom goals, plus a side-by-side dashboard. No macros. Instant download. $4.99 at Budget Harbor Co on Etsy.",
                "url": U07,
            },
        )
    )

    # ======================================================================
    # WEEK 2 — Wed Nov 25 — Bill Tracker
    # ======================================================================
    d = ROOT / "03_wed25_bill_tracker"

    def e1(sz):
        return hook_slide(sz, ["See every bill", "in one place."])

    def e2(sz):
        return statement_slide(
            sz,
            "What's due, and whether it's paid.",
            "A bill list, a monthly calendar, a 12-month payment tracker, and a dashboard with totals and 'pay soon' alerts.",
        )

    def e3(sz):
        return content_slide(
            sz,
            "The tracker does the dates for you.",
            bullets=[
                "Up to 40 bills: amount, due day, frequency, autopay",
                "Next due date, days left, and pay-soon alerts",
                "A calendar for any month, with totals by day",
                "12 months of check-offs, with unpaid amounts totaled",
            ],
        )

    def e4(sz):
        return sheet_slide(sz, p08_cal, "A calendar of everything due this month.")

    def e5(sz):
        return mockup_slide(
            sz,
            "Bill Tracker & Bill Calendar.",
            m08,
            caption="Product mockup  ·  Example data shown",
            badge="$4.99  ·  GOOGLE SHEETS + EXCEL",
        )

    def e6(sz):
        return cta_slide(
            sz,
            "Bill Tracker & Calendar",
            "$4.99",
            points=["Google Sheets + Excel", "No macros  ·  Instant download"],
            thumb=m08,
        )

    cap_e = """See every bill in one place.

The Bill Tracker from Budget Harbor Co keeps the list, the calendar, and the paid check-offs together.

Up to 40 bills with amount, due day, frequency (monthly, quarterly, semiannual, annual), autopay, and account. Next due date, days left, and “pay soon” alerts are automatic, plus the monthly equivalent and yearly cost of each bill. Pick any month and see what's due, then check off payments across 12 months. A dashboard shows monthly and yearly totals, bills due in the next 7 days, and yearly cost by category.

$4.99. Google Sheets + Excel. No macros. Instant download. Example data included.

Link in bio, or search Budget Harbor Co on Etsy.

#BudgetHarborCo #BillTracker #BillCalendar #MonthlyBills #GoogleSheets #ExcelTemplate #BudgetPlanner #EtsyShop"""

    pin_e = pin_image(
        ["See every bill", "in one place."],
        "Bill Tracker & Bill Calendar",
        "$4.99",
        None,
        "Google Sheets + Excel  ·  Instant download",
        m08,
    )
    built.append(
        build_post(
            d,
            [e1, e2, e3, e4, e5, e6],
            pin_e,
            "Wed Nov 25  ·  Bill Tracker  ·  12:00 PM ET  ·  NOT YET SCHEDULED",
            cap_e,
            {
                "title": "Bill Tracker Spreadsheet with Monthly Bill Calendar | $4.99",
                "description": "See every bill, when it is due, and whether it is paid. Bill Tracker for Google Sheets and Excel: a bill list with pay-soon alerts, a monthly calendar, a 12-month payment tracker, and a dashboard of totals and yearly cost by category. No macros. Instant download. $4.99 at Budget Harbor Co on Etsy.",
                "url": U08,
            },
        )
    )

    # ======================================================================
    # WEEK 2 — Thu Nov 26 — Couples / Family Budget (Thanksgiving)
    # ======================================================================
    d = ROOT / "04_thu26_couples_family"

    def f1(sz):
        return hook_slide(sz, ["One budget that", "works for two."], variant="cream")

    def f2(sz):
        return statement_slide(
            sz,
            "Both incomes. Shared and personal spending. A fair split.",
            "Set 50/50, proportional to income, or a custom percent — then see who owes whom at the end of the month.",
        )

    def f3(sz):
        return content_slide(
            sz,
            "Built for a household.",
            bullets=[
                "Two names, two incomes, and a split you choose",
                "Up to 30 categories: shared or personal to one partner",
                "Log who paid, and whether it was shared or personal",
                "Settle Up: a plain-language “who owes whom” line",
                "Up to 10 joint goals with each person's contributions",
            ],
        )

    def f4(sz):
        return sheet_slide(sz, p10_settle, "A clear settle-up, not a guess.")

    def f5(sz):
        return mockup_slide(
            sz,
            "Couples & Family Budget.",
            m10,
            caption="Product mockup  ·  Example data shown",
            badge="$7.99  ·  GOOGLE SHEETS + EXCEL",
        )

    def f6(sz):
        return cta_slide(
            sz,
            "Couples & Family Budget",
            "$7.99",
            points=["Google Sheets + Excel", "Works for a single household too"],
            thumb=m10,
        )

    cap_f = """One budget that works for two.

The Couples & Family Budget from Budget Harbor Co is one spreadsheet for both incomes, shared and personal spending, and a fair way to split the shared costs.

Choose 50/50, proportional to income, or a custom percent. Budget up to 30 categories (shared or personal to one partner). Log each purchase with who paid and whether it was shared or personal. Settle Up shows what each of you should have paid, what you actually paid, and a plain-language “who owes whom” line. There's also room for up to 10 joint goals.

$7.99. Google Sheets + Excel. No macros. Instant download. Example data included. Works for a single household too.

Link in bio, or search Budget Harbor Co on Etsy.

#BudgetHarborCo #CouplesBudget #FamilyBudget #SharedExpenses #GoogleSheets #ExcelTemplate #HouseholdBudget #EtsyShop"""

    pin_f = pin_image(
        ["One budget that", "works for two."],
        "Couples & Family Budget",
        "$7.99",
        None,
        "Google Sheets + Excel  ·  Instant download",
        m10,
    )
    built.append(
        build_post(
            d,
            [f1, f2, f3, f4, f5, f6],
            pin_f,
            "Thu Nov 26  ·  Couples & Family Budget  ·  12:00 PM ET  ·  NOT YET SCHEDULED",
            cap_f,
            {
                "title": "Couples & Family Budget Spreadsheet with Settle Up | $7.99",
                "description": "One budget for two people: both incomes, shared and personal spending, and a fair split (50/50, proportional to income, or custom). Includes a settle-up that shows who owes whom, a monthly budget, transactions, joint goals, and a household dashboard. Google Sheets + Excel. $7.99 at Budget Harbor Co on Etsy.",
                "url": U10,
            },
        )
    )

    # ======================================================================
    # WEEK 2 — Fri Nov 27 — Net Worth
    # ======================================================================
    d = ROOT / "05_fri27_net_worth"

    def g1(sz):
        return hook_slide(sz, ["What you own minus", "what you owe."])

    def g2(sz):
        return statement_slide(
            sz,
            "Track it month by month, and see the trend.",
            "Up to 20 assets and 15 debts, a 12-month balance grid, and a dashboard with assets vs. debts and a net worth line.",
        )

    def g3(sz):
        return content_slide(
            sz,
            "What's on the sheet.",
            bullets=[
                "Cash, savings, retirement, investments, home, vehicles, and more",
                "Mortgage, auto, student loans, credit cards, and other debts",
                "Totals, net worth, and month-over-month change — automatic",
                "An investments tab for holdings you type in (nothing is pulled from the internet)",
            ],
            footnote="A net worth goal uses a simple straight-line target, not a forecast.",
        )

    def g4(sz):
        return sheet_slide(sz, p09_dash, "Assets, debts, and the trend in one view.")

    def g5(sz):
        return mockup_slide(
            sz,
            "Net Worth Tracker.",
            m09,
            caption="Product mockup  ·  Example data shown",
            badge="$5.99  ·  GOOGLE SHEETS + EXCEL",
        )

    def g6(sz):
        return cta_slide(
            sz,
            "Net Worth Tracker",
            "$5.99",
            points=["Google Sheets + Excel", "No macros  ·  Instant download"],
            thumb=m09,
        )

    cap_g = """What you own minus what you owe.

The Net Worth Tracker from Budget Harbor Co follows that number month by month so you can see the trend.

Up to 20 assets and 15 debts, each with a type. A starting column plus 12 months; totals, net worth, and month-over-month change are automatic. The dashboard shows the latest net worth, change since the start, debt-to-asset ratio, a trend line, and an assets vs. debts chart. Optional: enter a goal and target date to see a simple straight-line target (not a forecast). An investments tab tracks holdings from prices you type in — nothing is pulled from the internet.

$5.99. Google Sheets + Excel. No macros. Instant download. Example data included.

Link in bio, or search Budget Harbor Co on Etsy.

#BudgetHarborCo #NetWorth #WealthTracker #InvestmentTracker #GoogleSheets #ExcelTemplate #PersonalFinance #EtsyShop"""

    pin_g = pin_image(
        ["What you own minus", "what you owe."],
        "Net Worth Tracker",
        "$5.99",
        None,
        "Google Sheets + Excel  ·  Instant download",
        m09,
    )
    built.append(
        build_post(
            d,
            [g1, g2, g3, g4, g5, g6],
            pin_g,
            "Fri Nov 27  ·  Net Worth  ·  12:00 PM ET  ·  NOT YET SCHEDULED",
            cap_g,
            {
                "title": "Net Worth Tracker Spreadsheet: Assets, Debts & Trend | $5.99",
                "description": "Track what you own minus what you owe, month by month. Net Worth Tracker for Google Sheets and Excel: up to 20 assets and 15 debts, a 12-month balance grid, a dashboard with a trend line, an optional straight-line goal, and an investments tab (prices you type in). $5.99 at Budget Harbor Co on Etsy.",
                "url": U09,
            },
        )
    )

    # ======================================================================
    # WEEK 2 — Sat Nov 28 — Small Business Bundle B3 (leads with bookkeeping)
    # ======================================================================
    d = ROOT / "06_sat28_small_business_bundle"

    def h1(sz):
        return hook_slide(sz, ["Four tools for", "a small business."])

    def h2(sz):
        return statement_slide(
            sz,
            "Bookkeeping, tax tracking, pricing, and income — together.",
            "The Small Business Bundle is $24.99, versus $41.96 if you bought the four templates separately.",
        )

    def h3(sz):
        return content_slide(
            sz,
            "What's in the bundle.",
            bullets=[
                "Small Business Bookkeeping — income, expenses, monthly P&L, Schedule C-style summary",
                "Self-Employed Tax Tracker — deductions, mileage, quarterly estimates",
                "Pricing Calculator for Etsy Sellers — materials, labor, overhead, fees",
                "Side Hustle Income Tracker — income by source, expenses, tax set-aside",
            ],
            footnote="Tax figures are simplified planning estimates, not tax advice. Bookkeeping alone is also $14.99.",
        )

    def h4(sz):
        return sheet_slide(sz, p11_dash, "Log the activity. The reports fill in.")

    def h5(sz):
        return mockup_slide(
            sz,
            "Small Business Bundle.",
            mB3,
            caption="Bundle mockup  ·  Example data shown",
            badge="BUNDLE  ·  $24.99",
        )

    def h6(sz):
        return cta_slide(
            sz,
            "Small Business Bundle",
            "$24.99",
            was="$41.96",
            points=["Four templates  ·  Google Sheets + Excel", "No macros  ·  Instant download"],
            extra="Versus buying the four templates separately.",
            thumb=mB3,
        )

    cap_h = """Four tools for a small business.

The Small Business Bundle from Budget Harbor Co is $24.99, versus $41.96 if you bought these four templates separately.

1. Small Business Bookkeeping — income and expense logs, an automatic monthly P&L, a dashboard, and a Schedule C-style year-end summary
2. Self-Employed Tax Tracker — deductions, mileage at IRS rates, home office, and quarterly estimated-tax planning
3. Pricing Calculator for Etsy Sellers — materials, labor, overhead, and Etsy fees
4. Side Hustle & Commission Income Tracker — income by source, expenses, and a tax set-aside

Tax figures are simplified planning estimates, not tax advice. The bookkeeping template is also sold on its own for $14.99.

$24.99. Google Sheets + Excel. No macros. Instant download. Example data included.

Link in bio, or search Budget Harbor Co on Etsy.

#BudgetHarborCo #SmallBusiness #Bookkeeping #EtsySeller #GoogleSheets #ExcelTemplate #SelfEmployed #EtsyShop"""

    pin_h = pin_image(
        ["Four tools for", "a small business."],
        "Small Business Spreadsheet Bundle",
        "$24.99",
        "$41.96",
        "Four templates  ·  Google Sheets + Excel",
        mB3,
        badge="BUNDLE  ·  4 TEMPLATES",
    )
    built.append(
        build_post(
            d,
            [h1, h2, h3, h4, h5, h6],
            pin_h,
            "Sat Nov 28  ·  Small Business Bundle  ·  12:00 PM ET  ·  NOT YET SCHEDULED",
            cap_h,
            {
                "title": "Small Business Spreadsheet Bundle: Bookkeeping, Tax, Pricing | $24.99",
                "description": "Four spreadsheets for a small business, shop, or side business: Small Business Bookkeeping, Self-Employed Tax Tracker, Pricing Calculator for Etsy Sellers, and Side Hustle Income Tracker. $24.99 versus $41.96 if bought separately. Google Sheets + Excel. Tax figures are planning estimates, not tax advice. Budget Harbor Co on Etsy.",
                "url": UB3,
            },
        )
    )

    # ======================================================================
    # WEEK 2 — Sun Nov 29 — Self-Employed Tax Tracker
    # ======================================================================
    d = ROOT / "07_sun29_self_employed_tax"

    def i1(sz):
        return hook_slide(sz, ["Keep deductions in", "one place."])

    def i2(sz):
        return statement_slide(
            sz,
            "A rough idea of what to set aside each quarter.",
            "For freelancers, 1099 contractors, and side hustlers. Planning estimates based on rates you choose — not tax advice.",
        )

    def i3(sz):
        return content_slide(
            sz,
            "What's on the tracker.",
            bullets=[
                "Income by client or platform, with a 1099 check",
                "Deductions with business-use percent and a receipt check",
                "Mileage log at IRS standard rates (2026 rates pre-filled, editable)",
                "Home office: simplified vs. a rough regular-method comparison",
                "Quarterly estimates with IRS due dates and amounts paid",
            ],
            footnote="Confirm figures with a tax professional or irs.gov. Not tax advice.",
        )

    def i4(sz):
        return sheet_slide(sz, p12_dash, "Income, deductions, and a quarterly picture.")

    def i5(sz):
        return mockup_slide(
            sz,
            "Self-Employed Tax Tracker.",
            m12,
            caption="Product mockup  ·  Example data shown",
            badge="$12.99  ·  GOOGLE SHEETS + EXCEL",
        )

    def i6(sz):
        return cta_slide(
            sz,
            "Self-Employed Tax Tracker",
            "$12.99",
            points=["Google Sheets + Excel", "Planning estimates, not tax advice"],
            extra="Also in the $24.99 Small Business Bundle.",
            thumb=m12,
        )

    cap_i = """Keep deductions in one place.

The Self-Employed Tax Tracker from Budget Harbor Co is for freelancers, 1099 contractors, and side hustlers who want deductions organized and a rough idea of what to set aside each quarter.

Log income by client or platform and which 1099 you expect. Track deductions with a business-use percent (for mixed costs like a phone) and a receipt check. Mileage uses the IRS standard rate for that date (2026 rates, including the July 1 change, are pre-filled and editable). There's a home-office comparison and a quarterly-tax sheet with due dates, amounts paid, and what's left.

All tax figures are simplified planning estimates based on rates you choose. Not tax advice — confirm with a tax professional or irs.gov.

$12.99. Google Sheets + Excel. No macros. Instant download. Example data included. Also in the $24.99 Small Business Bundle.

Link in bio, or search Budget Harbor Co on Etsy.

#BudgetHarborCo #SelfEmployed #TaxTracker #1099 #QuarterlyTaxes #GoogleSheets #ExcelTemplate #EtsyShop"""

    pin_i = pin_image(
        ["Keep deductions in", "one place."],
        "Self-Employed Tax Tracker",
        "$12.99",
        None,
        "Planning estimates, not tax advice",
        m12,
    )
    built.append(
        build_post(
            d,
            [i1, i2, i3, i4, i5, i6],
            pin_i,
            "Sun Nov 29  ·  Self-Employed Tax  ·  12:00 PM ET  ·  NOT YET SCHEDULED",
            cap_i,
            {
                "title": "Self-Employed Tax Tracker: Deductions, Mileage, Quarterly Estimates | $12.99",
                "description": "For freelancers, 1099 contractors, and side hustlers. Track income, deductions, mileage at IRS rates, home office, and quarterly estimated taxes in Google Sheets or Excel. Figures are simplified planning estimates, not tax advice. $12.99 at Budget Harbor Co on Etsy. Also in the Small Business Bundle.",
                "url": U12,
            },
        )
    )

    # ======================================================================
    # EXTRA READY DRAFT — Pricing Calculator (schedule when a slot opens)
    # ======================================================================
    d = ROOT / "08_ready_pricing_calculator"

    def j1(sz):
        return hook_slide(sz, ["Price it before", "you list it."])

    def j2(sz):
        return statement_slide(
            sz,
            "Materials, time, overhead, packaging, shipping, and Etsy fees.",
            "See wholesale, retail, target-margin, and break-even prices — then set your own price and watch the margin.",
        )

    def j3(sz):
        return content_slide(
            sz,
            "Built for Etsy sellers.",
            bullets=[
                "Materials library: up to 60 supplies, cost per unit calculated",
                "Price a product: up to 12 materials, labor minutes, packaging, shipping",
                "Every Etsy fee, plus profit and margin at your price",
                "A product price list, a fee calculator, and a simple inventory tab",
            ],
            footnote="Fee defaults reflect Etsy's published US fees as of 2026; update them if fees change.",
        )

    def j4(sz):
        return sheet_slide(sz, p13_price, "Price it from the real numbers.")

    def j5(sz):
        return mockup_slide(
            sz,
            "Pricing Calculator for Etsy Sellers.",
            m13,
            caption="Product mockup  ·  Example data shown",
            badge="$6.99  ·  GOOGLE SHEETS + EXCEL",
        )

    def j6(sz):
        return cta_slide(
            sz,
            "Pricing Calculator for Etsy Sellers",
            "$6.99",
            points=["Google Sheets + Excel", "Also in the $24.99 Small Business Bundle"],
            thumb=m13,
        )

    cap_j = """Price it before you list it.

The Pricing Calculator for Etsy Sellers from Budget Harbor Co prices handmade products from real numbers: materials, your time, overhead, packaging, shipping, and Etsy fees.

Build a materials library (up to 60 supplies). Price a product with up to 12 materials, labor minutes, packaging, and shipping, and see wholesale, retail, target-margin, and break-even prices, every Etsy fee, and your profit and margin at the price you choose. Duplicate the tab for each product. There's also a 40-product price list, an Etsy fee calculator, and a simple inventory tab with reorder flags.

Fee defaults reflect Etsy's published US fees as of 2026; update them if Etsy changes them or your bank is outside the US.

$6.99. Google Sheets + Excel. No macros. Instant download. Example data included. Also in the $24.99 Small Business Bundle.

Link in bio, or search Budget Harbor Co on Etsy.

#BudgetHarborCo #EtsySeller #PricingCalculator #EtsyFees #HandmadeBusiness #GoogleSheets #ExcelTemplate #EtsyShop"""

    pin_j = pin_image(
        ["Price it before", "you list it."],
        "Pricing Calculator for Etsy Sellers",
        "$6.99",
        None,
        "Google Sheets + Excel  ·  Instant download",
        m13,
    )
    built.append(
        build_post(
            d,
            [j1, j2, j3, j4, j5, j6],
            pin_j,
            "READY DRAFT  ·  Pricing Calculator  ·  schedule when a slot opens",
            cap_j,
            {
                "title": "Etsy Seller Pricing Calculator: Materials, Labor, Fees | $6.99",
                "description": "Price handmade products from materials, labor, overhead, packaging, shipping, and Etsy fees. See wholesale, retail, target-margin, and break-even prices, plus profit at your own price. Includes a materials library, product price list, fee calculator, and inventory tab. Google Sheets + Excel. $6.99 at Budget Harbor Co on Etsy.",
                "url": U13,
            },
        )
    )

    # ======================================================================
    # HOLD — B2 New Year Money Reset Bundle (late Dec / Jan only)
    # ======================================================================
    d = ROOT / "hold_B2_new_year_reset"

    def k1(sz):
        return hook_slide(sz, ["A fresh start", "for your money."], variant="cream")

    def k2(sz):
        return statement_slide(
            sz,
            "Five spreadsheets for a new-year reset.",
            "The New Year Money Reset Bundle is $16.99, versus $28.95 if you bought the five templates separately.",
        )

    def k3(sz):
        return content_slide(
            sz,
            "What's in the bundle.",
            bullets=[
                "Savings Challenge Tracker — 52-week, 100-envelope, no-spend, custom goals",
                "Bill Tracker & Bill Calendar — due dates, calendar, 12-month paid tracker",
                "Net Worth Tracker — assets, debts, and the month-by-month trend",
                "Couples & Family Budget — a shared budget with a fair split and settle-up",
                "Sinking Funds & Savings Tracker — set-asides, cash envelopes, savings pots",
            ],
            footnote="Hold this post for late December or January. Do not schedule it in November.",
        )

    def k4(sz):
        return mockup_slide(
            sz,
            "New Year Money Reset Bundle.",
            mB2,
            caption="Bundle mockup  ·  Example data shown",
            badge="BUNDLE  ·  $16.99",
        )

    def k5(sz):
        return cta_slide(
            sz,
            "New Year Money Reset Bundle",
            "$16.99",
            was="$28.95",
            points=["Five templates  ·  Google Sheets + Excel", "No macros  ·  Instant download"],
            extra="Versus buying the five templates separately.",
            thumb=mB2,
        )

    cap_k = """A fresh start for your money.

The New Year Money Reset Bundle from Budget Harbor Co is $16.99, versus $28.95 if you bought these five templates separately.

1. Savings Challenge Tracker
2. Bill Tracker & Bill Calendar
3. Net Worth Tracker
4. Couples & Family Budget
5. Sinking Funds & Savings Tracker

$16.99. Google Sheets + Excel. No macros. Instant download. Example data included.

Link in bio, or search Budget Harbor Co on Etsy.

#BudgetHarborCo #NewYearBudget #BudgetBundle #SavingsChallenge #NetWorth #GoogleSheets #ExcelTemplate #EtsyShop"""

    pin_k = pin_image(
        ["A fresh start", "for your money."],
        "New Year Money Reset Bundle",
        "$16.99",
        "$28.95",
        "Five templates  ·  Google Sheets + Excel",
        mB2,
        badge="BUNDLE  ·  5 TEMPLATES",
    )
    built.append(
        build_post(
            d,
            [k1, k2, k3, k4, k5],
            pin_k,
            "HOLD  ·  late Dec / Jan only  ·  New Year Money Reset Bundle  ·  DO NOT SCHEDULE YET",
            cap_k,
            {
                "title": "New Year Money Reset Bundle: 5 Budget Spreadsheets | $16.99",
                "description": "Five money spreadsheets for a fresh start: Savings Challenge Tracker, Bill Tracker & Calendar, Net Worth Tracker, Couples & Family Budget, and Sinking Funds Tracker. $16.99 versus $28.95 if bought separately. Google Sheets + Excel. Budget Harbor Co on Etsy. Hold this pin for late December or January.",
                "url": UB2,
            },
        )
    )

    print("Built posts:", built)
    for post in built:
        for sub in ("ig", "tt", "pin"):
            folder = ROOT / post / sub
            if not folder.exists():
                continue
            for p in sorted(folder.glob("*.png")):
                im = Image.open(p)
                print(f"  {p.relative_to(ROOT)}  {im.size}")


if __name__ == "__main__":
    build_all()
