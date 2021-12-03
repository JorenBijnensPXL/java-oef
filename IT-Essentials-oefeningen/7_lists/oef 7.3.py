def geef_weer(input_list):
    print("de lijst is", len(input_list), "lang en bevat:")
    for i in input_list:
        print(i, end=" ")
    print()


def main():
    aantal = 10
    positieve_getallen = []
    negative_getallen = []

    for i in range(aantal):
        getal = int(input("geef een getal: "))
        if getal >= 0:
            positieve_getallen.append(getal)
        else:
            negative_getallen.append(getal)

    geef_weer(positieve_getallen)
    geef_weer(negative_getallen)



if __name__ == "__main__":
    main()
