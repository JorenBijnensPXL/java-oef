def tekenlijn(teken, breete):
    for i in range(breete):
        print(teken, end=" ")
    print()


def tekenrechthoek(teken, hoogte, breete):
    for i in range(hoogte):
        tekenlijn(teken, breete)


teken = "*"
hoogte = 7
breete = 5

tekenrechthoek(teken, hoogte, breete)