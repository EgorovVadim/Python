string = input()
count = temp_count = 0
in_a_row = True
for i in range(len(string)):
    if string[i] == "о":
        count += 1
    else:
        temp_count = count
        count = 0
print(temp_count)
