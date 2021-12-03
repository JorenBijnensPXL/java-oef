artikelnummer = int(input("geef het artiekelnummer: "))
totaal_prijs = 0

while artikelnummer != 999:
    hoeveelheid = int(input("hoeveelheid: "))
    eenheidsprijs = int(input("geef de eenheidsprijs: "))
    print("\nartiekelnummer:", artikelnummer, "\nhoeveelheid:", hoeveelheid, "\neenheidsprijs", eenheidsprijs,
          "\nartiekelprijs", eenheidsprijs * hoeveelheid, "\n")
    totaal_prijs += eenheidsprijs * hoeveelheid

    artikelnummer = int(input("geef het artiekelnummer: "))


print("\nhet te betalen bedrag is:", totaal_prijs)