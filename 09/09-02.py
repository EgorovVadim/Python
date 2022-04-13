n = int(input())
strings = list()
for i in range(n):
    word = input()
    strings.append(word)
search = input()
for elem in strings:
    if search in elem:
        print(elem)
