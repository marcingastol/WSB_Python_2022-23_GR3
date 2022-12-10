import copy

class Pociag:
    def __init__(self, pasazer=None):
        if pasazer is None:
            self.pasazer = []
        else:
            self.pasazer = list(pasazer)
    
    def odbieranie(self, name):
        self.pasazer.append(name)

    def wysylanie(self, name):
        self.pasazer.remove(name)

pociag1 = Pociag(["Anna","Bartlomiej","Damian","Daniel"])
pociag2 = copy.copy(pociag1)
pociag3 = copy.deepcopy(pociag1)

print(id(pociag1))
print(id(pociag2))
print(id(pociag3))

pociag1.wysylanie("Damian")
print(pociag2.pasazer)

print(id(pociag1.pasazer))
print(id(pociag2.pasazer))
print(id(pociag3.pasazer))

print(pociag3.pasazer)