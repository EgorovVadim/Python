alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"


def encrypt_caesar(msg, shift=3):
    result = ""
    words = msg.split()
    for word in words:
        for char in list(word):
            if char.lower() in alphabet:
                pos = alphabet.index(char.lower()) + shift
                if pos > 33:
                    pos -= 33
                if char.isupper():
                    result += alphabet[pos].upper()
                else:
                    result += alphabet[pos]
            else:
                result += char
        result += " "
    return result


def decrypt_caesar(msg, shift):
    result = ""
    words = msg.split()
    for word in words:
        for char in list(word):
            if char.lower() in alphabet:
                pos = alphabet.index(char.lower()) - shift
                if pos > 33:
                    pos -= 33
                if char.isupper():
                    result += alphabet[pos].upper()
                else:
                    result += alphabet[pos]
            else:
                result += char
        result += " "
    return result


msg = "Да здравствует салат Цезарь!"
shift = 3
encrypted = encrypt_caesar(msg, shift)
decrypted = decrypt_caesar(encrypted, shift)
print(encrypted)
print(decrypted)

