age = int(input("u leeftijd: "))
aansluitingsjaar = int(input("het jaar dat u lit werd: "))
huidig_jaar = 2021

if age < 21 or age > 60:
    prijs = 100 -14.5
else:
    prijs = 100

prijs -= 2.5*(huidig_jaar - aansluitingsjaar)

if prijs < 62.5:
    prijs = 62.5

print("u bijdrage is", prijs ,"euro")