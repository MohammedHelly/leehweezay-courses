# كورس 03 · درس 01 · الـ polymorphism بالـ inheritance والـ override
# C03 · L01 · inheritance + override · Python 3.13 · 2026
class Vehicle:
    def deliver(self, address):
        return f"{type(self).__name__}: going to {address}"

class Tuktuk(Vehicle):
    def deliver(self, address):           # override
        return f"Tuktuk: back streets to {address}"

class Bus(Vehicle):
    def deliver(self, address):           # override
        return f"Bus: catering boxes to {address}"

class PrivateCar(Vehicle):
    pass                          # base class's deliver

fleet = [Tuktuk(), Bus(), PrivateCar()]
for v in fleet:
    print(v.deliver("Shubra"))
