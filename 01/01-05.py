word1 = input("Первая строка: ")
word2 = input("Вторая строка: ")
word3 = input("Третья строка: ")
if ((word1 == "раз" or word1 == "один") and word2 == "два" and word3 == "три") or\
        (word1 == "1" and word2 == "2" and word3 == "3"):
    print("Гори")
else:
    print("Не гори")
