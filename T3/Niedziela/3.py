generator = (a for a in zip(["abc","def"],["100","200"]))

for x in generator:
    print(x)