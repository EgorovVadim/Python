n = int(input())
strings = list()
for i in range(n):
    strings.append(input())
number = int(input())
for i in range(number):
    print(strings[int(input()) - 1])
