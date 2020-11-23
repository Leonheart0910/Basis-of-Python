b = [1,2,3,4,5] ; k = ["pt", "ct"]
b.append('ss')
print(b)
c = b + [1,2]
print(c)
b.extend(k)
print(b)
b.insert(1,k)
print(b)
