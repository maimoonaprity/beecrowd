n = int(input())

for i in range(n):
    s = 0
    a = 0
    x , y = map(int,input().split())
    if x % 2 == 1:
        a = x
    elif x % 2 == 0:
        a = x + 1   

    for i in range(y):
        s = s + a + 2*i

    print(s)         
        
               
           

  
