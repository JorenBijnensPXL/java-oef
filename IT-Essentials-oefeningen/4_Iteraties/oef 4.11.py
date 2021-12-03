personeelnummer = int(input("personeelsnummer: "))
teller_mannen = 0
teller_vrouwen = 0

while personeelnummer != 0:
    geslacht = int(input("geslacht: 0= vrouw; 1= man: "))
    if geslacht == 1 or geslacht == 0:
        leeftijd = int(input(" leeftijd: "))
        brutoloon = float(input("brutoloon: "))

        if geslacht == 1 and (leeftijd > 34 or brutoloon > 1800):
            teller_mannen += 1

        if geslacht == 0 and leeftijd > 25:
            teller_vrouwen += 1
    else:
        print("geen geldig geslacht")
    print()
    personeelnummer = int(input("personeelsnummer: "))


print("\nhet aantal mannelijke personen die ouder zijn dan 34 jaar, of een loon hebben van 1800 euro of meer:", teller_mannen)
print("het aantal vrouwelijke personeelsleden die jonger zijn dan 25 jaar:", teller_vrouwen)

