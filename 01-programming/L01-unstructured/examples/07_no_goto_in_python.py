# كورس 01 · الدرس 01 · Python مفيهاش goto
# Course 01 · Lesson 01 · Check: goto is not a Python keyword
# Python 3.13 · 2026 · LeehWeEzay (ليه وإزاي)
import keyword, sys
print(sys.version.split()[0], "goto" in keyword.kwlist,
      "goto" in keyword.softkwlist)
