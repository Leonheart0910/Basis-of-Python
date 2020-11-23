import sys
n = sys.stdin.readline()
k = (len(n)//10) + 1
for i in range(k):
    print(n[10*i:10*(i+1)]) #[a:b]기호 주의!
