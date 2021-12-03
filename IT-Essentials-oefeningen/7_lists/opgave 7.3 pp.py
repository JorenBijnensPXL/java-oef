def main():
    input_getal = int(input("een getal: "))
    list_getallen = []

    while input_getal != 0:
        if list_getallen.count(input_getal) == 0:
            list_getallen.append(input_getal)
        else:
            print(input_getal, "staat al op plaats", list_getallen.index(input_getal), "in de lijst")
            list_getallen.remove(input_getal)

        input_getal = int(input("geef nog een getal: "))
    print(list_getallen)


if __name__ == "__main__":
    main()
