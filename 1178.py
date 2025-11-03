x = float(input())
limit = 100

nums = [x]
for i in range(limit - 1):
    x = x / 2
    nums.append(x)
for i in range(len(nums)):
    print(f"N[{i}] = {nums[i]:.4f}")

