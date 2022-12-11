class Tekst():
    def __init__(self, slowo1):
        self.slowo1 = slowo1

    def __eq__(self, slowo2):
        return self.slowo1.lower() == slowo2.slowo1.lower()

    def __repr__(self):
        return '||| ' + self.slowo1 + ' |||'

    def __str__(self):
        return self.slowo1


a = Tekst("abc") ##########
b = Tekst("ABC")
c = Tekst("qwerty")

print(a.__repr__())
