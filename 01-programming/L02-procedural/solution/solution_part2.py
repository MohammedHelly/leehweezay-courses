# كورس 01 · درس 02 (الجزء 2) · حل التمرين: سطرين بس اتعدّلوا
# C01 · L02 part 2 · solution: only 2 lines edited · Python 3.13 · 2026
price = 35                         # edit 1: the new price
def make_bill(name, pieces, fee):  # the procedure
    total = pieces * price + fee
    print(name + ":", total)
    return total                   # back to the caller
cash = 0                           # global data: drawer
cash = cash + make_bill("morning", 3, 0)
cash = cash + make_bill("evening", 2, 0)
cash = cash + make_bill("delivery", 4, 10)
cash = cash + make_bill("party", 5, 0)  # edit 2: one new call
print("cash:", cash)
