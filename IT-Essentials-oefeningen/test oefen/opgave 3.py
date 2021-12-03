def bereken_inschrijfgeld(code_student, bedrag):
    if code_student == 3:
        bedrag += (bedrag/100)*10
    elif code_student == 4 or code_student == 5:
        bedrag += (bedrag/100)*30
    elif code_student == 6 or code_student == 7:
        bedrag += (bedrag/100)*40
    else:
        bedrag += 45
    return int(bedrag)


def main():
    code_student = int(input("geef code student in: "))
    inschrijfgeld = bereken_inschrijfgeld(code_student, 600)
    print("het inschrijfgeld voor een student met code", code_student, "is gelijk aan", inschrijfgeld)


if __name__ == "__main__":
    main()
