a= int(input())
b= map(int,input().split())
c=list(b)



def identifying_tea(a,c):
    count=0
    for i in c:
        if i==a:
            count=count+1
    return count

p=identifying_tea(a,c)    
print(p)  