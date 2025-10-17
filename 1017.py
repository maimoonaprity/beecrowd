


def fuel_needed(a,b):
    return (a*b)/12

a= int(input())
b=int(input())
fuel= fuel_needed(a,b)
print(f"{fuel:.3f}")