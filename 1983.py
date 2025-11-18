n = int(input())
a = []
b = []
for i in range(n):
    p , q = map(float,input().split())
    a.append(p)
    b.append(q)

zipped = zip(a,b)
dictionary = dict(zipped)   

maxi = 7
c = []

if all(i< maxi for i in b):
        print("Minimum note not reached")


else:  
    for i in b:
       if i > maxi:
           c.append(i)
    max_of_c = max(c)
     
    for key, value in dictionary.items():
        if value == max_of_c:
          print(int(key))










