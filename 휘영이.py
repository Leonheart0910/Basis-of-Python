import re


text = '''
휘영이와 함께 한다는 것은 행복한 일이다. 나의 모질었던
행동들도 그녀를 만나 개과 천선하였으며 그녀를 향하는 내 마음은 새와 하늘 자유를 갈망하는 어린 잎새 와도
같다 사랗했다.......
'''

#pattern = re.compile( "[가-힣]+[은는]" )
#pattern = re.finditer(r'\b(\w+)[와과] (\w+)\b', text)
pattern = re.finditer(r'\b(\w+)[와과]\b', text)
#mlist = re.findall( pattern, text)

for w in pattern :
    print ( w.group(1) )



#pattern = re.compile( "\([가-힝 ]+\)" )
#mlist = re.findall( pattern, text)

#for w in mlist :
#    print ( w )



