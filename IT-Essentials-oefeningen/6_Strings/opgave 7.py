def main():
    text = "Barefoot on the grass,# listening to our favorite song"
    plaats = text.find("#") + 1
    print (text[plaats:].strip())


if __name__ == "__main__":
    main()
