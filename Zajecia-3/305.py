x = input("Podaj dlugosc miarki:")
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
print(miarka)
