n = int(input())
def user_input(n):
    nums = []
    for i in range(0 , n):
        nums.append(int(input()))
    return nums    

for i in user_input(n):
    if i > 0:
        if i & 1 == 0:
            print("EVEN POSITIVE")
        elif i & 1 == 1:
            print("ODD POSITIVE")
    if i < 0:
        if i & 1 == 0:
            print("EVEN NEGETIVE")
        elif i & 1 == 1:
            print("ODD NEGETIVE")
    elif i == 0:
        print("NULL")        
        

        


 