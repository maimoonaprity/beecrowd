
p= list(map(int,input().split()))
a = p[0]
n = p[1]
while n <= 0:
  for i in p[1:]:
    if i>0:
       n = i
       break
     
      
sum = a
total = a 
for i in range(n-1):
   sum = sum + 1
   total = total + sum
print(total)
   

   


