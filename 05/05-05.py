line = result = 0
while True:
    word = input()
    line += 1
    if "Кот" in word or "кот" in word:
        print(line)
        break
    if word == "СТОП":
        print("-1")
        break
