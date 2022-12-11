def zewnetrzna(func):
    def wewnetrzna(*args, **kwargs):
        print("Argumenty standardowe: ",args)
        print("Argumenty jako slownik: ",kwargs)
        print("Nazwa funkcji przekazana jako argument: ",func.__name__)
        
        zmienna = func(*args, **kwargs)

        print("Output funkcji: ",zmienna)

        return zmienna
    
    return wewnetrzna


def zewnetrzna1(func):
    def wewnetrzna1(*args, **kwargs):
        zmienna = func(*args, **kwargs)

        print("Jestem tutaj!")

        return zmienna * zmienna
    
    return wewnetrzna1

@zewnetrzna1
@zewnetrzna
def suma(liczba1, liczba2):
    return liczba1 + liczba2

print(suma(5,15))

#suma1 = zewnetrzna(suma)
#suma1(5,15)