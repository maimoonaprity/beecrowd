
nums= float(input())
cents= int(nums*100)

list_one=[10000,5000,2000,1000,500,200]
list_two=[100,50, 25, 10, 5,1]

r=cents
def notes(r):

    for i in list_one:
        a= r//i
        print(f"{a} nota(s) de R$ {i/100:.2f}")
        r= r%i
    return r
      
	
print("NOTAS:")           

rr=notes(r)
def coins(rr):
     for i in list_two:
         b= int(rr//i)
         print(f"{b} moeda(s) de R$ {i/100:.2f}")
         rr=rr%i


print("MOEDAS:")
coins(rr)
