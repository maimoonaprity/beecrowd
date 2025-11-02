n = int(input())
a = 0
b = 1
series = [a,b]
for i in range(1,n-1):
    
    s = a + b
    
    series.append(s)
    a = b
    b = s

for i in series:
    if i == series[len(series)-1]:
        print(i)
    else:    
        print(i, end= " ")    
  


