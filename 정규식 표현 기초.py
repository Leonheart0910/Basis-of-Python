#정규표현식
# 여기를 보세요 http://www.tutorialspoint.com/python/python_reg_expressions.htm
import re

print("banna")
print("\tbanna")
print("\bbanna")
print(r"\tbanna")
print()

text = "AgtcaccgAgttcaagtc"

dna1 = "[agt]"
dna2 = "agt"
dna3 = r"Agt|agt"
dna4 = "[Aa]gt" # == dna3 = r"Agt|agt" 과 같은 의미

print(re.findall(dna1, text))
print(re.findall(dna2, text))
print(re.findall(dna3, text))
print(re.findall(dna4, text))

text = "ban Start Xan[ Bananacake Gpineapple_banana_s :Ban this pigbanana"

all1 = re.findall( r"\b(ban|Ban)", text)
all2 = re.findall(  "\b(ban|Ban)", text) # raw가 아닌 경우와 비교해보자.
all3 = re.findall(  r"\b( ban| Ban)"  , text) # 공백이 먼저 나오는 경우
print("all1=", all1)
print("all2=", all2)
print("all3=", all3)
