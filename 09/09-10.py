numbers = list()
result = 0
for i in range(int(input())):
    numbers.append(int(input()))
start_n = int(input())
end_n = int(input())
for i in range(start_n - 1, end_n):
    result += numbers[i]
print(result)
