number = input()
while True:
    number = str(int(number) * int(number[0]))
    if number[0] == "1" or int(number) >= 1000000000:
        print(number)
        break
