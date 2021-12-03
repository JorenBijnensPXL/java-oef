def main():
    fruitlist = ["appel", "banaan", "kers", "mandarijn", "mango"]

    for i in range(len(fruitlist)):
        place_holder = fruitlist[i]
        fruitlist[i] = place_holder.upper()
    print(fruitlist)


if __name__ == "__main__":
    main()
