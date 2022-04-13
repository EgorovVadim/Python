alphabet = "ABCDEFGHI"
number = int(input())
temp_number = number
for i in range(number):
    for j in range(number):
        print(alphabet[j] + str(temp_number), end="\t")
        j += 1
    print()
    temp_number -= 1
