def rechthoek(lengte, hoogte):
    for i in range(hoogte):
        for j in range(lengte):
            print("*", end=" ")
        print()


def lege_rechthoek(lengte, hoogte):
    for i in range(hoogte):
        for j in range(lengte):
            if i == 0 or i == hoogte - 1:
                print("*", end=" ")
            else:
                if j == 0 or j == lengte - 1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
        print()


def main():
    lengte = 20
    hoogte = 10
    lege_rechthoek(lengte, hoogte)


if __name__ == "__main__":
    main()
