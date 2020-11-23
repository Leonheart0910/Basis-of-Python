import sys
n = int(sys.stdin.readline())
cnt = 0 ; sm = 0
for i in range(n):
    score = sys.stdin.readline()
    sl = list(score) ; sl.pop(-1) ; sm = 0 ; cnt = 0
    for k in sl:
        if k == "O":
            cnt += 1
            sm += cnt
        else:
            cnt = 0
    print(sm)

#5
#OOXXOXXOOO
#OOXXOXXOO
#OXOXOXOXOXOXOX
#OOOOOOOOOO
#OOOOXOOOOXOOOOX


