import sys


pupils_list = list(map(str.strip, sys.stdin))
pupils_list = list(map(lambda x: int(x), pupils_list))
print(sum(pupils_list) / len(pupils_list))
