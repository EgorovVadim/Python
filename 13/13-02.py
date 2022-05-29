numbers = dict()
for i in range(int(input())):
    line = input().split()
    name = line[1]
    number = line[0]
    numbers[name] = number
for i in range(int(input())):
    number_name = input()
    print(numbers.get(number_name))
