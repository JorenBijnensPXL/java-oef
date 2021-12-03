def fibonacci(tot):
    getal1 = 1
    getal2 = 0
    while getal1 <= tot:
        print(getal1, end=", ")
        getal1 += getal2
        getal2 = getal1 - getal2


def main():
    tot = 15000
    fibonacci(tot)


if __name__ == "__main__":
    main()
