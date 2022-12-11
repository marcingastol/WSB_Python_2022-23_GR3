class Okrag():
    def __init__(self, srednica):
        self.srednica = srednica

    @property
    def obwod(self):
        return self.srednica * 2


a = Okrag(50)
print(a.srednica)



a.srednica = 20
print(a.srednica)
a.obwod = 30
print(a.obwod)