x = []
for i in range(5):
    x.append(int(input()))

max = x[0]
for i in x:
    if i>max:
        max = i
        index = x.index(i)

print(max)
print(index+1)