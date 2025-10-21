a,b,c,d= map(int,input().split())

if a <c  and b <=d:
    print(f"O JOGO DUROU {c-a} HORA(S) E {d-b} MINUTO(S)")


elif a <c and b>d:
    print(f"O JOGO DUROU {c-a-1} HORA(S) E {60-(b-d)} MINUTO(S)")    

elif a==b==c==d:
    print(f"O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")

elif a==c and b>d:
    print(f"O JOGO DUROU {24-1} HORA(S) E {60-(b-d)} MINUTO(S)")

elif a==c and b<d:
    print(f"O JOGO DUROU {0} HORA(S) E {d-b} MINUTO(S)")    


elif a>c and b<=d:
    print(f"O JOGO DUROU {24-(a-c)} HORA(S) E {d-b} MINUTO(S)") 

elif a>c and b>d:
    print(f"O JOGO DUROU {24-(a-c)-1} HORA(S) E {60-(b-d)} MINUTO(S)")      
 

