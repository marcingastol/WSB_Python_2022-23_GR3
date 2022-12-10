lista1 = [1, 2, 3, (100, 200), [10, 20, 30]]
lista2 = list(lista1)

lista2 = lista1[:]

print(lista2)

print(lista1 == lista2)

print(lista1 is lista2)