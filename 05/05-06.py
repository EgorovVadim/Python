sum = count = 0
find_answer = False
while True:
    count += 1
    number = int(input())
    sum += number
    if number == 0:
        print(result)
        break
    if sum >= 10 and not find_answer:
        result = count
        find_answer = True
