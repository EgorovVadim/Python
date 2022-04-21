firs_line = input()
incorrect = list()
total_count = 0
count = int(firs_line[:3])
amount = int(firs_line[4:])
for i in range(count):
    product = input()
    if int(product[:6]) * int(product[8:12]) != int(product[13:]):
        incorrect.append(i + 1)
    total_count += int(product[13:])
if total_count < amount:
    print(amount - total_count)
    for elem in incorrect:
        print(elem, end=" ")
else:
    print("0")

