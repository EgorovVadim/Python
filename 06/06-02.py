number = int(input())
city_set = set()
for i in range(number):
    city_set.add(input())
if input() not in city_set:
    print("OK")
else:
    print("TRY ANOTHER")
