def find (lista, wartosc):
    lista2 = []
    ind = 0
    for i in lista:
        if wartosc == i:
            lista2.append(ind)
        ind += 1
    return lista2
print(find([1,2,2,4,2,451,15,2],9))









