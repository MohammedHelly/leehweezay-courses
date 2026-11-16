# كورس 01 · درس 03 · module الحسابات
# C01 · L03 · billing module · Python 3.13 · 2026
price = 30                         # TODO: move to menu.py

def make_bill(name, pieces, fee):
    total = pieces * price + fee
    if pieces >= 4:                # big-order discount
        total = total - 15
    print(name + ":", total)
    return total

def report(cash):                  # data comes as a parameter
    print("sales today:", cash)
