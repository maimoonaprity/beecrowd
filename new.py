seconds_value= int(input())


def time(seconds_value):
    remaining_value= seconds_value
    hour=remaining_value//3600
    if hour>=1:
        remaining_value=remaining_value%3600
    min= remaining_value//60
    if min>=1:
        remaining_value=remaining_value%60
        sec=remaining_value
    else:
        sec=remaining_value 
            
    print(f"{hour}{min}{sec}")        
    



       
      

time(seconds_value)
     
         
          

        

