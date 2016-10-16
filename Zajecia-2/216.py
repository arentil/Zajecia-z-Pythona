line = "abcdGvR defg"

find = "GvR"
replace = "Guido van Rossum"
index = line.find(find)

line = line[:index] + replace + line[index+len(find):]

print line
