def kostprijs(opp, prijs_per_uur, persoon_per_uur_per_opp):
    uren = int((opp / persoon_per_uur_per_opp) + 0.9999999999)
    kost = uren * prijs_per_uur
    return kost


def personen_berekenen(opp, uren_per_persoon, persoon_per_uur_per_opp):
    uren = opp / persoon_per_uur_per_opp
    personen = int((uren / uren_per_persoon) + 0.9999999999)
    return personen


def main():
    opp = float(input("oppervlakte schoon te maken: "))
    persoon_per_uur_per_opp = 160
    uren_per_persoon = 8
    prijs_per_uur = 12.5

    while opp != 0:
        kost = kostprijs(opp, prijs_per_uur, persoon_per_uur_per_opp)
        aantal_personen = personen_berekenen(opp, uren_per_persoon, persoon_per_uur_per_opp)
        print("de kostprijs is:", kost)
        print("er zijn", aantal_personen, "mensen nodig om het op 1 dag te doen\n")
        opp = float(input("oppervlakte schoon te maken: "))


if __name__ == "__main__":
    main()
