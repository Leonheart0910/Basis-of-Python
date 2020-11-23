cnt = 0

def hnum(n):
    global cnt
    if n//100 - n%100//10 == n%100//10 - n%10:
        cnt += 1
    return cnt

import sys
n = int(sys.stdin.readline())

for i in range(1, n+1):
    if i < 100:
        cnt += 1
    else:
        hnum(i)
print(cnt)
