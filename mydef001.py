#약수 구하기
def aliquot(n):
    ml = []
    for i in range(1 , n+1):
        if (n%i == 0):
            ml.append(i)

    return(ml)

n = 100
print(aliquot(n))

