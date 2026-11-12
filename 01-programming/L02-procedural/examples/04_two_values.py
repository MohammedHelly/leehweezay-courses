# كورس 01 · درس 02 · function بترجّع قيمتين في tuple
# C01 · L02 · a function that returns two values (a tuple) · Python 3.13 · 2026
def order_info(pieces, price):    # 2 parameters
    total = pieces * price
    grams = pieces * 100          # 100 g per piece
    return total, grams           # 2 values, 1 tuple
print(order_info(4, 30))
total, grams = order_info(4, 30)  # unpack into 2 names
print("total:", total, "weight:", grams, "g")
