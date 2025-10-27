n = int(input())
num = []


for i in range(n):
    num.append(list((map(int,input().split()))))

for i in num:
    if i[1]==0:
        print("divisao impossivel")
        continue
    a = i[0]/i[1]
    print(f"{a:.1f}")


