s = input("Podaj wymiary prostokata (np.2x4):")
x = ""
y = ""
flag = False
for i in s:
    if (i == 'x'):
        flag = True
        continue
    
    if (flag):
        x += i
    else:
        y += i

x = int(x)
y = int(y)


width = "+"
height = ""
for w1 in range(0, x):
    width += "---+"
for w2 in range(0, y):
    height += "\n|"
    for h1 in range(0, x):
        height += "   |"
    height += "\n+"
    for h2 in range(0, x):
        height += "---+"
        
result = width + height
print(result)
    