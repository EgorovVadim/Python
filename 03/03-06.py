password = input("Введите пароль: ")
conf_password = input("Введите пароль еще раз: ")
while len(password) < 8:
    print("Короткий!")
    password = input("Введите пароль: ")
    conf_password = input("Введите пароль еще раз: ")
while "123" in password:
    print("Простой!")
    password = input("Введите пароль: ")
    conf_password = input("Введите пароль еще раз: ")
while conf_password != password:
    print("Различаются!")
    password = input("Введите пароль: ")
    conf_password = input("Введите пароль еще раз: ")
print("ОК")
