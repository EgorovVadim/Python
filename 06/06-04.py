result_set = set()
number1 = int(input())
number2 = int(input())
for i in range(number1 + number2):
    word = input()
    if word in result_set:
        result_set.discard(word)
    else:
        result_set.add(word)
if len(result_set):
    print(len(result_set))
else:
    print("NO")
