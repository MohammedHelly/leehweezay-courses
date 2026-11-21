# كورس 01 · درس 04 · module المخزن
# C01 · L04 · stock module · Python 3.13 · 2026
sugar_kg = 20                      # this module's data

def use(kg):                       # its job: change the stock
    global sugar_kg
    sugar_kg = sugar_kg - kg

def report():
    print("sugar left:", sugar_kg, "kg")
