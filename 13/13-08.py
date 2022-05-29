dictionary = dict()
for i in range(int(input())):
    line = input().split()
    key = line[0]
    line.remove(key)
    value = " ".join(line)
    dictionary[key] = value
for i in range(int(input())):
    line = input()
    if line in dictionary:
        print(dictionary.get(line))
    else:
        print("Нет в словаре")