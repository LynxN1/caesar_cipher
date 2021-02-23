import string

letters = string.ascii_lowercase


def encrypt(variation, input_text):
    encrypted = ""
    for i in range(len(input_text)):
        for j in range(len(letters)):
            if input_text[i] == letters[j]:
                if j + variation >= len(letters):
                    encrypted += letters[j + variation - len(letters)]
                else:
                    encrypted += letters[j + variation]
    return encrypted


def decrypt(variation, input_text):
    decrypted = ""
    for i in range(len(input_text)):
        for j in range(len(letters)):
            if input_text[i] == letters[j]:
                if j - variation < 0:
                    decrypted += letters[j - variation + len(letters)]
                else:
                    decrypted += letters[j - variation]
    return decrypted


if __name__ == '__main__':

    text           = input("Text: ")
    shift          = int(input("Shift: "))

    encrypted_text = encrypt(shift, text.lower())
    decrypted_text = decrypt(shift, encrypted_text)

    print("==============================")
    print(f"Encrypted: {encrypted_text}")
    print(f"Decrypted: {decrypted_text}")
    print(f"Shift: {shift}")
    print("==============================")
