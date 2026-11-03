# كورس 01 · درس 01 · تمرين: نسخة رابعة لحساب العزومة
# C01 · L01 · exercise: a 4th copy for a party order · Python 3.13 · 2026
sugar_kg = 25         # global data: stock
cash = 0              # global data: drawer
total = 3 * 25        # morning: 3 pieces
cash = cash + total
print("morning:", total)
total = 2 * 25        # evening: 2 pieces
cash = cash + total
print("evening:", total)
total = 4 * 25 + 10   # delivery: 4 + fee
cash = cash + total
print("delivery:", total)
total = 5 * 25        # party: 5 pieces (new copy)
cash = cash + total
print("party:", total)
print("cash:", cash, "sugar:", sugar_kg)
