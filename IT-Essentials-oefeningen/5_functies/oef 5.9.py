def hotel_kosten(aantal_nachten):
    prijs_per_nacht = 140.5
    prijs_hotel = aantal_nachten * prijs_per_nacht
    prijs_hotel -= prijs_per_nacht * (aantal_nachten // 3)
    return prijs_hotel


def vliegtuig_kosten(stad):
    if stad == "Barcelona" or stad == "barcalona":
        vlucht_prijs = 183
    elif stad == "Rome" or stad == "rome":
        vlucht_prijs = 220
    elif stad == "Berlijn" or stad == "berlijn":
        vlucht_prijs = 125
    else:
        vlucht_prijs = 450

    return vlucht_prijs


def huurauto_kosten(aantal_dagen):
    kost_huurauto = aantal_dagen * 40
    if aantal_dagen >= 7:
        kost_huurauto -= 50
    elif aantal_dagen > 3:
        kost_huurauto -= 20
    return kost_huurauto


def reis_kosten(stad, aantal_dagen):
    prijs_reis = hotel_kosten(aantal_dagen - 1)
    prijs_reis += vliegtuig_kosten(stad)
    prijs_reis += huurauto_kosten(aantal_dagen)
    print("U reis kost", str(prijs_reis) + "euro")


def main():
    stad = input("waar wilt u naar toe? ")
    if stad == "Barcelona" or stad == "barcalona" or stad == "Rome" or stad == "rome" or stad == "Berlijn" or stad == "berlijn" or stad == "Oslo" or stad == "oslo":
        aantal_dagen = int(input("aantal dagen: "))
        reis_kosten(stad, aantal_dagen)
    else:
        print("geen geldige stad")


if __name__ == "__main__":
    main()
