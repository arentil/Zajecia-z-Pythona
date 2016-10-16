L = [1, 23, 721, 10, 300, 601, 5, 2, 37, 78]

line = ""

for i in L:
    line += str(i).zfill(3)
    line += " "
    
print line
