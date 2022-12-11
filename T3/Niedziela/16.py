class Klasa:
    iteracja = 0
    def __init__(self):
        Klasa.iteracja += 1
    
    def pusta(self):
        print("jestem tutaj")
    
    @classmethod
    def obiekty(cls):
        print("Klasa ma tyle stworzynych obiektow: ", cls.iteracja)

klasa1 = Klasa()
klasa2 = Klasa()
klasa3 = Klasa()
klasa4 = Klasa()
klasa5 = Klasa()

Klasa.obiekty()