# كورس 01 · درس 04 · خطأ شائع: من غير global
# C01 · L04 · common mistake: no global line · Python 3.13 · 2026
sugar_kg = 20

def use(kg):
    sugar_kg = sugar_kg - kg       # no global line

def report():
    print("sugar left:", sugar_kg, "kg")
