def main():
    text = "abracadabra"
    text = text.replace("a","o")
    print(text)

    teller = 0
    for i in text:
        if i == "o":
            teller += 1
    print(teller)


if __name__ == "__main__":
    main()
