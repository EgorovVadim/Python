import string
import random


alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits


def generate_password(m):
    result = ""
    for i in range(m):
        result += alphabet[random.randint(0, len(alphabet) - 1)]
    return result


def main(n, m):
    result = list()
    for i in range(n):
        line = ""
        for j in range(m):
            line += alphabet[random.randint(0, len(alphabet) - 1)]
        result.append(line)
    return result

print("Случайный пароль из 7 символов:", generate_password(7))
print("10 случайных паролей длиной 15 символов:")
print(*main(10, 15), sep="\n")
