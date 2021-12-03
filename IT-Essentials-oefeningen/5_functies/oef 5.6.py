import random


def reeks_creator(reeksnummer, aantal_per_reeks, hoogste_getallen):
    print("\nreeks", reeksnummer)
    aantal_oef = 1

    while aantal_oef <= aantal_per_reeks:
        getal_1 = random.randint(0, hoogste_getallen)
        getal_2 = random.randint(0, hoogste_getallen)
        if getal_1 - getal_2 >= 0:
            print(str(aantal_oef)+")", getal_1, "-", getal_2, "=")
            aantal_oef += 1


def main():
    aantal_per_reeks = 5
    hoogste_getal = 20
    aantal_reeksen = 5

    reeksnummer = 1
    while reeksnummer <= aantal_reeksen:
        reeks_creator(reeksnummer, aantal_per_reeks, hoogste_getal)
        reeksnummer += 1


if __name__ == "__main__":
    main()