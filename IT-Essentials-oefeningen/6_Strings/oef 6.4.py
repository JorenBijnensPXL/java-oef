def main():
    text1 = "abc"
    text2 = "ijkml"
    if len(text1) < 4:
        text1 += (4 - len(text1)) * "*"
    if len(text2) < 4:
        text2 += (4 - len(text2)) * "+"
    print(text1[:4].upper() + text2[(len(text2)-4):])


if __name__ == "__main__":
    main()
