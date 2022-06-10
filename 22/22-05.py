import string
import random


alphabet_lower = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'p', 'a', 's', 'd', 'f', 'g',
       'h', 'j', 'k', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
alphabet_upper = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'P', 'A', 'S', 'D', 'F', 'G', 'H',
       'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
alphabet_digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
alphabet = alphabet_digits + alphabet_upper + alphabet_lower
result_list = list()


def generate_password(m):
    result = ""
    for i in range(m):
        result += alphabet[random.randint(0, len(alphabet) - 1)]
    return result


def main(n, m):
    all_pass = ""
    for i in range(n):
        line = ""
        for j in range(m):
            char = alphabet[random.randint(0, len(alphabet) - 1)]
            while char in all_pass:
                char = alphabet[random.randint(0, len(alphabet) - 1)]
            line += char
        result_list.append(line)
        all_pass += line
    return result_list


print("Случайный пароль из 7 символов:", generate_password(7))
print("10 случайных паролей длиной 15 символов:")
print(*main(5, 15), sep="\n")
