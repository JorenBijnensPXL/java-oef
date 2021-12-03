import random


def perfectGetal(getal):
    delersom = 0
    print("\n"+str(getal))
    for i in range(1, getal):
        if getal % i == 0:
            delersom += i

    if delersom == getal:
        print("perfect getal")
        return True
    else:
        print("geen perfect getal")


def getalgenerator():
    getal = 0
    for i in range(4):
        getal += random.randint(1, 3) * 10**i
    return getal


def main():
    perfect = False
    while not perfect:
        #getal = random.randint(1, 100)
        getal = getalgenerator()
        perfect = perfectGetal(getal)


if __name__ == "__main__":
    main()
