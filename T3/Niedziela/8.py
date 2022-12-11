class Pies():
    def szczekanie(self):
        print("hau hau")

class Szczeniak(Pies):
    def szczekanie(self):
        print("hau hau hau hau")

    def aportowanie(self):
        print("hi hi hi")

#print(issubclass(Szczeniak, Pies))

Pies1 = Pies()
Szczeniak1 = Szczeniak()

Szczeniak1.szczekanie()
