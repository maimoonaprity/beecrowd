sec_value= int(input())

def time(sec_value):
    hour= sec_value//3600
    remainting_time= sec_value%3600
    min= remainting_time//60
    remainting_time=remainting_time%60
    sec=remainting_time
    print(f"{hour}:{min}:{sec}")


time(sec_value)