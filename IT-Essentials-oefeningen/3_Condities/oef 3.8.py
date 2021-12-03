afstand = float(input("geef de afstand van u vlucht: "))
soort_vlucht = input("geef het type van u vlucht( toeristenklasse, charter, zakenreis): ")

if afstand < 1000:
    factor = 0.25

elif afstand > 2999:
    factor = 0.12

else:
    factor = 0.2

prijs = afstand * factor

if soort_vlucht == "charter":
    factor2 = 0.8

elif soort_vlucht == "zakenreis":
    factor2 = 1.3

else:
    factor2 = 1

prijs = prijs * factor2

print("de prijs van u vlucht is", prijs,"euro")
