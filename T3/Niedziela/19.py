class Kola():
    def __init__(self, rodzaj):
        self.rodzaj = rodzaj

class Szyby():
    def __init__(self, kolor):
        self.kolor = kolor

class Samochod():
    def __init__(self, kola, szyby):
        self.kola = kola
        self.szyby = szyby
    
    def pomoc(self):
        print("Samochod posiada kola ", self.kola.rodzaj, " oraz szyby ",self.szyby.kolor)

michelin = Kola("zimowe")
abc = Szyby("przezroczyste")
audi = Samochod(michelin, abc)

audi.pomoc()