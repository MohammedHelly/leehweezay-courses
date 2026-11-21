# كورس 01 · درس 04 · حل التمرين: module المخزن بالجرام
# C01 · L04 · exercise solution: stock in grams · Python 3.13 · 2026
sugar_g = 20000                    # changed: grams

def use(kg):
    global sugar_g                 # changed
    sugar_g = sugar_g - kg * 1000  # changed

def report():
    print("sugar left:", sugar_g, "g")   # changed
