line = input().split()
result = 0
for elem in line:
    if elem == "+":
        x2 = line[0]
        x1 = line[1]
        result = int(x1) + int(x2)
        line = [result] + line[2:]
    elif elem == "*":
        x2 = line[0]
        x1 = line[1]
        result = int(x1) * int(x2)
        line = [result] + line[2:]
    elif elem == "-":
        x2 = line[0]
        x1 = line[1]
        result = int(x1) - int(x2)
        line = [result] + line[2:]
    elif elem == "/":
        x2 = line[0]
        x1 = line[1]
        result = int(x1) // int(x2)
        line = [result] + line[2:]
    else:
        line = [elem] + line
print(line[0])