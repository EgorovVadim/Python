numbers = list()
result = False
for i in range(int(input())):
    numbers.append(int(input()))
find = int(input())
for i in range(len(numbers)):
    for j in range(len(numbers) - i):
        if (numbers[i] * numbers[j]) == find:
            result = True
if result:
    print("Да")
else:
    print("Нет")
