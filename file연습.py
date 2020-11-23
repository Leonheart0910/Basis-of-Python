A=open('ki.txt','w')
print("안녕",file=A)
A.close()
print(open('ki.txt').read())