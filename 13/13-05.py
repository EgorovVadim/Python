dates = dict()
for i in range(int(input())):
    line = input().split()
    dates[line[2]] = line[0]
for i in range(int(input())):
    line = input()
    if line in dates:
        print(dates.get(line))
    else:
        print("")
