import sys
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
d = a*b*c ; d = str(d)
for j in range(10):
    cnt = 0
    for i in range(len(d)):
        if int(d[i]) == j:
            cnt += 1
    print(cnt)



