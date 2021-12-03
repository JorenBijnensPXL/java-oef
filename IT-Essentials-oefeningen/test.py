def main():
    getal = 35
    n = 10
    moves_made = 0
    for i in range(n):
        stap = getal - (getal // (n - moves_made))
        moves_made += 1
        print(stap)

if __name__ == "__main__":
    main()
