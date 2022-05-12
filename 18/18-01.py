def matrix(n=1, m=None, a=0):
    result = list()
    if m is None:
        m = n
    for i in range(n):
        result.append([a] * n)
    return result


rows = matrix(2)
for row in rows:
    print(*row)

