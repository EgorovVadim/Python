import string
import random


alphabet_lower = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'p', 'a', 's', 'd', 'f', 'g',
       'h', 'j', 'k', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
alphabet_upper = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'P', 'A', 'S', 'D', 'F', 'G', 'H',
       'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
alphabet_digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
alphabet = alphabet_digits + alphabet_upper + alphabet_lower



def generate_password(m):
    password = ""
    alp_low_bool = False
    alp_upp_bool = False
    alp_dig_bool = False
    for i in range(m):
        char = alphabet[random.randint(0, len(alphabet) - 1)]
        password += char
        if len(password) == m:
            for char in list(password):
                if char in alphabet_lower:
                    alp_low_bool = True
                if char in alphabet_upper:
                    alp_upp_bool = True
                if char in alphabet_digits:
                    alp_dig_bool = True
    if alp_dig_bool and alp_upp_bool and alp_low_bool:
        return password


def main(n, m):
    result = list()
    for i in range(n):
        temp_pass = generate_password(m)
        if temp_pass not in result:
            result.append(temp_pass)
        else:
            i -= 1
    return result

print("Случайный пароль из 7 символов:", generate_password(7))
print("10 случайных паролей длиной 15 символов:")
print(*main(10, 15), sep="\n")
