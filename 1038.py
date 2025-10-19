a,b= map(int,input().split())

price=[4, 4.5, 5, 2, 1.5]

def total(a,b,price):
    for code,value in enumerate(price,start=1):
        if a==code:
            t=value*b
    return t        

q=total(a,b,price)
print(f"Total: R$ {q:.2f}")
# def total(a,b):
#     if a==1:
#       p=b*4
#     if a==2:
#       p=b*4.50
#     if a==3:
#        p=b*5
#     if a==4:
#       p=b*2
#     if a==5:
#        p=b*1.5
#     return p       




