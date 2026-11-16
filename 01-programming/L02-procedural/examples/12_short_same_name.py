# كورس 01 · درس 02 (الجزء 2) · Short: نفس الاسم مرتين
# C01 · L02 part 2 · Short: one name, defined twice · Python 3.13 · 2026
cash = 265
sugar_kg = 20
def report():
    print("sales today:", cash)
# ... hundreds of lines later ...
def report():
    print("sugar left:",
          sugar_kg, "kg")
report()
