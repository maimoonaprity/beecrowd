operation = input()

b = []
for i in range(3):
    a = []
    for i in range(3):
        a.append(float(input()))
    b.append(a)   

result = 0
count = 0
for i in range(3):
    for j in range(3):
        if i < j :
            count = count + 1
            result = result + b[i][j]

if operation == "S":
    print(f"{result:.1f}")

if operation == "M":
    print(f"{(result)/count:.1f}")    


