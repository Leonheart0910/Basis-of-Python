def swap3(a, b, c):
    return(b, c, a)

a, b, c = 4, 7, 10
print(a, b, c)

Q = swap3(a, b, c)
print("before = " , Q)
Q = a, b, c

print("after =" , a, b, c)
""