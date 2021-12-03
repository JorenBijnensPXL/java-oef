getal_a = int(input("geef een getal a:"))
getal_b = int(input("geef een getal b:"))
code = int(input("code 1: optelling (a+b), code 2: aftrekking (a-b) ,code 3: vermenigvuldiging (a×b), code 4: kwadraat van a, code 5: kwadraat van b: "))

if code == 1:
    result = getal_a + getal_b

elif code == 2:
    result = getal_a - getal_b

elif code == 3:
    result = getal_a * getal_b

elif code == 4:
    result = getal_a**2

elif code == 5:
    result = getal_b**2

else:
    print("geen geldig code")

print("de uitkomst is:",result)