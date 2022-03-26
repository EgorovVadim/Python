count = int(input())
number = 0
for i in range(count):
    if i % 2:
        number += int(input())
    else:
        number -= int(input())
print(abs(number))
