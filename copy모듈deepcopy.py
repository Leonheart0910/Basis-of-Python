a = [1,2,3,4,5]
b = a[:]
c = a
a[0] = 38
print(a)
print(b)
print(c)

print(' '.join([str(i) for i in c]))

#==>

for i in c:
    print(i, end=' ')



#주소를 복사 ==> c = a
#값을 복사==> b = a[:]