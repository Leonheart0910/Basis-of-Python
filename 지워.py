infile = open("price.txt" , "r")
outfile = open("total.txt" , "w")


a = infile.readline().split()
a=int(a)
print(a)
infile.close()
outfile.close()
