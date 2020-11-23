n = int(input())
a = n%5
b = n//5
while(True):
    if a%3 == 0:
        c = int(a//3)
        d = int(a%3)
        break
    a += 5
    b -= 1
print((d == 0) and (c + b) or -1)