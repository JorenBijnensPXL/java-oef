aantal_artiekels = int(input("aantal artiekes u wil bestellen: "))

prijs = (11.5 * aantal_artiekels) + ((11.5 * aantal_artiekels)/100*21)

if prijs > 1000:
    prijs -= prijs / 100 * 10
print("u betaalt:", prijs)
