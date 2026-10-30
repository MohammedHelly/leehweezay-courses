# كورس 01 · الدرس 01 · السعر في variable واحد: الخطوات لسه مكررة
# Course 01 · Lesson 01 · Price in one variable: the steps are still copied
# Python 3.13 · 2026 · LeehWeEzay (ليه وإزاي)
rice_kg = 25          # global data: stock
cash = 0              # global data: drawer
price = 30            # global data: one price
total = 3 * price     # lunch: 3 plates
cash = cash + total
print("lunch:", total)
total = 2 * price     # dinner: 2 plates
cash = cash + total
print("dinner:", total)
total = 4 * price + 10  # delivery: 4 + fee
cash = cash + total
print("delivery:", total)
