def input_gen(aantal):
    import random
    output = ""
    for i in range(aantal):
        output += " " + str(random.randint(1, 50))
    return output


def main():
    input_list = input_gen(15)
    input_list = input_list.split()

    gem = 0
    for i in input_list:
        gem += int(i)
    gem = gem / len(input_list)

    kleiner = 0
    for i in input_list:
        if int(i) < gem:
            kleiner += 1

    print("aantal kleiner dan", gem, ":", kleiner)
    print("dat is", (kleiner / len(input_list)) * 100, "percent van de getallen")


if __name__ == "__main__":
    main()
