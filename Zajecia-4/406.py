#kompilacja z python3

def sum_seq(sequence):
    suma = 0
    for i in sequence:
        if (isinstance(i, (list, tuple))):
            suma += sum_seq(i)
        else:
            suma += i
    return suma
    
seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print(seq)
print(sum_seq(seq))