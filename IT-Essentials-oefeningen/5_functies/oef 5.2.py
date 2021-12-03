def schrikkeljaar(jaar):
    if jaar % 4 == 0 and jaar % 100 != 0:
        return True
    elif jaar % 400 == 0:
        return True
    else:
        return False


def main():
    jaar = int(input("geef een jaar: "))

    x = schrikkeljaar(jaar)
    print("schrikkeljaar:", x)


if __name__== "__main__":
    main()