# كورس 01 · درس 03 · حل التمرين: billing بياخد السعر من menu
# C01 · L03 · exercise solution: billing reads menu.price · Python 3.13 · 2026
import menu

def make_bill(name, pieces, fee):
    total = pieces * menu.price + fee
    if pieces >= 4:                # big-order discount
        total = total - 15
    print(name + ":", total)
    return total

def report(cash):                  # data comes as a parameter
    print("sales today:", cash)
