class Pies:
    def __init__(self, nazwaPsa):
        self.__nazwa = nazwaPsa

    @property
    def nazwa(self):
        print("Getter")
        return self.__nazwa

    @nazwa.setter
    def nazwa(self, nazwaPsa):
        print("Setter")
        self.nazwa_ukryta = nazwaPsa


pies1 = Pies("Puszek")

#pies1.nazwa = "Puszka"
#print(pies1.nazwa)

print(pies1._Pies__nazwa)