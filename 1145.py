

x , y = map(int,input().split())


for i in range(1, y + 1, x):
    p = i
    for j in range(1,x+1): 
       if j == x:
           print(p)
       else:    
         print(p,end=" ")
       p = p + 1 
       
        

          
        


        


