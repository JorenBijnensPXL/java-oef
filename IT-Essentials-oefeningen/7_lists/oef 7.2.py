def random_num_list(aantal, laagste, hoogste):
    import random
    number_list = []
    for i in range(aantal):
        getal = random.randint(laagste, hoogste)
        number_list.append(getal)
    return number_list


def main():
    hoogste = 10000
    laagste = 0
    aantal = 500
    input_list = random_num_list(aantal, laagste, hoogste)

    groter = 0
    for i in input_list:
        if i > 5000:
            groter += 1

    if groter < 250:
        som = 0
        for i in input_list:
            if i > 5000:
                som += i
        print("som van alle getallen groter dan 5000:", som)
    else:
        som = 0
        for i in input_list:
            if i > 8000:
                som += i
        print("som van alle getallen groter dan 8000:", som)


if __name__ == "__main__":
    main()
