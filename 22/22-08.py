import string
import random


alphabet_lower = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'p', 'a', 's', 'd', 'f', 'g',
       'h', 'j', 'k', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
alphabet_upper = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'P', 'A', 'S', 'D', 'F', 'G', 'H',
       'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
alphabet_digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
alphabet = alphabet_digits + alphabet_upper + alphabet_lower
result_list = list()
is_correct = False

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
    all_pass = ""
    for i in range(n):
        temp_pass = generate_password(m)
        if temp_pass == None:
            while temp_pass == None:
                temp_pass = generate_password(m)
        is_correct = True
        for j in range(len(temp_pass) - 1):
            if temp_pass[j] in all_pass:
                is_correct = False
        if is_correct:
            all_pass += temp_pass
            result_list.append(temp_pass)
        else:
            n += 1 # проблема, в том что, если в пароле имеются совпадения он пропускает иттерацию. Из за этого не всегода необходимое кол-во паролей
    return result_list


print("Случайный пароль из 7 символов:", generate_password(7))
print("3 случайных паролей длиной 7 символов:")
print(*main(3, 7), sep="\n")