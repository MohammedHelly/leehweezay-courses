# كورس 02 · درس 01 · شكل الـ agent loop (من غير model)
# C02 · L01 · the shape of an agent loop (no model) · Python 3.13 · 2026
STOCK = {"basbousa_large": 2, "basbousa_small": 10}

def check_stock(item):
    return STOCK.get(item, 0)

TOOLS = {"check_stock": check_stock}

# NOT a model: a fixed list that stands in for
# the model's choices. A model replaces it in L07.
PLAN = [("check_stock", "basbousa_large"),
        ("check_stock", "basbousa_small"),
        ("answer", "Only 2 large. 10 small available.")]

def run_agent(choose, max_steps=5):
    history = []                     # results go back
    for step in range(1, max_steps + 1):
        action, arg = choose(history)
        if action == "answer":
            return f"answer: {arg}"
        result = TOOLS[action](arg)  # OUR code runs it
        history.append((action, arg, result))
        print(f"step {step}: {action}({arg}) -> {result}")
    return "stopped: max_steps reached"

def scripted_choices(history):
    return PLAN[len(history)]

def stuck_choices(history):
    return ("check_stock", "rice_pudding")

print(run_agent(scripted_choices))
print("---")
print(run_agent(stuck_choices, max_steps=3))
