import math


x1,y1= map(float, input().split())
x2,y2= map(float, input().split())

def calculate_distance(x1,y1,x2,y2):
    return math.sqrt(pow((x1-x2),2)+pow((y2-y1),2))
    


d=calculate_distance(x1,y1,x2,y2)
print(f"{d:.4f}")
    

