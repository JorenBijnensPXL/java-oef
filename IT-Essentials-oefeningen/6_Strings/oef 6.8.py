def driehoek(aantal, begin):
    letter = ord(begin)
    for i in range(aantal + 1):
        for j in range(i):
            if letter <= ord("A") or ord("Z") < letter:
                letter = ord("A")
            print(chr(letter), end=" ")
            letter += 1
        print()



def main():
    aantal = int(input("aantal: "))
    begin_letter = input("begin letter: ").upper()
    driehoek(aantal, begin_letter)


if __name__ == "__main__":
    main()
