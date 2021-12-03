aantal_boeken = int(input("aantal boeken: "))
prijs_per_boek= 24.95-24.95/100*40
kost_verschepingskosten_eerste_boek = 3
kost_verschepingskosten_andere_boek = 0.75
print((prijs_per_boek + kost_verschepingskosten_eerste_boek) + (prijs_per_boek + kost_verschepingskosten_andere_boek) * (aantal_boeken-1),"euro")