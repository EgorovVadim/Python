def take_large_banknotes(banknotes):
    result = list()
    for banknote in banknotes:
        if banknote > 10:
            result.append(banknote)
    return result


print(*take_large_banknotes([1, 5, 500, 0.5, 2, 0.1, 10, 100, 100, 1000, 50]))