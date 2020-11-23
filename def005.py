def x(a):
    a = 100
    print("x(), a = ", a)

def y(L):
    L.append("99")

a = "book"
x(a)
print("main , a = " , a)

M = [1,2,3,4]
print("M = ",M)
y(M)
print("M = ",M)
