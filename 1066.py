nums = []
for i in range(0,5):
    nums.append(int(input()))

even_count = 0
odd_count = 0
posi_count = 0
neg_count = 0
for i in nums :
    if i & 1 == 0 :
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1
    if i > 0 :
        posi_count = posi_count + 1  
    elif i < 0 :
        neg_count = neg_count + 1  

print(f"{even_count} valor(es) par(es)\n{odd_count} valor(es) impar(es)\n{posi_count} valor(es) positivo(s)\n{neg_count} valor(es) negativo(s)")