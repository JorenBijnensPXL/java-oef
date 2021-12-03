def convertion(euro_to_dollar, value):
    dollar_value = value * euro_to_dollar
    print(round(dollar_value, 2),"\n")


def main():
    euro_to_dollar = float(input("de wisselkoers van euro naar dollar: "))
    bedrag = float(input("het bedrag om om te zetten: "))

    while bedrag != 0:
        convertion(euro_to_dollar, bedrag)
        bedrag = float(input("het bedrag om om te zetten: "))


if __name__=="__main__":
    main()