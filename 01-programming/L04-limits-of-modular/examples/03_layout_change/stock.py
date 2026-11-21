# كورس 01 · درس 04 · شكل البيانات اتغيّر
# C01 · L04 · the data layout changed · Python 3.13 · 2026
sugar_kg = {"Dokki": 20, "Maadi": 12}   # new: one stock per branch

def use(kg):                       # not updated yet
    global sugar_kg
    sugar_kg = sugar_kg - kg

def report():
    print("sugar left:", sugar_kg, "kg")
