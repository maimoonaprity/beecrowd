a = []

while True:
    p = int(input())
    if p == 0:
        break
    a.append(p)

for i in a:
    for j in range(1 ,i + 1):
        if j == i:
            print(j)
        else:     
            print(j, end=' ')
    # print("")