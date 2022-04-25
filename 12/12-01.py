for i in range(int(input())):
    word = input().lower()
    if "кот" in word:
        print(i + 1, word.find("кот") + 1)
