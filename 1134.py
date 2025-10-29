
a = g = d = 0
p = []


while True:
   x = int(input())
   if x == 4:
         break
   p.append(x)
   
   
for i in p:
    if i == 1:
         a = a + 1
    if i == 2:
         g = g + 1   
    if i == 3:
         d = d + 1   

print("MUITO OBRIGADO")
print(f"Alcool: {a}")
print(f"Gasolina: {g}")
print(f"Diesel: {d}")
  
  
      