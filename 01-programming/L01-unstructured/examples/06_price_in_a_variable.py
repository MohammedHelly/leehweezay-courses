# كورس 01 · درس 01 · السعر في متغير: الخطوات لسه متكررة
# C01 · L01 · price in a variable: steps still copied · Python 3.13 · 2026
sugar_kg = 25         # global data: stock
cash = 0              # global data: drawer
price = 30            # global data: one price
total = 3 * price     # morning: 3 pieces
cash = cash + total
print("morning:", total)
total = 2 * price     # evening: 2 pieces
cash = cash + total
print("evening:", total)
total = 4 * price + 10  # delivery: 4 + fee
cash = cash + total
print("delivery:", total)
