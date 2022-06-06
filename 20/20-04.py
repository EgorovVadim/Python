import sys


count = 0
code = list(map(str.strip, sys.stdin))
for line in code:
    if "#" in line:
        count += 1

print(count)