def x(a, b, c):
    print("x(), a+b+c = ", a+b+c)

for i in range(3):
    x(3, 4 + i, 5)
    x(i, 7, 6 + i + 1)