money= int(input())
note_list= [100,50,20,10,5,2,1]

def note_count(money):
    remaining_money=money
    for i in note_list:
        c= remaining_money//i
        print(f"{c} nota(s) de R$ {i},00")
        remaining_money=remaining_money%i

print(money)
note_count(money)        
       


