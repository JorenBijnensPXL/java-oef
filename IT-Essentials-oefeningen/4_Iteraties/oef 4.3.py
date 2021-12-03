getal = int(input("geef een getal: "))
som = 0
aantal_getallen_onder_null = 0

while getal != 0:
    som += getal
    if getal < 0:
        aantal_getallen_onder_null += 1
    getal = int(input("geef een getal: "))

print("de som van de getallen is", som)
print("aantal getallen onder 0:", aantal_getallen_onder_null)
