L=[-4,-5,6,-7,10,-9,-11]
n=len(L)
max=0
a=0
b=0
for i in range(n):
    for j in range(i,n):
        if sum(L[i:j+1])>max:
            max=sum(L[i:j+1])
            a=i
            b=j
print(sum(L[a:b+1]),L[a],L[b])

