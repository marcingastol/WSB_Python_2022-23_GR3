def funkcja(n):
    """ Moja funkcja ktora zwraca multiplikacje tekstu abc """
    return "abc" if n < 2 else n * funkcja(n-1)

print(funkcja(3))
print(funkcja.__doc__)
print(type(funkcja))