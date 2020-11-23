a = "우리나라 좋은 나라 흐흐"
b = "좋은 교수님 조환규?? 흐"

t = set(a) ; s = set(b)
print(t)
print(s)

w = t.intersection(s) #교집합 구하기
s = s.union({3})
print(s)
print(w)

sa = set(a.split()) #어절 단위로 끊기
print(sa)