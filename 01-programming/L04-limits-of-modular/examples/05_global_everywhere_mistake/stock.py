# كورس 01 · درس 04 · خطأ شائع: global في كل function
# C01 · L04 · common mistake: global everywhere · Python 3.13 · 2026
sugar_kg = 20

def use(kg):
    global sugar_kg
    sugar_kg = sugar_kg - kg

def report():
    global sugar_kg                # not needed: it only reads
    print("sugar left:", sugar_kg, "kg")
