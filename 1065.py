num=[]

for i in range(0,5):
    num.append(int(input()))

count=0
for i in num:
    if i & 1==0:
        count=count+1

print(f"{count} valores pares")       