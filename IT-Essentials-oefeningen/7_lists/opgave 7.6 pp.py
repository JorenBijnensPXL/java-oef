def cumulatieve_som(aantal):
    getallen = []
    for i in range(aantal):
        getallen.append(i+1)

    lijst = []
    som = 0
    for i in getallen:
        som += i
        lijst.append(som)
    print(lijst)


def main():
    cumulatieve_som(10)


if __name__ == "__main__":
    main()
