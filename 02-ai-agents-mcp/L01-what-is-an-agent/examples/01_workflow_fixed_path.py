# كورس 02 · درس 01 · الـ workflow: مسار ثابت مكتوب مسبقًا
# C02 · L01 · workflow: a fixed, predefined path · Python 3.13 · 2026
STOCK = {"koshary_large": 2, "koshary_small": 10}

def handle_order(item, qty, backup):
    # fixed path: WE wrote every step in advance
    if STOCK.get(item, 0) >= qty:
        return f"OK: {qty} x {item}"
    if STOCK.get(backup, 0) >= qty:
        return f"OK (backup): {qty} x {backup}"
    return "Sorry: not enough stock"
print(handle_order("koshary_large", 3, "koshary_small"))
print(handle_order("koshary_large", 1, "koshary_small"))
