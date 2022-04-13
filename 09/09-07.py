strings = list()
search_list = list()
result_list = list()
for i in range(int(input())):
    strings.append(input())
for i in range(int(input())):
    search_list.append(input())
for i in range(len(search_list)):
    for j in range(len(strings)):
        if search_list[i] in strings[j]:
            if strings[j] in result_list:
                print(strings[j])
            else:
                result_list.append(strings[j])

