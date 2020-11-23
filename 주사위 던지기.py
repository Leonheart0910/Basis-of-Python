import random

for i in range(10):

    a = random.random()
    b = random.random()

    p = int(10*a)
    q = int(10*b)


    if 1<= p <= 6:
        if 1 <= q <= 6:
            print("첫 번째 주사위 = ", p ," ", "두 번째 주사위 =", q)
            print("곱",p*q, "=" ,"dice")
    else:
        print("다시 던지기")

