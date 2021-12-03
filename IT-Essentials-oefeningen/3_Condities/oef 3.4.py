getal_1 = float(input("geef een getal: "))
getal_2 = float(input("geef een getal: "))

if getal_1 - getal_2 < 0:
    kleinste_getal = getal_1
    grootste_getal = getal_2
else:
    kleinste_getal = getal_2
    grootste_getal = getal_1

print("het kleinste getal is:", kleinste_getal)
print("het kwadraat van het kleinste getal is:", kleinste_getal**2)
if kleinste_getal != 0:
    print("het grootste getal delen door het kleinste getal:", grootste_getal/kleinste_getal)
else:
    print("kan niet delen door 0")