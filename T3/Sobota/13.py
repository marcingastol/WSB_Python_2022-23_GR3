def wiersz(slowo):
    return slowo[::-1]

slowa = ["wiernosc","litosc","milosc","zawsze","dalsze","zlosc","nasze"]

print(sorted(slowa, key=wiersz))