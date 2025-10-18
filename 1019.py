seconds_value= int(input())


def time(seconds_value):
    
    if seconds_value//3600>=1:
       
       hour=seconds_value//3600
       remaining_time= seconds_value%3600
       min=remaining_time//60
       remaining_time=remaining_time%60
       sec=remaining_time
       print(f"{hour}:{min}:{sec}")
       

    elif seconds_value//60>=1:

        min= seconds_value//60
        sec=seconds_value%60
        print(f"0:{min}:{sec}")
    else:
        sec=seconds_value 
        print(f"0:0:{sec}")

time(seconds_value)
     
         
          

        

