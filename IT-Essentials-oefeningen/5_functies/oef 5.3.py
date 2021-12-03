def senioren(lidgeld, leeftijd, senioren_leeftijd, senioren_korting):
    if leeftijd > senioren_leeftijd:
        lidgeld -= senioren_korting
    return lidgeld


def kinderkost(lidgeld, extra_betalen_kinderen, aantal_kinderen, max_prijs_kinderen):
    if extra_betalen_kinderen * aantal_kinderen <= max_prijs_kinderen:
        lidgeld += extra_betalen_kinderen * aantal_kinderen
    return lidgeld


def trouwheidskorting(lidgeld, huidig_jaar, aansluitingsjaar, trouwheidstatus):
    if huidig_jaar - aansluitingsjaar <= trouwheidstatus:
        lidgeld -= 12.5
    return lidgeld


def klein_inkomen(lidgeld, inkomen):
    if inkomen < 7500:
        lidgeld -= 25
    return lidgeld


def min_lidgeld(lidgeld):
    if lidgeld < 50:
        lidgeld = 50
    return lidgeld


def main():
    naam = input("naam: ")
    senioren_leeftijd = 60
    senioren_korting = 15
    extra_betalen_kinderen = 7.5
    max_prijs_kinderen = 35
    huidig_jaar = 2021
    trouwheidstatus = 20

    while naam != "x" and naam != "X":
        leeftijd = int(input("leeftijd: "))
        aantal_kinderen = int(input("aantal kinderen: "))
        inkomen = float(input("inkomen: "))
        aansluitingsjaar = int(input("aansluitingsjaar: "))
        lidgeld = 100

        lidgeld = senioren(lidgeld, leeftijd, senioren_leeftijd, senioren_korting)
        lidgeld = kinderkost(lidgeld, extra_betalen_kinderen, aantal_kinderen, max_prijs_kinderen)
        lidgeld = trouwheidskorting(lidgeld, huidig_jaar, aansluitingsjaar, trouwheidstatus)
        lidgeld = min_lidgeld(lidgeld)
        lidgeld = klein_inkomen(lidgeld, inkomen)

        print(naam + ":\n"+str(lidgeld), "euro")
        print()

        naam = input("naam: ")


if __name__ == "__name__":
    main()
