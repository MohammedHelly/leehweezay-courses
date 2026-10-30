# كورس 03 · درس 01 · حل التمرين: الـ polymorphism للعربيات
# C03 · L01 · solution: polymorphism · Python 3.13 · 2026
# Fixes problem 2 (the vehicle if-chain) with polymorphism.
# Problems 1, 3, 4 stay on purpose: lessons 02-04 fix them.
PLATE_PT = 3500                     # piastres (int)

class Branch:
    def __init__(self, city):
        self.city = city

class CairoDeliveryBranch(Branch): pass
class CairoDineInBranch(Branch): pass
class AlexDeliveryBranch(Branch): pass
class AlexDineInBranch(Branch): pass

class Tuktuk:
    def fee_pt(self):
        return 1000

class Bus:
    def fee_pt(self):
        return 5000

class Bike:                         # new: zero edits below
    def fee_pt(self):
        return 750

class SmsGateway:
    def send(self, text):
        print("REAL SMS SENT:", text)

def egp(pt):
    return f"{pt // 100}.{pt % 100:02d} EGP"

def checkout(branch, vehicle, plates):
    total = plates * PLATE_PT
    if isinstance(branch, (CairoDeliveryBranch,
                           AlexDeliveryBranch)):
        total += vehicle.fee_pt()  # one message
    if isinstance(branch, (AlexDeliveryBranch,
                           AlexDineInBranch)):
        total += 250 * plates
    SmsGateway().send(f"Your bill: {egp(total)}")
    return total

bill = checkout(CairoDeliveryBranch("Cairo"), Tuktuk(), 2)
print(egp(bill))
bill = checkout(AlexDineInBranch("Alex"), None, 3)
print(egp(bill))
bill = checkout(CairoDeliveryBranch("Cairo"), Bike(), 1)
print(egp(bill))
bill = checkout(CairoDineInBranch("Cairo"), Tuktuk(), 2)
print(egp(bill))                    # dine-in: no fee
