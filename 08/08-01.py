words = set()
max_word = min_word = ""
permission = False
while True:
    word = input()
    if word == "стоп":
        break
    words.add(word)
for i in words:
    if len(i) > len(max_word):
        max_word = i
    elif len(i) < len(min_word) or len(min_word) == 0:
        min_word = i
for i in range(len(min_word)):
    if min_word[i] not in max_word:
        print("НЕТ")
        permission = False
        break
    else:
        permission = True
if permission:
    print("ДА")
