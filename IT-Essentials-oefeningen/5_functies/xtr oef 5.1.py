def grerory_leibnitz(aantal):
    tussen_uitkomst = 0
    str_tussen_uitkomst = ""

    for i in range(1,aantal+1):
        if i % 2 != 0:
            tussen_uitkomst += 1/(i * 2 - 1)
        else:
            tussen_uitkomst -= 1 / (i * 2 - 1)
    print(4 * (tussen_uitkomst))


def main():
    aantal = int(input("geef het aantal: "))
    grerory_leibnitz(aantal)


if __name__ == "__main__":
    main()
