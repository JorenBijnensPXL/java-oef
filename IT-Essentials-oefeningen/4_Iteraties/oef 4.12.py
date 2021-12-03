naam = input("familinaam: ")
premie = 0
totaal_premies = 0
hoogste_premie = 0
kans_op_premie = 5
premie_bedrag = 25
top_jaren_in_dienst = 40

while naam != "/" and naam != "*": #beide factoren moeten rekening mee gehouden worden
    voor_naam = input("voornaam: ")
    jaren = int(input("aantal jaren in dienst: "))

    while jaren > 0 and jaren < top_jaren_in_dienst:
        print("geen correct aantal jaren")
        jaren = int(input("aantal jaren in dienst: "))

    if jaren > kans_op_premie:
        premie = jaren * premie_bedrag
    else:
        premie = 0

    totaal_premies += premie
    print("\n"+naam, voor_naam,"\njaren in dienst:",jaren,"\npremie:", premie, "\n")

    if premie > hoogste_premie:
            hoogste_premie = premie


    naam = input("familinaam: ")

print("totaal uit te bepalen premies: ",totaal_premies)
print("de hoogste uit te betalen premie is:", hoogste_premie)