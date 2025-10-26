n = int(input())
a = [i for i in range(1,10001) if i % n == 2 ]

for i in a:
    print(i)
