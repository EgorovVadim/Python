alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
number = int(input())
message = input()
result = ""
for i in message.lower():
    pos = alphabet.find(i) + number
    if i in alphabet:
        result += alphabet[pos]
    else:
        result += i
print(result)
