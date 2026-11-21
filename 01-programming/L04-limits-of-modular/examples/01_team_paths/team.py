# كورس 01 · درس 04 · قنوات التواصل في الفريق
# C01 · L04 · team communication paths · Python 3.13 · 2026
def paths(n):
    return n * (n - 1) // 2        # one path for every pair

for devs in [2, 5, 10, 20]:
    print("team:", devs, "· paths:", paths(devs))
