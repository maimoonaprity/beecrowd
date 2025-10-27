n = int(input())
p = []
num = []
numbers = []
c = 0
r = 0
s = 0

for i in range(n):
    p.append(input().split())

for i in p:
    num.append(i[0])
    if i[1] == "C":
        c = c + int(i[0])
    elif i[1] == "R":
         r = r + int(i[0])
    elif i[1] == "S":
        s = s + int(i[0])       

for i in num:
    numbers.append(int(i))

total = (sum(numbers))

cp = (c/total)*100
rp = (r/total)*100
sp = (s/total)*100

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {c}")
print(f"Total de ratos: {r}")
print(f"Total de sapos: {s}")
print(f"Percentual de coelhos: {cp:.2f} %")
print(f"Percentual de ratos: {rp:.2f} %")
print(f"Percentual de sapos: {sp:.2f} %")



