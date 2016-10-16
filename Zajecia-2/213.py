line = "znalesc laczna dlugosc wyrazow w napisie line"

count = 0
for w in line.split():
    for c in w:
        count += 1
        
print count
    
