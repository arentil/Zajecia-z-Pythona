line = "posortowac wyrazy z napisu line raz alfabetycznie"

L = sorted(line.split())    #alfabetycznie

print L

L = sorted(line.split(), key = len) #pod wzgl dlugosci wrazu

print L