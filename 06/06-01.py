number_set1 = set()
number_set2 = set()
while True:
    number = input()
    if number == "":
        break
    else:
        number_set1.add(int(number))
while True:
    number = input()
    if number == "":
        break
    else:
        number_set2.add(int(number))
if number_set1 & number_set2:
    print(number_set1 & number_set2)
else:
    print("EMPTY")
