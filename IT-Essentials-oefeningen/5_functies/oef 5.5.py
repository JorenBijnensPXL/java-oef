import random

def prijs(lidnummer):
    tweede_cijfer = int(lidnummer / 100000)
    tweede_cijfer = tweede_cijfer % 10
    tweede_cijfer = tweede_cijfer * 10

    vierde_cijfer = int(lidnummer / 1000)
    vierde_cijfer = vierde_cijfer % 10

    getal = tweede_cijfer + vierde_cijfer

    laatste_getallen = lidnummer % 100

    if getal == laatste_getallen:
        return "gratis"
    else:
        return "niet gratis"


def main():
    #lidnummer = int(input("geef u 7 nummer lange lidnummer: "))
    lidnummer = random.randint(1000000, 9999999)
    uitkomst = ""
    teller = 0

    while uitkomst != "gratis":
        print(lidnummer)
        uitkomst = prijs(lidnummer)
        print(uitkomst, "\n")
        #lidnummer = int(input("geef u 7 nummer lange lidnummer: "))
        lidnummer = random.randint(1000000, 9999999)
        teller += 1
    print(teller)


if __name__ == "__main__":
    main()
