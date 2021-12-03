import random


def getal_check(getal, te_raden_getal):
    if getal < te_raden_getal:
        print("hoger")
        return False
    elif getal > te_raden_getal:
        print("lager")
        return False
    else:
        print("proficiat, getal geraden")
        return True


def main():

    geraden = False
    teller = 0
    te_raden_getal = random.randint(1, 10)
    while not geraden and teller < 4:
        getal = int(input("raad een getal: "))
        geraden = getal_check(getal, te_raden_getal)
        teller += 1


if __name__ == "__main__":
    main()
