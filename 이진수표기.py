for i in range(1 , 11):

    a = i
    b = a << 4 # << 4 는 2**4를 a 와 곱한다는 뜻
    print(b)
#---------------------------------------#
print()
print("다음은 이진수 구하기 입니다.")

a = 0b111
print(a)
b= 1024
c=bin(b)
print(b,"",c)
