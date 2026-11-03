# كورس 01 · درس 01 · خطأ شائع: استبدال الكل غيّر كمية السكر
# C01 · L01 · common mistake: Replace All changed the sugar stock · Python 3.13 · 2026
sugar_kg = 30         # global data: stock
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
