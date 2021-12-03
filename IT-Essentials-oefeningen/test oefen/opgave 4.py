def main():
    aantal_rijen = int(input("Geef het aantal rijen in "))

    for i in range(aantal_rijen):
        print("\n" + str(i+1),":",end=" ")
        for j in range(i+1):
            print((i+1)*(j+1), end=" ")


if __name__ == "__main__":
    main()
