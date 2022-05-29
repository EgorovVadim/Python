daily_food = [0, 150, 150]


def count_food(days):
    result = 0
    if len(days) > 1:
        for i in range(days[0], days[1] + 1):
            result += daily_food[i - 1]
    elif len(days) == 1:
        result = daily_food[0]
    return result


print(count_food([1]))