def ask_password():
    tries = 2
    while True:
        line = input()
        if line == "password":
            print("Пароль принят")
            break
        elif tries == 0:
            print("В доступе отказано")
            break
        else:
            tries -= 1
