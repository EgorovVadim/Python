line = input().lower()
result = list()
for char in set(line):
    result.append(line.count(char))
print(max(result))

