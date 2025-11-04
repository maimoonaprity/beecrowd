n = int(input())
print(n)
t = input()
a = []
b = []
for i in range(2):
     
    for j in range(2):
        a.append(float(input()))
    b.append(a)
    a = []

       
final = 0


if t == "S": 
    for i in range(2):
        final = final + b[n][i]
if t == "M":
    for i in range(2):
        final = (final + b[n][i])
    final = final/2
print(f"{final:.2f}")          

