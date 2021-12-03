foutstatus = 1

while foutstatus == 1:
    getal = int(input("geef een getal tussen 1 en 100: "))
    if getal >= 100 :
        print("geef een getal kleiner dan 100")
    elif getal <= 1:
        print("geef een getal groter of gelijk aan 1")
    else:
        foutstatus = 0
print("het getal is",getal)

#____________________________________
getal = int(input("geef een getal tussen 1 en 100: "))

while getal >= 100 or getal <= 1:
    if getal >= 100 :
        print("geef een getal kleiner dan 100")
    else:
        print("geef een getal groter of gelijk aan 1")
    getal = int(input("geef een getal tussen 1 en 100: "))

print("het getal is",getal)