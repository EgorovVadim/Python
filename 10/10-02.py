names = list()
for i in range(int(input())):
    names.append(input())
for elem in names:
    print(elem)
print()
for elem in names:
    if int(elem[-1]) > 3:
        print(elem)
