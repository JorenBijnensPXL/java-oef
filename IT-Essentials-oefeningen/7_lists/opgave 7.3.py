def random_num_list(aantal, laagste, hoogste):
    import random
    number_list = []
    for i in range(aantal):
        getal = random.randint(laagste, hoogste)
        number_list.append(getal)
    return number_list


def main():
    aantal = 20
    laagste = 1
    hoogste = 100

    getallen = random_num_list(aantal, laagste, hoogste)
    laagste_getal = hoogste

    for i in range(len(getallen)):
        if getallen[i] < laagste_getal:
            laagste_getal = getallen[i]
    print(laagste_getal)


if __name__ == "__main__":
    main()
