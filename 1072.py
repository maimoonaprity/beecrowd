n = int(input())

def user_input(n):
    nums = []
    for i in range(0 , n):
        nums.append(int(input()))
    return nums

outside = 0
inside = 0

for i in  user_input(n):
  
    if i >= 10 and i <= 20:
        inside = inside + 1
    else:
        outside = outside + 1

print(f"{inside} in\n{outside} out")
  