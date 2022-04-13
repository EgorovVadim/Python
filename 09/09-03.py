n = int(input())
strings = list()
for i in range(n):
    word = input()
    strings.append(word)
number = int(input())
for elem in strings:
    print(elem[number - 1], end="")
