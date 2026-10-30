# كورس 02 · درس 01 · حل التمرين: tool تانية اسمها branch_open
# C02 · L01 · exercise solution: a second tool · Python 3.13 · 2026
# Exercise: add a second tool, branch_open(branch),
# and a PLAN that uses it first. run_agent stays the same.
STOCK = {"koshary_large": 2, "koshary_small": 10}
OPEN = {"dokki": True, "maadi": False}

def check_stock(item):
    return STOCK.get(item, 0)

def branch_open(branch):
    return OPEN.get(branch, False)

TOOLS = {"check_stock": check_stock,
         "branch_open": branch_open}

PLAN = [("branch_open", "maadi"),
        ("branch_open", "dokki"),
        ("check_stock", "koshary_large"),
        ("answer", "Maadi is closed. Dokki has 2 large.")]

def run_agent(choose, max_steps=5):  # unchanged from L01
    history = []
    for step in range(1, max_steps + 1):
        action, arg = choose(history)
        if action == "answer":
            return f"answer: {arg}"
        result = TOOLS[action](arg)
        history.append((action, arg, result))
        print(f"step {step}: {action}({arg}) -> {result}")
    return "stopped: max_steps reached"

def scripted_choices(history):
    return PLAN[len(history)]

print(run_agent(scripted_choices))
