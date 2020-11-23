import random
random.seed()

def dice():
    return random.randrange(1,7)
    # == return random.randint(1,7)

def yut():
    stick = ['도', '개', '걸', '윷', '모']
    return random.choice(stick)

print("주사위 수 = ", dice())

print("나온 윷가락 = ", yut())