# كورس 01 · الدرس 01 · زيادة السعر: نسخة التوصيل ما اتعدلتش
# Course 01 · Lesson 01 · Price increase: the delivery copy was not updated
# Python 3.13 · 2026 · LeehWeEzay (ليه وإزاي)
rice_kg = 25          # global data: stock
cash = 0              # global data: drawer
total = 3 * 30        # lunch: 3 plates
cash = cash + total
print("lunch:", total)
total = 2 * 30        # dinner: 2 plates
cash = cash + total
print("dinner:", total)
total = 4 * 25 + 10   # delivery: 4 + fee
cash = cash + total
print("delivery:", total)
print("cash:", cash, "rice:", rice_kg)
