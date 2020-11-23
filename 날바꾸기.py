
import time

Kday = {'Mon' : '월', 'Sun' : '일', 'Tue' : '화', 'Wed' : '수', 'Thu' : '목', 'Fri' : '금', 'Sat' : '토'}
Kmonth = {'Jan' : '1', 'Feb' : '2', 'Mar' : '3', 'Apr' : '4', 'May' : '5', 'Jun' : '6', 'Jul' : '7', 'Aug':'8', 'Sep':'9', 'Oct':'10', 'Nov':'11', 'Dec':'12'}

now = time.ctime().split()
now2 = list(now)
print(now2)

k = now2[3].split(':')

T = """
------------------
사용자 여러분
지금 시간은 %d년 %s월 %d일,
%s 요일 시각은 %s시 %s 분 입니다.
오늘 즐거운 하루가 되시기 바랍니다.
------------------
"""


print(T % (int(now2[-1]), Kmonth[now[1]], int(now[2]), Kday[now[0]], k[3]))
