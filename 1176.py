


a = 0
b = 1
series= []
series.append(a)
series.append(b)
for i in range(58):
        
    p = a + b
    series.append(p)
    a = b
    b = p 

n = int(input())
for i in range(n):
   x = int(input())
   print(f"fib({x}) = {series[x]}")
         


       