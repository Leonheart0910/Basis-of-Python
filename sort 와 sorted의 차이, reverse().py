numlist = [6,10, 9, 20, 32]
strlist = ["avici", "Mommy son", "pitbul", "taylor swift", "Yeonja"]

#단지 리버스의 사용은 리스트의 순서를 대칭시키는 용도
numlist.reverse()
print(numlist)

# 오름차순으로 정렬 (작은수부터 큰수대로)---> .sort() 사용
numlist.sort()
print(numlist)

# .reverse()를 사용하면 내림차순 정렬
numlist.reverse()#sort로 오름차순 정렬후 revers사용하였으므로 위reverse와 다름
print(numlist)

# 단 reverse에 true나 1 을 입력시 처음부터 내림차순 정렬 가능
numlist.sort(reverse=True)
print(numlist)

#문자열에서는 마찬가지이나 대문자가 먼저오고 소문자가 나중에 온다
strlist.sort()
print(strlist)

# 대 소문자 구분을 하지 않고 싶을때 key 값 사용
strlist.sort(key=str.lower)
print(strlist)

# sorted 의 차이

numlist2 = sorted(numlist, reverse = 1)# 인자를 넣어 사용가능함
print(numlist2)

strlist2 = sorted(strlist, reverse = 1, key=str.lower)
print(strlist2)




