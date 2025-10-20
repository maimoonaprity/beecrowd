a,b,c= list(map(float, input().split()))

if a+b>c and b+c>a and a+c>b:
    perimeter=(a+b+c)
    print(f"Perimetro = {perimeter:.1f}")
else:
    area=((a+b)*0.5)*c
    print(f"Area = {area:.1f}") 

