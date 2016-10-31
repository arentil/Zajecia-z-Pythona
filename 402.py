#kompilowane z python3


def miar(x):            #miarka
    miarka = "|"
    liczby = "0"
    space = "    "
    for i in range(0, int(x)):
        miarka += "....|"
        if (i == 9):
            space = "   "
        elif (i == 99):
            space = "  "
        elif (i == 999):
            space = " "
            
        liczby += space + str(i+1)
        
    miarka += "\n" + liczby
    return miarka


def rec(s):
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
    return result

dl_miarki = input("Podaj dlugosc miarki:")
print(miar(dl_miarki))
      
prostokat = input("Podaj wymiary prostokata (np.2x4):")
print(rec(prostokat))