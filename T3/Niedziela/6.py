class Pies():
    pass


pies1 = Pies()
pies2 = Pies()

pies1.wiek = 5
pies1.nazwa = "Puszek"
pies1.rodzenstwo = pies2

pies2.wiek = 6
pies2.nazwa = "Puszka"
pies2.rodzenstwo = pies1

print(pies1.wiek)
print(pies1.nazwa)
print(pies1.rodzenstwo.nazwa)