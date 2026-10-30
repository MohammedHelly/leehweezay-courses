# كورس 01 · الدرس 01 · الطريقة الصحيحة: Find Next ومراجعة كل نتيجة
# Course 01 · Lesson 01 · The right way: review each search match
# Python 3.13 · 2026 · LeehWeEzay (ليه وإزاي)
rice_kg = 25          # global data: stock
cash = 0              # global data: drawer
total = 3 * 30        # lunch: 3 plates
cash = cash + total
print("lunch:", total)
total = 2 * 30        # dinner: 2 plates
cash = cash + total
print("dinner:", total)
total = 4 * 30 + 10   # delivery: 4 + fee
cash = cash + total
print("delivery:", total)
print("cash:", cash, "rice:", rice_kg)
