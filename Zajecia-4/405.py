#kompilacja z python3

def odwracanie(L, left, right):
    r = int((right - left) / 2)
    for i in range(r):
        L[left + i], L[right - i] = L[right - i], L[left + i]
    return L

lista = [i for i in range(13)]
print(odwracanie(lista, 2, 6))

def odwracanie1(L, left, right):
    L[left], L[right] = L[right], L[left]
    if (left + 1 != right):
        odwracanie(L, left + 1, right - 1)
    return L

lista = [i for i in range(10)]
print(odwracanie1(lista, 3, 8))