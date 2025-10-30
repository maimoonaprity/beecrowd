
a = []
while True:

    
    x, y = map(int,input().split())
    if x <= 0 or y <= 0:
            break
    else:
        a.append([x, y])

for i in a: 
     sum = 0 
     for j in range(min(i), max (i) +1):
          sum += j
          if j == max(i):
               print(f"{j} Sum={sum}")
          else:   
              print(j, end=" ")       


   
  

