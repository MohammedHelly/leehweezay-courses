# كورس 01 · الدرس 01 · إضافي: الـ Replace All غيّر كمية الرز
# Course 01 · Lesson 01 · Bonus: Replace All changed the rice stock
# Python 3.13 · 2026 · LeehWeEzay (ليه وإزاي)
rice_kg = 35          # global data: stock
cash = 0              # global data: drawer
total = 3 * 35        # lunch: 3 plates
cash = cash + total
print("lunch:", total)
total = 2 * 35        # dinner: 2 plates
cash = cash + total
print("dinner:", total)
total = 4 * 35 + 10   # delivery: 4 + fee
cash = cash + total
print("delivery:", total)
total = 5 * 35        # takeaway: 5 plates (new copy)
cash = cash + total
print("takeaway:", total)
print("cash:", cash, "rice:", rice_kg)
