names = set()
final_list = set()
temp_names = set()
result = set()
sheets = int(input())
for sheet in range(sheets):
    rows = int(input())
    for i in range(rows):
        name = input()
        if name in names:
            temp_names.add(name)
        else:
            names.add(name)
        if name in names and temp_names:
            result.add(name)
print(result)
