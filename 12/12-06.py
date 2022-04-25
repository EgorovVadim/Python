line = input().split()
result = ""
for word in line:
    result += "-".join(list(word)) + " "
print(result.upper())
