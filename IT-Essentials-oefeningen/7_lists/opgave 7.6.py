def tel_voorkomens(parameter_list, element):
    print(parameter_list.count(element))
    for i in range(len(parameter_list)):
        if parameter_list[i] == element:
            print(element, "op plek:", i)


def main():
    fruitlist = ["appel", "banaan", "kers", "doerian", "appel"]
    te_zoeken = "appel"
    tel_voorkomens(fruitlist, te_zoeken)


if __name__ == "__main__":
    main()
