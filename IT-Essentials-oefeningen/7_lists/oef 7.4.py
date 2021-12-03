#werkt niet


def main():
    input_string = "Tel hoe vaak iedere letter voorkomt in een string (zonder verschil te maken tussen hoofd- en kleine letters)."
    input_string = input_string.lower()
    input_string = list(input_string)
    print(input_string)
    for i in input_string:
        if ord(i) < ord("a") or ord(i) > ord("z"):
            input_string.remove(i)
    print(input_string)


if __name__ == "__main__":
    main()
