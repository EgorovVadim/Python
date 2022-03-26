number = int(input("Ваше число: "))
for i in range(16):
    divider = int(input())
    if number % divider == 0:
        print("ДА")
    else:
        print("НЕТ")
