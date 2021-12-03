def main():
    n = input("geef een random input: ")

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    teller = 0
    for i in n:
        if i.isnumeric() is True:
            teller += int(i)
        elif i in alphabet:
            print(i, "lowercase")
        elif i in alphabet.upper():
            print(i, "uppercase")
        else:
            print("onbekend")
    print("de som van alle cijfers is", teller)


if __name__ == "__main__":
    main()
