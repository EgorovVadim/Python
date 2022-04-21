white_list = list()
searches = list()
for i in range(int(input())):
    white_list.append(input())
for i in range(int(input())):
    searches.append(input())
for i in range(len(searches)):
    for j in range(len(white_list)):
        if searches[i] == white_list[j]:
            print(searches[i])
