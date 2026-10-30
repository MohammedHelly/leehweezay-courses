# كورس 03 · درس 01 · الـ duck typing: class من غير base class
# C03 · L01 · duck typing · Python 3.13 · 2026
class Vehicle:
    def deliver(self, address):
        return f"{type(self).__name__}: going to {address}"

class Tuktuk(Vehicle):
    def deliver(self, address):
        return f"Tuktuk: back streets to {address}"

class Bike:                               # NO base class
    def deliver(self, address):
        return f"Bike: bread-rack ride to {address}"

fleet = [Tuktuk(), Bike()]
for v in fleet:
    print(v.deliver("Shubra"))

print(isinstance(Bike(), Vehicle))
