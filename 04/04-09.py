number = int(input())
count = 1
row = ((number * 2 - 1) // 2) + 1
for i in range(1, number + 1):
    print(" " * row, "*" * count)
    count += 2
    row -= 1
