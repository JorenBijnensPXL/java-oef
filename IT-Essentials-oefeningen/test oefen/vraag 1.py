def werkelijke_voorraad(werkelijke_artikel):

    for i in range(len(werkelijke_artikel)):
        werkelijk_aantal = int(input("geef het werkelijk aantal "))
        if werkelijke_artikel[i][0] == "S":
            werkelijke_artikel.append(werkelijk_aantal)
        else:
            while int(werkelijke_artikel[i][2]) < werkelijk_aantal:
                werkelijk_aantal = int(input("geef het werkelijk aantal "))
            werkelijke_artikel[i].append(werkelijk_aantal)
    return werkelijke_artikel


def lijsten_maken(artikel):
    A_artikel_list = []
    S_artikel_list = []
    for i in range(len(artikel)):
        if artikel[i][0] == "S" and int(artikel[i][3]) > int(artikel[i][4]):
            bijbestelen = int(artikel[i][3]) - int(artikel[i][4])
            while bijbestelen % int(artikel[i][2]) != 0:
                bijbestelen += 1
            S_artikel_list.append(bijbestelen)
        elif artikel[i][0] == "A" and int(artikel[i][3]) != 0:
            A_artikel_list.append(artikel[i])
    return S_artikel_list, A_artikel_list


def show_list(s_list, a_list, artikel):
    print("lijst van bij te bestellen producten:")
    for i in range(len(s_list)):
        print("product", artikel[i][1], ":", s_list[i], "bijbestellen")
    print()
    print("lijst van beschikbare actie producten")
    for j in range(len(a_list)):

        print("artikel", a_list[j][1], "heeft nog", a_list[j][3], "in stock")



def main():
    artikel = ["S-kaftE34-5-100", "S-DVD345-1-124", "A-penD34-125", "S-boekX33-3-256", "A-bal34-145", "S-boekZ34-2-2", "A-ballon34-15"]
    artikel = werkelijke_voorraad(artikel)
    s_list = lijsten_maken(artikel)[0]
    a_list = lijsten_maken(artikel)[1]
    show_list(s_list, a_list, artikel)


if __name__ == "__main__":
    main()
