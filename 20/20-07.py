import sys


code = list(map(str.strip, sys.stdin))
result = list()
pos = 0
for line in code:
    pos += 1
    if "#" in line:
        index = line.find("#")
        temp_line = "Line " + str(pos) + ": " + line[index + 2:]
        result.append(temp_line)
print(*result, sep="\n")