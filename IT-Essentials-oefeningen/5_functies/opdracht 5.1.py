def tekenlijn(teken, aantal):
    for i in range(aantal + 1):
        print(teken, end="")


symbool = input("teken: ")
hoeveelheid = int(input("aantal: "))
tekenlijn(symbool, hoeveelheid)
