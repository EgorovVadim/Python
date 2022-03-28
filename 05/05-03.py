line = result = 0
cat_find = False
while True:
    word = input()
    line += 1
    if "Кот" in word or "кот" in word:
        if not cat_find:
            result = line
            cat_find = True
    if word == "СТОП":
        if not cat_find:
            result = -1
        print(result)
        break
