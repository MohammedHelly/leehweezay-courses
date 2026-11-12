# كورس 01 · درس 02 · حل التمرين: procedure للمخزن
# C01 · L02 · solution: a stock procedure · Python 3.13 · 2026
sugar_kg = 25                       # global data: stock
def stock_after(trays, stock):      # 2 kg per tray
    return stock - trays * 2
print("start:", sugar_kg)
sugar_kg = stock_after(3, sugar_kg)
print("after morning:", sugar_kg)
sugar_kg = stock_after(2, sugar_kg)
print("after evening:", sugar_kg)
sugar_kg = stock_after(4, sugar_kg)
print("after delivery:", sugar_kg)
