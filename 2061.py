a, b = map(int, input().split())
state = []
for i in range(b):
    state.append(input())

for i in state:
    if i == "fechou":
        a += 1
    if i == "clicou": 
        a = a - 1   
print(a)        

