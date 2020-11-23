import calendar

yobi = ["일요일","화요일","수요일","목요일","금요일","토요일"]
m = [31,28,31,30,31,30,30,31,30,31,31,31]
s = 0

for i,w in enumerate(m):
    total.append(s)
    s += w

def day(a,b):
    c = calendar.weekday(2019,a,b)
    d = yobi[c]
    return(d)

def count(dal, nal):
    return(total[dal - 1]+nal)#dal에 -1 이유는 1월부터 시작하기 때문

k = ["월요일","화요일","수요일","목요일","금요일","토요일","일요일"]
def future(a,b,c):#a,b현재 날짜와 일 -->c == 며칠 뒤인가?
    t = (count(a,b)+c)%7
    return(k[t])

print(count(5,1))
print(day(5,1))
print(future(5,1,49))