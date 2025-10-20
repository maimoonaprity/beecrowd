a,b= map(int,input().split())


if a>12 and b<12:
    print(f"O JOGO DUROU {24-a+b} HORA(S)")
elif a==b:
    print(f"O JOGO DUROU {24} HORA(S)")
elif a<12 and b>12: 
    print(f"O JOGO DUROU {abs(a-b)} HORA(S)")
elif a==0 and b<12:
    print(f"O JOGO DUROU {b} HORA(S)")
elif a<12 and b<12:
    print(f"O JOGO DUROU {abs(a-b)} HORA(s)")    
