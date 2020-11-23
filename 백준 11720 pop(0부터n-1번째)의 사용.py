import sys
a = int(sys.stdin.readline())
n = sys.stdin.readline()
ml = list(n) ; ml.pop(-1)
# 리스트에서 pop(n)는 n-1번째 문자 제거소거
sm = 0
for i in range(a):
    sm += int(ml[i])

print(sm)