n=input('number')
digit=0
n=int(n)
while(n>=1):
    digit=digit+(n%2)
    n=n/2
print("digit",digit)