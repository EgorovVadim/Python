numbers = input().split()
ranges = input().split()
print(sum([int(numbers[i]) for i in range(int(ranges[0]), int(ranges[1]) + 1)]))