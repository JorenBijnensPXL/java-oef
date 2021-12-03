def remove_dubble(input_list):
    for i in input_list:
        if input_list.count(i) > 1:
            input_list.remove(i)
    print(input_list)

def main():
    fruitlist = ["appel", "banaan", "kers", "doerian", "appel", "kers"]
    remove_dubble(fruitlist)


if __name__ == "__main__":
    main()
