number = int(input())
count = 0
names = set()
temp_names = set()
for i in range(number):
    name = input()
    if name in names:
        count += 1
        temp_names.add(name)
    names.add(name)
print(count + len(temp_names))
