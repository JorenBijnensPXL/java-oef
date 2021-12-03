startnummer = int(input("startnummer: "))
tijd = 0
snelste_tijd = 35996400
snelste_nummer = startnummer
aantal_renners = 0
renners_over_een_uur = 0


while startnummer >= 0:
    tijd = float(input("tijd in seconden: "))
    aantal_renners += 1
    if tijd < snelste_tijd:
        snelste_tijd = tijd
        snelste_nummer = startnummer
    if tijd > 3600:
            renners_over_een_uur += 1
    startnummer = int(input("startnummer: "))

if aantal_renners > 0:
    uren = snelste_tijd // 3600
    minuten = (snelste_tijd % 3600) //60
    seconden = (snelste_tijd % 3600) % 60

    print("rugnummer", snelste_nummer,"had de snelste tijd met", uren,"uren", minuten,"minuten", seconden,"seconden")
    print(renners_over_een_uur / aantal_renners, "pecent van de renners deet er langer dan een uur over")
