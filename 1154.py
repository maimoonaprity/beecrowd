cnt = 0
sum = 0
x = 100

while x > 0:
    x = int(input())
    if x < 0:
        break
    cnt = cnt + 1
    sum = sum + x
print(f"{float(sum/cnt):.2f}")    

   

    


    

