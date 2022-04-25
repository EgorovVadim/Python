line = input().lower()
max_count = 0
char = ""
for i in range(len(line)):
    count = line.count(line[i])
    if count > max_count:
        max_count = count
        char = line[i]
print(char)