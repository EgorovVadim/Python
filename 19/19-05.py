vowels = ["a", "e", "i", "o", "u", "y"]
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s",
"t", "v", "w", "x", "z"]


def ask_password(login, password, success, failure):
    vowels_in = 0
    consonants_in = 0
    for char in password.lower():
        if char in vowels:
            vowels_in += 1
        elif char in consonants and char in login:
            consonants_in += 1
    if vowels_in != 3 and vowels_in != consonants_in:
        print("Everything is wrong")
    elif vowels_in != 3:
        print("Wrong number of vowels")
    elif vowels_in != consonants_in:
        print("Wrong consonants")
    success = def_success(login)

def def_success(text):



ask_password("login", "luagon", def_success(login), )
