gewicht_apple = float(input("het gewicht van 1 apple: "))

for i in range(1, 101):
    print(i, "appel(s) =", i * gewicht_apple,"gr")


teller = 0
while teller < 100:
    teller += 1
    print(teller, "appel(s) =", teller * gewicht_apple, "gr")
