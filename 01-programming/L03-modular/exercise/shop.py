# كورس 01 · درس 03 · الـ main program بيستخدم الـ modules
# C01 · L03 · main program imports the modules · Python 3.13 · 2026
import billing
import stock

cash = 0                           # main program data: drawer
cash = cash + billing.make_bill("morning", 3, 0)
cash = cash + billing.make_bill("evening", 2, 0)
cash = cash + billing.make_bill("delivery", 4, 10)
billing.report(cash)
stock.report()
