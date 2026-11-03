# كورس 01 · درس 01 · حل التمرين: السعر 35 وأربع تعديلات
# C01 · L01 · solution: price 35, four edits · Python 3.13 · 2026
sugar_kg = 25         # global data: stock
cash = 0              # global data: drawer
total = 3 * 35        # morning: edit 1
cash = cash + total
print("morning:", total)
total = 2 * 35        # evening: edit 2
cash = cash + total
print("evening:", total)
total = 4 * 35 + 10   # delivery: edit 3
cash = cash + total
print("delivery:", total)
total = 5 * 35        # party: edit 4 (new copy)
cash = cash + total
print("party:", total)
print("cash:", cash, "sugar:", sugar_kg)
