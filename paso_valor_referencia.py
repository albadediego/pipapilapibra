lista = list(range(1, 11))
numero = 23

def add(l, n):
    for ix in range(len(l)):
        l[ix] += 1


def add_sin_mutar(l, n):
    nl = l[:]
    

def addi(m, n):
    m += n

print(lista) # -> 1,...10
resuadd = add(lista, 1)
print(lista) # -> 1...10
print(resuadd is None) # -> True


print(numero) # 23
resuaddi = addi(numero, 1)
print(numero) # 23
print(resuaddi is None) # -> True
    