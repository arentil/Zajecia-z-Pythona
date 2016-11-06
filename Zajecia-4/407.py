#kompilacja z python3

def flatten(sequence):
    L = []
    for i in sequence:
        if (isinstance(i, (list, tuple))):
            L += flatten(i)
        else:
            L.append(i)
    return L

seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print(seq)
print(flatten(seq))