# كورس 01 · درس 03 · خطأ شائع: from ... import *
# C01 · L03 · common mistake: import * · Python 3.13 · 2026
from billing import *
from stock import *

cash = 0
cash = cash + make_bill("morning", 3, 0)
cash = cash + make_bill("evening", 2, 0)
cash = cash + make_bill("delivery", 4, 10)
report(cash)                       # which report?
