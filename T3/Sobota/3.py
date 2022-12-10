ewa = {'nazwa': 'Ewa Szlachecka', 'urodziny': 1990}

anna = ewa

print(anna is ewa)

print(id(anna))
print(id(ewa))

anna["miejsce"] = "Warszawa"

print(ewa)

ewa = {'nazwa': 'Ewa Szlachecka', 'urodziny': 1990, 'miejsce': 'Warszawa'}

print(anna == ewa)
print(ewa is not anna)