def apply_move(move, bord, speler):
    if bord[move[0] - 1][move[1] - 1] != "_":
        print("dit vak is al bezet, probeer opnieuw")
        move = geef_rij_kolom()
    rij = bord[move[0] - 1]
    if speler == 1:
        rij[move[1] - 1] = "x"
    else:
        rij[move[1] - 1] = "O"
    bord[move[0] - 1] = rij
    return bord


def create_bord():
    bord = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append("_")
        bord.append(row)
    return bord


def toon_bord(bord):
    print(bord[0])
    print(bord[1])
    print(bord[2])
    print()


def geef_rij_kolom():
    move = []
    str_move = input("geef de rij en kolom geschijden door een space: ").split()
    for j in str_move:
        j = int(j)
        move.append(j)
    while move[0] > 3 or move[1] > 3:
        move = []
        str_move = input("geen geldig invoer, probeer opnieuw: ").split()
        for j in str_move:
            j = int(j)
            move.append(j)
    return move


def winnaar(bord, speler):
    for i in range(len(bord)):
        if (bord[i][0] == bord[i][1] == bord[i][2] and (bord[i][0] == "x" or bord[i][0] == "O")) or (
                bord[0][i] == bord[1][i] == bord[2][i] and (bord[0][i] == "x" or bord[0][i] == "O")) or (
                bord[0][0] == bord[1][1] == bord[2][2] and (bord[0][0] == "x" or bord[0][0] == "O")) or (
                bord[0][2] == bord[1][1] == bord[2][0] and (bord[0][2] == "x" or bord[0][2] == "O")):
            print("speler", speler, "heeft gewonnen")
            return True
        else:
            return False


def main():
    curent_bord = create_bord()
    toon_bord(curent_bord)
    einde = False
    speler = 0
    moves = 0

    while not einde:
        if speler == 1:
            speler = 2
        else:
            speler = 1
        print("speler", str(speler) + ":", end=" ")
        move = geef_rij_kolom()
        curent_bord = apply_move(move, curent_bord, speler)
        toon_bord(curent_bord)
        einde = winnaar(curent_bord, speler)
        moves += 1
        if moves >= 9:
            print("geen winnaar")
            einde = True


if __name__ == "__main__":
    main()
