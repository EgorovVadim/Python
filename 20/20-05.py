import sys


count = 0
code = list(map(str.strip, sys.stdin))
print(any(["0" in line for line in code]))



