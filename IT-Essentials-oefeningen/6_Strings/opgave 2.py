def main():
    text = input("een text: ")
    letters = "aeiou"
    """teller = 0
    for i in text:
        if i.lower() in letters:
            print(i,"is op plek",teller)
        teller += 1
        """

    for j in range(len(text)):
        if text[j].lower() in letters:
            print("op plek",j)


if __name__ == "__main__":
    main()
