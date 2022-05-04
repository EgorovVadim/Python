for i in range(int(input())):
    line = input().split()
    result = list()
    if len(line) > 1:
        result.append(line[0])
        result.append(line[-1])
        line.remove(line[0])
        line.remove(line[-1])
