# كورس 01 · درس 04 · فرع من غير data type خاص بيه
# C01 · L04 · a branch with no type of its own · Python 3.13 · 2026
dokki = ("Dokki", 20)              # (name, sugar_kg)
maadi = ("Maadi", 12)

def report(branch):
    print(branch[0], "sugar:", branch[1], "kg")

dokki = (dokki[0], dokki[1] - 5)   # use 5 kg: build a new tuple
report(dokki)
report(maadi)
print(type(dokki))
