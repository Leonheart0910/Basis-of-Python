import calendar ; import sys
a, b = sys.stdin.readline().split()# 문자열로 받음
a = int(a) ; b = int(b)
l = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
c = calendar.weekday(2007, a, b)
print(l[c])