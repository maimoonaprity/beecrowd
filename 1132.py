def multiply(x,y):
    sum = 0
    if x < y:
        for i in range(x, y + 1):
            if i % 13 != 0:
               sum = sum + i
    elif x > y :
        for i in range(y, x + 1):
            if i % 13 != 0:
                sum = sum + i
    else:
        sum = sum            


    return sum

x = int(input())
y = int(input())

print(multiply(x,y))



