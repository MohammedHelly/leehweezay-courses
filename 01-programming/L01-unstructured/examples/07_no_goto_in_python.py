# كورس 01 · درس 01 · التأكد إن goto مش كلمة محجوزة في Python
# C01 · L01 · check: goto is not a Python keyword · Python 3.13 · 2026
import keyword, sys
print(sys.version.split()[0], "goto" in keyword.kwlist,
      "goto" in keyword.softkwlist)
