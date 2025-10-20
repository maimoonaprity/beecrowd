p= list(map(float, input().split()))
p.sort(reverse=True)

a=p[0]
b=p[1]
c=p[2]
if a>=(b+c):
    print("NAO FORMA TRIANGULO")

else:
    if a**2 ==((b**2)+(c**2)):
        print("TRIANGULO RETANGULO") 
    elif a**2>((b**2)+(c**2)): 
         print("TRIANGULO OBTUSANGULO")  
    elif  a**2<((b**2)+(c**2)): 
         print("TRIANGULO ACUTANGULO") 
if a==b==c:
         print("TRIANGULO EQUILATERO")
if a==b!=c or b==c!=a or a==c!=b:
         print("TRIANGULO ISOSCELES")   
# if 
#     
# if a**2>((b**2)+(c**2)):  
#     print("TRIANGULO OBTUSANGULO")  
# if a**2<((b**2)+(c**2)): 
#     print("TRIANGULO ACUTANGULO")
# if a==b==c:
#     
# if a==b!=c or b==c!=a or a==c!=b:
#           



# if A ≥ B + C, write the message: NAO FORMA TRIANGULO
# if A2 = B2 + C2, write the message: TRIANGULO RETANGULO
# if A2 > B2 + C2, write the message: TRIANGULO OBTUSANGULO
# if A2 < B2 + C2, write the message: TRIANGULO ACUTANGULO
# if the three sides are the same size, write the message: TRIANGULO EQUILATERO
# if only two sides are the same and the third one is different, write the message: TRIANGULO ISOSCELES
