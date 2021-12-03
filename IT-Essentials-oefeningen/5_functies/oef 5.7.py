def boete_berekenen(boeken, overschreden):
    boeten = overschreden * 0.07 * boeken
    if overschreden / 45 > 1:
        boeten += (overschreden // 45) * 0.84
    boeten = round(boeten, 2)
    return boeten


def aantal_brievenberekenen(overschreden):
    aantal_brieven = (overschreden // 45)
    return aantal_brieven


def main():
    naam = input("naam: ")
    overschreden = 0
    while naam != "xx":
        boeken = int(input("aantal boeken: "))
        overschreden = int(input("aantal dagen over limiet: "))

        print("\nnaam:", naam)
        print("boeten:", boete_berekenen(boeken, overschreden), "\n")

        naam = input("naam: ")
    print("aanmaningsbrieven:", aantal_brievenberekenen(overschreden))


if __name__ == "__main__":
    main()
