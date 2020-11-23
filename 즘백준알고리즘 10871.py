import sys
a, b = sys.stdin.readline().split()
a = int(a) ; b = int(b)
n = sys.stdin.readline()
ml = list(map(int, n.split()))
for i, w in enumerate(ml):
    if w < b:
        print(w, end=' ')