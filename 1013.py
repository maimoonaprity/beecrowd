def max_of_firstcomparision(a,b):
    if (((a+b)+abs(a-b))/2)==a:
       return a
    else: 
        return b 
    
def max_of_secondcomparision(c,result_from_first_comparison):
    if    (((result_from_first_comparison+c)+abs(result_from_first_comparison-c))/2)==result_from_first_comparison: 
          return result_from_first_comparison
    else:
        return c
    
a,b,c= input().split()
a=int(a)
b=int(b)
c=int(c)
result_from_first_comparison= max_of_firstcomparision(a,b)
final= max_of_secondcomparision(c,result_from_first_comparison)



print(f"{final} eh o maior")