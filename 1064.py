
num=[]
for i in range(1,7):
    num.append(float(input()))

posicount=0
sum=0
for i in num:
    if i>0:
        sum=sum+i
        posicount=posicount+1
avg=sum/posicount
print(f"{posicount} valores positivos\n{avg:.1f}")


