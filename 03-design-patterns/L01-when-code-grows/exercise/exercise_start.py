# كورس 03 · درس 01 · تمرين: حدّد المشاكل الأربع في الكود
# C03 · L01 · exercise: find 4 problems · Python 3.13 · 2026
# Money = whole piastres (int). Prices are illustrative.
PLATE_PT = 3500             # large plate = 35.00 EGP

class Branch:
    def __init__(self, city):
        self.city = city

class CairoDeliveryBranch(Branch): pass
class CairoDineInBranch(Branch): pass
class AlexDeliveryBranch(Branch): pass
class AlexDineInBranch(Branch): pass

class Tuktuk: pass
class Bus: pass

class SmsGateway:
    def send(self, text):
        print("REAL SMS SENT:", text)

def egp(pt):
    return f"{pt // 100}.{pt % 100:02d} EGP"

def checkout(branch, vehicle, plates):
    total = plates * PLATE_PT
    if isinstance(branch, (CairoDeliveryBranch,
                           AlexDeliveryBranch)):
        if isinstance(vehicle, Tuktuk):
            total += 1000
        elif isinstance(vehicle, Bus):
            total += 5000
    if isinstance(branch, (AlexDeliveryBranch,
                           AlexDineInBranch)):
        total += 250 * plates       # Alex price difference
    SmsGateway().send(f"Your bill: {egp(total)}")
    return total

bill = checkout(CairoDeliveryBranch("Cairo"), Tuktuk(), 2)
print(egp(bill))
bill = checkout(AlexDineInBranch("Alex"), None, 3)
print(egp(bill))
