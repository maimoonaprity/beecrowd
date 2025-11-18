while True:

    try:
        a = input()
        hour = int(a[0])
        min =  int(a[2]+a[3])

        if hour == 7:
            if min == 0:
                print("Atraso maximo: 0")
            elif 0 <= min <= 59 :
                print(f"Atraso maximo: {min}") 

        elif hour == 8:
            if  0<= min <=59 :
                print(f"Atraso maximo: {min+60}")
        elif hour == 9:
            print(f"Atraso maximo: {120}")        

        else:
            print("Atraso maximo: 0")

    except EOFError:
       break
     
