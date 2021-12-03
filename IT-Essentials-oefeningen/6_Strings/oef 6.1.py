def t_in_text(text):
    teller = 0
    t_gevonden = 0
    for i in text:
        if (i == "t" or i == "T") and t_gevonden == 0 and len(text) % 2 == 0:
            print(text[:teller] + text[teller:].upper())
            t_gevonden = 1
        elif (i == "t" or i == "T") and t_gevonden == 0 and len(text) % 2 != 0:
            print(text[:teller] + text[teller:].lower())
            t_gevonden = 1
        teller += 1

def main():
    input = "Bepaal in een tekst de positie van de eerste t of T. Vervang van dan af alle letters door hoofdletters als de tekst bestaat uit een oneven aantal tekens, door kleine letters als de tekst bestaat uit een even aantal tekens. Geef een gepaste melding als er in de tekst geen t of T voorkomt."
    t_in_text(input)


if __name__ == "__main__":
    main()
