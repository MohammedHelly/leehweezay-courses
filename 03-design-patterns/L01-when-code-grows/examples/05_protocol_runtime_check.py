# كورس 03 · درس 01 · مرجع: الـ Protocol والـ type check وقت التشغيل
# C03 · L01 · Protocol runtime check · Python 3.13 · 2026
from typing import Protocol

class Deliverer(Protocol):
    def deliver(self, address: str) -> str: ...

class Bike:
    def deliver(self, address):
        return f"Bike -> {address}"

def run(d: Deliverer) -> str:
    return d.deliver("Shubra")

print(run(Bike()))
try:
    isinstance(Bike(), Deliverer)
except TypeError as e:
    print("TypeError:", e)
