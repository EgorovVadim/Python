lives = 10
left_border = right_border = temp_border = 0
a = ""
cur_position = int(1000 / 2)
while lives > 0:
    print("Осталось попыток : ", lives)
    print(cur_position)
    a = input("Введите знак: ")
    if a == "<":
        right_border = cur_position
        temp_border = cur_position
    elif a == ">":
        left_border = cur_position
        right_border = temp_border
    elif a == "=":
        break
    cur_position = (left_border + right_border) // 2
    lives -= 1
