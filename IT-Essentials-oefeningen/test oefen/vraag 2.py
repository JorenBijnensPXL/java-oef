def basisscore(naam, geboorte_jaar):
    score = 0
    plaats = 0
    for i in naam:
        plaats += 1
        if i in "cinema":
            score += (ord(i) * plaats)
    return score + geboorte_jaar


def score(punten, keer, snack):
    if keer == 1:
        punten = punten / 2
    elif keer == 2:
        punten = punten * 2
    else:
        punten = punten * 3

    if snack == "N" and (keer == 1 or keer == 2):
        punten -= 1050

    return punten


def prijs():
    import random
    getal = random.randint(1000, 9999)
    while getal % 10 == 0 or (getal > 5000 and getal % 2 != 0):
        getal = random.randint(1000, 9999)
    print(getal)
    str_getal = list(str(getal))
    tickets = 0
    for i in str_getal:
        tickets += int(i)
    print("u wint:", tickets, "tickets")


def main():
    naam = input("geef u naam: ")
    hoogste_punten = 0
    winaar_naam = ""
    while naam != "xxx" and naam != "qqq":
        jaar = int(input("In welk jaar bent u geboren: "))
        keer_naar_cinema = int(input("hoe vaak gaat u naar de cinema: "))
        snack = input("- Welke versnapering nuttig je in kinepolis: P = popcorn, C = chips, N = niets: ")
        punten = basisscore(naam, jaar)
        punten = score(punten, keer_naar_cinema, snack)
        if punten > hoogste_punten:
            winaar_naam = naam
            hoogste_punten = punten
        naam = input("geef u naam: ")

    print("de winaar is", winaar_naam)
    print("de winnende score is:", hoogste_punten)
    prijs()


if __name__ == "__main__":
    main()
