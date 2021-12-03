uren = int(input("vertrek uur: "))
minuten = int(input("vertrek minuten: "))
duur = int(input("duur in minuten: "))


for i in range(duur):
    minuten += 1
    if minuten == 60:
        minuten = 0
        uren += 1
        if uren == 24:
            uren = 0

"""
uren_plus = duur // 60
minuten_plus = duur % (60 * uren_plus)

minuten += minuten_plus
if minuten >= 60:
    minuten -= 60
    uren += 1

uren += uren_plus
if uren >= 24:
    uren -= 24
"""
print("de vlucht komt aan om", uren, "uur", minuten)