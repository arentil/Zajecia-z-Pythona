line = "Znalezc najdluzszy wyraz oraz dlugosc najdluzszego wyrazu w napisie line"

wyraz = ""

for w in line.split():
    if (len(w) > len(wyraz)):
        wyraz = w
    else:
        continue
    
print "wyraz: ", wyraz
print "dlugosc:", len(wyraz)
