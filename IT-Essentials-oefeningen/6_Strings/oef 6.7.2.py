import random
# werkt niet
# bug waardoor getal uit het niets veranderd ongeveer 3/4de zin


def encryption(input_text):
    output_text = ""
    encryption_key = ""
    for i in input_text:
        local_encryption_key = random.randint(1, 9)
        output_text += chr(ord(i) + local_encryption_key)
        encryption_key += str(local_encryption_key)
    print(output_text)
    return output_text, int(encryption_key)


def decryption(text):
    input_text, encryption_key = text
    output_text = ""
    letter_selector = 1
    print(encryption_key, "\n")
    for i in input_text:
        local_key = (int(encryption_key / 10**((len(input_text) - letter_selector) * 1)) % 10)
        print(encryption_key)
        print(int(encryption_key / 10**((len(input_text) - letter_selector) * 1)), "\n")
        letter_selector += 1
        output_text += chr(ord(i) - local_key)
    print(output_text)


def main():
    test_sting = "dit is een belangrijke tekst"
    text = encryption(test_sting)
    decryption(text)


if __name__ == "__main__":
    main()
