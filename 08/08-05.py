number = int(input())
advices = []
for i in range(number):
    string = input()
    if string[:3] == "Не ":
        advices.append(string[3:])
    else:
        advices.append(string)
print(advices)
