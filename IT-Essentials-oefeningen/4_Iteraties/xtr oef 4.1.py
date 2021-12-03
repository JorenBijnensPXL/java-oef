def prijstabbel(prijs, aantal):
    for i in range(aantal):
        print(i + 1, "jetons =", round(prijs * (i + 1), 2))


def main():
    aantal = 50
    prijs = 0.7
    prijstabbel(prijs, aantal)


if __name__ == "__main__":
    main()
