def d(n):
    a = 0
    for i in range(0, len(str(n))):
        b = (str(n)) ; b = b[i] ; b = int(b)
        a += b ; c = n + a
    return c

ml = []
for i in range(10000):
    ml.append(d(i))
for i in range(10000):
    if i not in ml:
        print(i)
#------------------------------------

def d(num):
    total = num
    for i in range(0, len(str(num))):
        total += int(num/10**i)%10
        print(total)

    return total

dzip = list()
for i in range(10000):
    dzip.append(d(i))

for i in range(10000):
    if i not in dzip:
        print(i)

