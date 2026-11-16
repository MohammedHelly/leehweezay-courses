# كورس 01 · درس 02 · الحسبة في مكان واحد
# C01 · L02 · the bill in one place · Python 3.13 · 2026
price = 30                         # global data: one price
def make_bill(name, pieces, fee):  # the procedure
    total = pieces * price + fee
    print(name + ":", total)
    return total                   # back to the caller
cash = 0                           # global data: drawer
cash = cash + make_bill("morning", 3, 0)
cash = cash + make_bill("evening", 2, 0)
cash = cash + make_bill("delivery", 4, 10)
print("cash:", cash)
