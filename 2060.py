n = int(input())

list_of_nums = list(map(int,input().split()))
a =  b =  c =  d = 0
for i in list_of_nums:
    if i % 2 == 0:
        a += 1
        
    if i % 3 == 0:
        b += 1
        
    if i % 4 == 0:
        c += 1
        
    if i % 5 == 0:
        d += 1 
                      
p = [a, b, c, d]
q = [2 , 3 , 4 , 5]
dict = dict(zip(p, q))


for key, value in dict.items():
    print(f"{key} Multiplo(s) de {value}")