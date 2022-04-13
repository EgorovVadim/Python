alphabet = "abcdefghijklmnopqrstuvwxyz1234567890_"
word = input()
correct = False
for i in range(len(word)):
    if word[i] in alphabet:
        correct = True
        continue
    else:
        print("Неверный символ: ", word[i])
        correct = False
        break
if correct:
    print("OK")
