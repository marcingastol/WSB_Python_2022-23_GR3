class Pies:
    def __init__(self, nazwaPsa):
        self.nazwa_ukryta = nazwaPsa

    def getter(self):
        print("Getter")
        return self.nazwa_ukryta

    def setter(self, nazwaPsa):
        print("Setter")
        self.nazwa_ukryta = nazwaPsa

    nazwa = property(getter, setter)


pies1 = Pies("Puszek")

#pies1.setter("Puszka")
#print(pies1.getter())

pies1.nazwa = "Puszka"
print(pies1.nazwa)