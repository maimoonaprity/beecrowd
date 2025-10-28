
k = -0.2
def fmt(x):
     if x == int(x):
          return int(x)
     else:
          return round(x, 1)     


for i in range(0, 11): 
     k = round(k + 0.2,1)
     for j in range(1, 4):
          p = j + k
          print(f"I={fmt(k)} J={fmt(p)}") 
         

   

       
   