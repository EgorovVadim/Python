words = list()
for i in range(int(input())):
    words.append(input())
for i in range(len(words)):
    for j in range(i + 1, len(words)):
        if words[i] > words[j]:
            words[i], words[j] = words[j], words[i]
for elem in words:
    print(elem)
