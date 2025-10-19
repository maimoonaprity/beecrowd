marks=map(float, input().split())
m=list(marks)


weight=[2,3,4,1]


def media(weight,m):
    weighted_value=[]
    for i in range(len(weight)):
           weighted_value.append(m[i]*weight[i])
    avg_sum=(sum(weighted_value))/sum(weight)

    print(f"Media: {avg_sum:.1f}")
    if avg_sum>=7:
      print("Aluno aprovado.")

    if avg_sum>=5.0 and avg_sum<=6.9:
      print("Aluno em exame.")
      a=float(input())
      print(f"Nota do exame: {a:.1f}")
      final=(avg_sum+a)/2

      if final>=5:
         print("Aluno aprovado.")
      if final<=4.9:
         print("Aluno reprovado.")
      print(f"Media final: {final:.1f}")

    if avg_sum<5:
      print("Aluno reprovado.") 
    return avg_sum

media(weight,m)





     

