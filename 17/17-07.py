def transpose(matrix):
    result = list()
    n = len(matrix)
    if len(matrix) == 1:
        m = n
    else:
        m = len(matrix[0])
    for j in range(m):
        temp_result = list()
        for i in range(n):
            temp_result += [matrix[i][j]]
        result += temp_result
    return result


matrix = [[1, 2], [3, 4]]
transpose(matrix)
for line in matrix:
    print(*line)
