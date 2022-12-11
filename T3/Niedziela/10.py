class Zwierzeta:
    def glos(self):
        return "ja mowie"
    
class Malpa(Zwierzeta):
    def glos(self):
        return "hi ha"

class Kon(Zwierzeta):
    def glos(self):
        return "hi hi hi hi"

class Kot(Kon, Malpa):
    pass

class Pies(Malpa, Kon):
    pass

#print(Pies.mro())

kot1 = Kot()
print(kot1.glos())

pies1 = Pies()
print(pies1.glos())