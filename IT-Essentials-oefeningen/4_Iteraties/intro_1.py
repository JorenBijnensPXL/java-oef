klas_leeftijd = 0
teller = 0
studenten = 28

for i in range(studenten):
    klas_leeftijd += int(input("geef u leeftijd: "))
    teller += 1

gem_leeftijd = klas_leeftijd / teller
print(gem_leeftijd)
