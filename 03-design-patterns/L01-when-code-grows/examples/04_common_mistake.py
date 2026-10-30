# كورس 03 · درس 01 · الخطأ الشائع: type() مقابل isinstance
# C03 · L01 · type() vs isinstance · Python 3.13 · 2026
class Tuktuk:
    def deliver(self, address):
        return f"Tuktuk: back streets to {address}"

class ElectricTuktuk(Tuktuk):
    pass

v = ElectricTuktuk()
print(type(v) == Tuktuk)
print(isinstance(v, Tuktuk))
print(v.deliver("Shubra"))
