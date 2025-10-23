x = int(input())
y = int(input())
if x>y:
   temp = x
   x = y
   y = temp


sum = 0
for i in range(x+1,y):
    if i & 1 == 1:
        sum = sum + i
print(sum)
