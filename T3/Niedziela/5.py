def jedna(lista):
    for a in lista:
        if isinstance(a,list):
            for b in jedna(a):
                yield b
        else:
            yield a


lista1 = [1,2,[3,4,5],[6,[7,8,9],[]]]

print(jedna(lista1))

print(list(jedna(lista1)))