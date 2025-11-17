dict = {
    1 : "I",
    4 : "IV",
    5 : "V",
    9 : "IX",
    10 : "X",
    40: "XL",
    50 : "L",
    90: "XC",
    100 : "C",
    400: "CD",
    500: "D",
    900:"CM",
    1000: "M"

}
nums = [1000,900,500,400,100,90,50,40,10,9,5,4,1]


n = int(input())

     
p = []

for i in nums:
    
      p.append(n//i)
      n = n % i
roman = ''
for count, value in zip(p, nums):
      for _ in range(count):
        roman = roman + dict[value]
print(roman)
     

            
      


