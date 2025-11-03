n = int(input())
nums = []

limit = 100//n
remainder = 100 % n
for i in range(limit):
    for j in range(n):
        nums.append(j)
for i in range(remainder):
    nums.append(i)     

for i in range(len(nums)):
    print(f"N[{i}] = {nums[i]}")       

        
