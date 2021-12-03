sterren = int(input("aantal sterren: "))
code = input(" O (enkel ontbijt), H (half-pension), V (vol pension), A (all-inclusive): ").lower()
overnachtingen = int(input("aantal overnachtingen: "))
seizoen = input("H (hoogseizoen), L (laagseizoen), T (tussenseizoen): ").lower()

een_ster = 30
vierplus_sterren = 55
tweedrie_sterren = 40
ontbijt = 0.2
half = 0.5
vol = 0.6
all_in = 80
korting = 0.1

if sterren == 1:
    prijs = een_ster * overnachtingen
elif sterren >= 4:
    prijs = vierplus_sterren * overnachtingen
else:
    prijs = tweedrie_sterren * overnachtingen

if code == "o":
    if seizoen == "l":
        prijs += prijs * ontbijt - prijs * korting
    else:
        prijs += prijs * ontbijt

elif code == "h":
    if seizoen == "l":
        prijs += prijs * half - prijs * korting
    else:
        prijs += prijs * half

elif code == "v":
    prijs += prijs * vol

else:
    prijs += prijs * vol + all_in

print("u vakantie kost:", prijs)
