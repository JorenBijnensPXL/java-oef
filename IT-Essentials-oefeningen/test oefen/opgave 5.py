def main():
    getal = int(input("geef een even getal in "))

    while getal % 2 != 0:
        getal = int(input("Foute ingave! geef een even getal in "))
    for i in range(int(getal/2)):
        print(i + 1, "/", getal - (i + 1))


if __name__ == "__main__":
    main()
