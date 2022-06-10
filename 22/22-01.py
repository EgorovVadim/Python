import random
from pprint import pprint


def make_bingo():
    result = list()
    v = list(range(1, 76))
    random.shuffle(v)
    for i in range(5):
        row = v[i * 5:i * 5 + 5]
        if i == 2:
            row[2] = 0
        result.append(tuple(row))
    return tuple(result)


res = make_bingo()
pprint(res)