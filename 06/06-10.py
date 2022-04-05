M = int(input())
dishes = set()
day_dishes = set()
for i in range(M):
    dish = input()
    dishes.add(dish)
result = dishes
N = int(input())
for i in range(N):
    number_dishes = int(input())
    for j in range(number_dishes):
        day_dish = input()
        day_dishes.add(day_dish)
    dishes -= day_dishes
print(dishes)
