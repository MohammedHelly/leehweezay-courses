# كورس 01 · الدرس 01 · حل التمرين: السعر الجديد وعدد التعديلات
# Course 01 · Lesson 01 · Solution: the new price and the number of edits
# Python 3.13 · 2026 · LeehWeEzay (ليه وإزاي)
rice_kg = 25          # global data: stock
cash = 0              # global data: drawer
total = 3 * 35        # lunch: edit 1
cash = cash + total
print("lunch:", total)
total = 2 * 35        # dinner: edit 2
cash = cash + total
print("dinner:", total)
total = 4 * 35 + 10   # delivery: edit 3
cash = cash + total
print("delivery:", total)
total = 5 * 35        # takeaway: edit 4 (new copy)
cash = cash + total
print("takeaway:", total)
print("cash:", cash, "rice:", rice_kg)
