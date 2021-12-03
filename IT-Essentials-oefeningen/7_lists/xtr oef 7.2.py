def number_to_string(input_number_list):
    string_numbers = ["nul","een","twee","drie","vier","vijf","zes","zeven","acht","negen"]
    number_list = []
    output_list = []
    for i in input_number_list:
        i = int(i)
        number_list.append(i)
    for i in number_list:
        output_list.append(string_numbers[i])
    return output_list


def main():
    number = list(input("geef een getal: "))
    output = number_to_string(number)
    print(output)


if __name__ == "__main__":
    main()
