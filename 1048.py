salary= float(input())


if salary>0:
    if salary<=400:
        percentage=15
    elif salary>400 and salary<=800:
        percentage=12
    elif salary>800 and salary<=1200:
        percentage=10
    elif salary>1200 and salary<=2000:
        percentage=7
    else:
        percentage=4

       
  

def Salary_increament(salary,percentage):
     increse=(percentage/100)*salary
     final_salary=salary+increse
     print(f"Novo salario: {final_salary:.2f}\nReajuste ganho: {increse:.2f}\nEm percentual: {percentage} %")

           
Salary_increament(salary,percentage)