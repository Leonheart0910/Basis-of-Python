import random

birth=["boy", "girl"]
bn=0
i=0
while(1):
    i=i+1
    baby=random.choice(birth)
    print("성별",baby)
    bn = bn + 1
    if i == 100 :
        break

print("아이 수 :", bn)


