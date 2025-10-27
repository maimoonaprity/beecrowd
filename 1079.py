n = int(input())
nums = [] 

for i in range(n):
    nums.append(list(map(float,input().split())))
   
for num in nums:
    a = (num[0]*2)
    b = (num[1]*3)
    c = (num[2]*5)
    d = round((a+b+c)/10,1)
    print(d)
      


