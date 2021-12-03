import random


def encryption(input_text):
    encryption_key = random.randint(1, 12) * 2
    output_text = ""
    for i in input_text:
        output_text += chr(ord(i) + encryption_key)
    print(output_text)
    return output_text, encryption_key


def decryption(text):
    input_text, encryption_key = text
    output_text = ""
    for i in input_text:
        output_text += chr(ord(i) - encryption_key)
    print(output_text)


def main():
    test_sting = "dit is een belangrijke tekst"
    text = encryption(test_sting)
    decryption(text)


if __name__ == "__main__":
    main()
