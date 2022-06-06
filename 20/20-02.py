total_list = list()
temp_list = list()
for i in range(int(input())):
    number = int(input())
    temp_list = list()
    for j in range(number):
        line = input()
        temp_list.append(line)
    total_list.append(temp_list)
if any("5" in student for line in total_list for student in line):
    print("Да")
else:
    print("Нет")