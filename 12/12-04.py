numbers = input().split()
ranges = input().split()
print(sum([int(numbers[i]) ** 2 for i in range(int(ranges[0]), int(ranges[1]) + 1)]))