import sys


code = list(map(str.strip, sys.stdin))
print(*sorted(code, key=lambda word: sum([(ord(i) - ord("A") + 1) for i in word.upper()])), sep='\n')
