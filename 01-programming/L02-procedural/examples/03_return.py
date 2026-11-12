# كورس 01 · درس 02 · الـ return: النتيجة بترجع للي استدعى
# C01 · L02 · return: the result goes back to the caller · Python 3.13 · 2026
def pieces_total(pieces, price):  # 2 parameters
    return pieces * price         # send the result back
print(pieces_total(3, 30))
total = pieces_total(4, 30)       # keep the returned value
print(total + 10)                 # use it: add delivery
