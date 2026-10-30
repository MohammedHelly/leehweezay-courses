# كورس 01 · الدرس 01 · تمرين: أضف حساب سفري بنفس الخطوات
# Course 01 · Lesson 01 · Exercise: add a takeaway bill with the same steps
# Python 3.13 · 2026 · LeehWeEzay (ليه وإزاي)
rice_kg = 25          # global data: stock
cash = 0              # global data: drawer
total = 3 * 25        # lunch: 3 plates
cash = cash + total
print("lunch:", total)
total = 2 * 25        # dinner: 2 plates
cash = cash + total
print("dinner:", total)
total = 4 * 25 + 10   # delivery: 4 + fee
cash = cash + total
print("delivery:", total)
total = 5 * 25        # takeaway: 5 plates (new copy)
cash = cash + total
print("takeaway:", total)
print("cash:", cash, "rice:", rice_kg)
