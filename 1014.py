def avg_consumption(a,b):
    return a/b

a=int(input())
b= float(input())
avg= avg_consumption(a,b)

print(f"{avg:.3f} km/l")