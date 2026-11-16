# كورس 01 · درس 02 · خطأ شائع: procedure بنفس الاسم مرتين
# C01 · L02 · common mistake: one name defined twice · Python 3.13 · 2026
cash = 265                        # global data: drawer
sugar_kg = 20                     # global data: stock
def report():                     # cashier, near the top
    print("sales today:", cash)
# ... hundreds of lines later ...
def report():                     # stock keeper, far below
    print("sugar left:", sugar_kg, "kg")
report()                          # which one runs?
