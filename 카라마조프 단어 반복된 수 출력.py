"""
소설 <카라마조프의 형제들> 단어 분석하기

"""
import re

def putdict(D,x) :
    if x in D.keys() :
        D[x] +=1
    else :
        D[x] = 1

myfile = open("kara_small.txt", "r")
M = {}
i=1
for line in myfile :
    line = line.split()
    print("\n i=", i, ": " , end=" ")

    for word in line :
        # 단어에서 영문자만 선택, 각종 기호는 삭제함
        w1 = " ".join(re.findall("[a-zA-Z]+", word))
        w2 = w1.lower()  # 소문자로 통일시킴
        print( w2, end=" ")
        putdict(M,w2)
    i += 1

for s in M :
    print(s,M[s])


myfile.close()