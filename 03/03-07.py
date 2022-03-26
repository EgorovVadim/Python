tries = 10
cur_tries = tries
max_number = 11
answer = ""
cur_number = max_number // 2
preveous_number = max_number
temp_preveous_number = 0
while answer != "=" or cur_tries > tries:
    print(cur_number)
    answer = input()
    tries -= 1
    if answer == "<":
        temp = abs(cur_number - preveous_number) // 2
        preveous_number = cur_number
        cur_number -= temp
    if answer == ">":
        temp = abs(cur_number - preveous_number) // 2
        if temp_preveous_number > cur_number:
            preveous_number = temp_preveous_number
        else:
            preveous_number = cur_number
        cur_number += temp
    temp_preveous_number = preveous_number
    print("Осталось попыток: ", tries)
