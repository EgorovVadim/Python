numbers = list()
for i in range(int(input())):
    numbers.append(int(input()))
for i in range(len(numbers)):
    if i + 1 < len(numbers):
        print(numbers[i] + numbers[i + 1])
