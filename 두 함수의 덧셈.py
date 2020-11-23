fa = [4,  0, 0, -1, 2, 3]
fb = [ 6, -1, 0, 0]
k = []
#zip이란 함수
#for i in zip(fa, fb):
#    print(i[0], i[1])

la = len(fa)
lb = len(fb)

# fa.insert(0,99)#insert --> 0번째에 99 란 값을 집어넣어 줍니다.(추가)

if lb > la:
    for i in range(lb - la):
        fa.insert(0,0)
elif la > lb:
    for i in range(la - lb):
        fb.insert(0,0)

print(fa)
print(fb)
q = []
for i in zip(fa, fb):
    c = i[0] + i[1]
    q.append(c)


def fun_add():
    lq = len(q)
    print("L(X)=", end = ' ')
    for i in range(lq):
        if q[i] != 0:
            print(q[i],"x^", lq-i-1,"+",  end=" ")

    return


print(fun_add())

