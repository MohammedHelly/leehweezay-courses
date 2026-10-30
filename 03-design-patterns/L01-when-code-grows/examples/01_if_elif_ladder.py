# كورس 03 · درس 01 · سلسلة if و elif بتعمل type check على العربية
# C03 · L01 · type-check chain · Python 3.13 · 2026
class Vehicle:
    def __init__(self, plate):
        self.plate = plate

class Tuktuk(Vehicle): pass
class Microbus(Vehicle): pass
class Bus(Vehicle): pass
class PrivateCar(Vehicle): pass

def send(v, address):
    if isinstance(v, Tuktuk):
        return f"Tuktuk: back streets to {address}"
    elif isinstance(v, Microbus):
        return f"Microbus: staff ride to {address}"
    elif isinstance(v, Bus):
        return f"Bus: catering boxes to {address}"
    raise TypeError(f"no rule for {type(v).__name__}")

print(send(Tuktuk("TK-1"), "Shubra"))
print(send(PrivateCar("PC-4"), "Maadi"))
