def main():
    text1 = "jens"
    text2 = "jente"
    if len(text2) - len(text1) > 0:
        kortste = text1
    else:
        kortste = text2

    for i in range(len(kortste)):
        if text1[i] == text2[i]:
            print(text1[i], i)


if __name__ == "__main__":
    main()
