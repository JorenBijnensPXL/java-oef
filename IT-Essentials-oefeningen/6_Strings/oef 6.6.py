def hoogte_controle(hoogte):
    while 2 > hoogte or 6 < hoogte:
        hoogte = int(input("geef een geldige hoogte: "))
    return hoogte


def breete_controle(breete):
    while 2 > breete or 8 < breete:
        breete = int(input("geef een geldige breete: "))
    return breete


def opp_poort(hoogte, breete):
    opp = hoogte_controle(hoogte) * breete_controle(breete)
    return opp


def gewicht(hoogte, breete):
    gewicht_poort = opp_poort(hoogte, breete) * 11
    return gewicht_poort


def motor(hoogte, breete):
    gewicht_poort = gewicht(hoogte, breete)
    if gewicht_poort > 300:
        return "x300", 250.5
    elif gewicht_poort < 150:
        return "a101", 120
    else:
        return "a105", 220.5


def prijs_poort(hoogte, breete, speciale_kleur):
    motor_type, motor_prijs = motor(hoogte, breete)
    prijs_poort = opp_poort(hoogte, breete) * 113.5
    if speciale_kleur == "ja":
        prijs_poort = prijs_poort * 1.1 + motor_prijs
    else:
        prijs_poort += motor_prijs
    return prijs_poort


def offerte_nummer(hoogte, breete, naam, speciale_kleur):
    prijs = prijs_poort(hoogte, breete, speciale_kleur)
    prijs = int(prijs)
    naam = naam.upper()
    nummer = "2018_" + naam + "_" + str(prijs)[::-1]
    return nummer


def main():
    naam = "jos"
    hoogte, breete = input("geef de hoogte en breete van de poort: ").split()
    hoogte = float(hoogte)
    breete = float(breete)
    hoogte = hoogte_controle(hoogte)
    breete = breete_controle(breete)
    speciale_kleur = input("speciale kleur ja of nee: ")

    print("\nprijsofferte:")
    print(offerte_nummer(hoogte, breete, naam, speciale_kleur))
    print("opp poort:", opp_poort(hoogte, breete))
    print("gewicht poort:", gewicht(hoogte, breete))
    type_motor, prijs_motor = motor(hoogte, breete)
    print("motor:", type_motor)
    print("totaalprijs:", prijs_poort(hoogte, breete, speciale_kleur))


if __name__ == "__main__":
    main()
