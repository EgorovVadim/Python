import sys
import random


names = list(map(str.strip, sys.stdin))
temp_list = names[:]
i = 1
for name in names:
    number = random.randint(0, len(names) - i)
    if name != temp_list[number]:
        print(name, "-", temp_list[number])
        temp_list.remove(temp_list[number])
        i += 1

print(names)