ml = [0,1,2,3,4]
ml.insert(2,88)# 2번째 수에 99 붙이기
print(ml)

ml.append(99)# 끝에 99 붙이기
print(ml)

ml[0]=99 # 0번째 수가 99로 수정됨
print(ml)

ml.pop(0) # 0번째 소거함
print(ml)

ml.remove(88)# 리스트에 88이란 수를 없앤다.
print(ml)