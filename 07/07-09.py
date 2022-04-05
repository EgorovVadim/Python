word = input()
number = int(input())
if number <= len(word):
    print(word[number - 1])
else:
    print("ОШИБКА")
