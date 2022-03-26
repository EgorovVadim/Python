login = input("Укажите желаемый логин от электронный почты: ")
res_mail = input("Укажите резервный адрес электронной почты: ")
if "@" not in login and "@" in res_mail:
    print("OK")
elif "@" in login:
    print("Некорректный логин")
elif "@" not in res_mail:
    print("Некорректный адрес")
    