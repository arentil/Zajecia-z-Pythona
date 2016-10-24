L1 = [1,3,4,6,7,9,15,16,3,1,6]
L2 = [2,4,7,16,34,73,75,2,16,73]
a = []
b = []

for i in L1+L2:
    if i not in a:
        a.append(i)
    else:
        b.append(i)
        
print("a): ", a)
print("b): ", b)