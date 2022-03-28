number = int(input())
for i in range(number):
    word = input()
    if "Кот" in word or "кот" in word:
        print("МЯУ")
        break
else:
    print("НЕТ")
