def main():
    bedrag = 400
    geld = 2
    bijkomen = 2.10
    weken = 1
    while geld < bedrag:
        geld += bijkomen
        bijkomen += 0.1
        weken += 1
    print(weken)


if __name__ == "__main__":
    main()
