max_len = int(input())
number = int(input())
headers = []
for i in range(number):
    header = input()
    if len(header) > max_len:
        headers.append(header[:max_len - 3] + "...")
    else:
        headers.append(header)
print(headers)
