def teks_omkeerder(text):
    for i in range(len(text), 0, -1):
        print(text[i-1], end="")
    #print(text[-1::-1])

def main():
    text = input()
    print(text)
    teks_omkeerder(text)


if __name__ == "__main__":
    main()
