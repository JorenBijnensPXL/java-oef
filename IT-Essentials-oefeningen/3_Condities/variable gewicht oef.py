gewicht = float(input("gewicht bagage: "))

if gewicht > 20:
    print("er moet 25 eur betaalt worden voor te zware bagage")
elif gewicht == 20:
    print("poeh,net goed")
else:
    print("goede rijs")