def funkcja(n):
    """ Moja funkcja ktora zwraca multiplikacje tekstu abc """
    return "abc" if n < 2 else n * funkcja(n-1)

funkcja1 = funkcja
print(funkcja1)

print(funkcja1(4))

print(map(funkcja, range(4)))

print(list(map(funkcja, range(4))))