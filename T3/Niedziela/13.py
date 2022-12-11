class Pies:
    def __init__(self, nazwaPsa):
        self.nazwa_ukryta = nazwaPsa

    @property
    def nazwa(self):
        print("Getter")
        return self.nazwa_ukryta

    @nazwa.setter
    def nazwa(self, nazwaPsa):
        print("Setter")
        self.nazwa_ukryta = nazwaPsa


pies1 = Pies("Puszek")

pies1.nazwa = "Puszka"
print(pies1.nazwa)