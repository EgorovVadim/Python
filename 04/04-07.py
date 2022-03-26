number = int(input())
answer = ""
for i in range(1, number + 1):
    if number != 1:
        if number % i == 0:
            answer += str(i) + " "
print(answer)
if len(answer) > 5:
    print("НЕТ")
elif len(answer) <= 5 or number == 1:
    print("ПРОСТОЕ")
