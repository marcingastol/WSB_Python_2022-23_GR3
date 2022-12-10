lista1 = [1, 2, 3, [100, 200], (10, 20, 30)]
lista2 = list(lista1)

lista1.append(40)
lista1[3].remove(200)

print("lista1: ",lista1)
print("lista2: ",lista2)

lista2[3] += [300,400]
lista2[-1] += (50,)

print("lista1: ",lista1)
print("lista2: ",lista2)