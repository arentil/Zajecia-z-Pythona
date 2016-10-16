line = "zbudowac napis stworzony z pierwszych i ostatnich znakow napisu line"

napis1 = ""

for w in line.split():  #napis z pierwszych znakow
    napis1 += w[0:1]
    
print napis1
    
napis2 = ""    

for w in line.split():  #napis z ostatnich znakow
    napis2 += w[len(w)-1:len(w)]
    
print napis2
