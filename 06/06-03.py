eng_set = set()
ger_set = set()
result_set = set()
number1 = int(input())
number2 = int(input())
for i in range(number1):
    eng_set.add(input())
for i in range(number2):
    ger_set.add(input())
result_set = eng_set ^ ger_set
if len(result_set):
    print(len(result_set))
else:
    print("NO")
