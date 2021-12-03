jaar = int(input("het jaar dat de film uitkwam: "))
rating = int(input("geef de rating (gettal tussen 1 en 5): "))
prijs = 5
huidig_jaar =2021

if rating > 5 or rating < 1 or jaar > huidig_jaar:
    print("geen geldige informatie")
else:
    if (huidig_jaar - jaar) <= 2:
        prijs += 1
        if rating >= 4:
            prijs += 2
        elif rating == 3 or rating == 2:
            prijs += 1
    elif rating >= 4:
        prijs += 2
    elif rating == 3 or rating == 2:
        prijs += 1

    if prijs > 7:
        prijs = 7


    print("de film kost:", prijs)
