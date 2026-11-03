# كورس 01 · درس 01 · الطريقة الصحيحة: مراجعة كل نتيجة بحث
# C01 · L01 · right way: review each search match · Python 3.13 · 2026
sugar_kg = 25         # global data: stock
cash = 0              # global data: drawer
total = 3 * 30        # morning: 3 pieces
cash = cash + total
print("morning:", total)
total = 2 * 30        # evening: 2 pieces
cash = cash + total
print("evening:", total)
total = 4 * 30 + 10   # delivery: 4 + fee
cash = cash + total
print("delivery:", total)
print("cash:", cash, "sugar:", sugar_kg)
