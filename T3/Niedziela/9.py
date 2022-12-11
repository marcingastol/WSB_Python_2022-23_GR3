class Osoba():
    def __init__(self, nazwa):
        self.nazwa = "Ojciec ",nazwa

class TelefonOsoba(Osoba):
    def __init__(self, nazwa, telefon):
        super().__init__(nazwa)
        self.telefon = telefon

damian = TelefonOsoba("Damian Abc",123456789)
print(damian.nazwa)
print(damian.telefon)