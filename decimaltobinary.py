
def decimal_to_binary(n):
    n = 25
    b = []
    while n > 0 :
       b.append(n % 2)
       n = n // 2  
    b.reverse()
    b = list(map(str,b))
    binary_number = "".join(b)
    return binary_number

n = int(input())
print(decimal_to_binary(n))



   







    