import math
a,b,c= map(float,input().split())

d=(b**2)-(4*a*c)
def finding_root(a,b,c,d):
    if((a==0)or(d<0)):
        print("Impossivel calcular")
    else:
        root1= (-b+math.sqrt(d))/(2*a)  
        root2= (-b-math.sqrt(d))/(2*a) 
        print(f"R1 = {root1:.5f}",f"R2 = {root2:.5f}",sep="\n") 

finding_root(a,b,c,d)        