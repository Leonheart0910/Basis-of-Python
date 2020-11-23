num = set([1,1,2,3,3,3,4])
num2 = set([2,3,3,3,4,4,5,6])
k = (num-num2)
k.discard(1)
print(k) ; print()
k.add(2)
print(k) ; print()
k.remove(2)
print(k) ; print()
#-----issubset ---> 부분집합을 나타냄

num3 = {6}
print(num3.issubset(num))
print()
print(num3.issubset(num2)) ; print()

#---intersection ---> 교집합을 의미
num4 = num.intersection(num2)
print(num4)