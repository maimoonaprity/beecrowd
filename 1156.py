s = 0
n = 1

for i in range(0,20):
    s = s + n/(2**i)
    n = n + 2
print(f"{s:.2f}")    