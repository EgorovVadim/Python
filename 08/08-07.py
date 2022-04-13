number = int(input())
for i in range(number):
    word = input()
    if "кот" in word.lower():
        print(i + 1, word.lower().find("кот") + 1)
