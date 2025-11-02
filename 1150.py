x = int(input())
z = 0
while z <= x:
    z = int(input())
    if z > x:
        break
s = 0 
cnt = 0   
while s <= z:
    s = s + x
    x = x + 1
    cnt = cnt + 1
    if s > z:
        break

print(cnt)




    


