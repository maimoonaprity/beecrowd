#taking multiple input in separate line from user and storing to a list
a=[]
for i in range(1,7):
    a.append(float(input()))

def positive_number(a):
    positive_counter=0
    for number in a:
        if number>0:
            positive_counter=positive_counter+1
    print(f"{positive_counter} valores positivos")     


positive_number(a)




   


    
    
   