from re import *

email = """halo0910@naver.com sub0908@naver.com
        hanmil@nate.net suk9999@daum.net"""

a = findall(r'\b\w+\.\w+\b', email)

for x in a:
    print(a)
