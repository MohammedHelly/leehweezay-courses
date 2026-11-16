# كورس 01 · درس 02 · الحل المؤقت: اسم مختلف لكل procedure
# C01 · L02 · a quick fix: one name per procedure · Python 3.13 · 2026
cash = 265                        # global data: drawer
sugar_kg = 20                     # global data: stock
def sales_report():               # cashier
    print("sales today:", cash)
def stock_report():               # stock keeper
    print("sugar left:", sugar_kg, "kg")
sales_report()
stock_report()
