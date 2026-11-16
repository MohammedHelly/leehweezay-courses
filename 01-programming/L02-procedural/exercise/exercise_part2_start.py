# كورس 01 · درس 02 (الجزء 2) · تمرين: حساب عزومة بـ call واحد
# C01 · L02 part 2 · exercise: a party bill with one call · Python 3.13 · 2026
price = 30                         # global data: one price
def make_bill(name, pieces, fee):  # the procedure
    total = pieces * price + fee
    print(name + ":", total)
    return total                   # back to the caller
cash = 0                           # global data: drawer
cash = cash + make_bill("morning", 3, 0)
cash = cash + make_bill("evening", 2, 0)
cash = cash + make_bill("delivery", 4, 10)
# TODO 1: add a party bill (5 pieces) with ONE call
# TODO 2: set price to 35; count the lines you edited
print("cash:", cash)
