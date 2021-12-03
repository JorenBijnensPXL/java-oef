def invoercreation():
    colom = []
    for j in range(7):
        colom.append(j+1)
    return colom


def main():
    matrix = []
    for i in range(7):
        #getallen = input("geef de 7 getellen gesplitst door een spatie: ").split()
        getallen = invoercreation()
        getallen_int = []
        for j in getallen:
            j = int(j)
            getallen_int.append(j)
        matrix.append(getallen_int)

    som = 0
    for i in range(len(matrix)):
        if matrix[i][i] == matrix[i][len(matrix) - 1 - i]:
            getal_plus = matrix[i][i]
        else:
            getal_plus = matrix[i][i] + matrix[i][len(matrix) - 1 - i]
        som += getal_plus
    print(som)


if __name__ == "__main__":
    main()
