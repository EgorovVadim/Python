lives = 10
left_border = 0
right_border = 1000
temp_border = 0
cur_position = int(right_border / 2)
while True:
    if lives <= 0:
        print("У вас не осталось попыток(")
        break
    else:
        print("Осталось попыток : ", lives)
        print(cur_position)
        sign = input("Введите знак: ")
        if sign == "<":
            right_border = cur_position
            temp_border = cur_position
        elif sign == ">":
            left_border = cur_position
            if temp_border != 0:
                right_border = temp_border
        elif sign == "=":
            print("Ваше число: ", cur_position)
            break
        cur_position = (left_border + right_border) // 2
        lives -= 1
