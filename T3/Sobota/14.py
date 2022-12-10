def funkcja(n):
    """ Funkcja do obliczenia silni """
    return 1 if n < 2 else n * funkcja(n-1)

print(list(map(funkcja, range(5))))

print([funkcja(n) for n in range(5)])

print(list(map(funkcja, filter(lambda n: n % 2, range(5)))))

print([funkcja(n) for n in range(5) if n % 2])