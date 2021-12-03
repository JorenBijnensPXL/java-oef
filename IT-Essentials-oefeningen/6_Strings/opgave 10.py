def strings(input_sting):
    output_string = ""
    for i in input_sting:
        if "a" <= i <= "z":
            output_string += i
        else:
            output_string += " "
    return output_string


def main():
    string = "Een r@ndom 123 StRing"
    nieuwe_string = strings(string)
    print(nieuwe_string)

if __name__ == "__main__":
    main()
