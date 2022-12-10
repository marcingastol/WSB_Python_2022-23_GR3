zmienna1 = (100, 200, 300, [1, 2])
zmienna2 = (100, 200, 300, [1, 2])

print(zmienna1 == zmienna2)

print(id(zmienna1[-1]))

zmienna1[-1].append(400)
print(zmienna1)

print(id(zmienna1[-1]))

print(zmienna1 == zmienna2)