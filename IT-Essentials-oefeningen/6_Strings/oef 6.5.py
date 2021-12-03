def personen (volwassenen, kinderen, kindercode):
    if kindercode.lower() == "a":
        persoon = volwassenen
    else:
        persoon = volwassenen + 0.5 * kinderen
    return persoon


def prijs_berekenen(volwassenen, kinderen, hotelcode, sterren, kindercode):
    prijs = 0
    if hotelcode[:2].lower() == "br" or hotelcode[:2].lower() == "an":
        if hotelcode[:2].lower() == "an":
            prijs = 60 * volwassenen
        else:
            prijs = 60 * personen(volwassenen, kinderen, kindercode)
    else:
        if sterren >= 4:
            prijs = 60 * personen(volwassenen, kinderen, kindercode)
        elif hotelcode[:2].lower() == "hi":
            prijs = 70 * personen(volwassenen, kinderen, kindercode)
        elif sterren >= 3:
            prijs = 56 * personen(volwassenen, kinderen, kindercode)
        else:
            prijs = 48 * personen(volwassenen, kinderen, kindercode)
    return round(prijs, 2)


def main():
    volwassenen = int(input("aantal volwassenen: "))
    kinderen = int(input("aantal kinderen: "))
    hotelcode = input("hotelcode: ")

    while hotelcode != "/":
        print(hotelcode[:2].lower() )
        sterren = int(input("aantal sterren: "))
        kindercode = input("kindercode: ")
        if kindercode.lower() in "abcdefghijklmnopqrstuvwxyz":
            prijs = prijs_berekenen(volwassenen, kinderen, hotelcode, sterren, kindercode)
            print("{:6} {:5} {:4}".format(hotelcode, "*" * sterren, prijs))
        hotelcode = input("hotelcode: ")


if __name__ == "__main__":
    main()
