# كورس 01 · درس 01 · إضافي: استبدال الكل غيّر كمية السكر
# C01 · L01 · bonus: Replace All changed the sugar stock · Python 3.13 · 2026
sugar_kg = 35         # global data: stock
cash = 0              # global data: drawer
total = 3 * 35        # morning: 3 pieces
cash = cash + total
print("morning:", total)
total = 2 * 35        # evening: 2 pieces
cash = cash + total
print("evening:", total)
total = 4 * 35 + 10   # delivery: 4 + fee
cash = cash + total
print("delivery:", total)
total = 5 * 35        # party: 5 pieces (new copy)
cash = cash + total
print("party:", total)
print("cash:", cash, "sugar:", sugar_kg)
