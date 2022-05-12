def solve(*coefficients):
    a = b = c = x1 = x2 = 0
    if len(coefficients) == 0 or len(coefficients) > 3:
        return None
    if len(coefficients) == 3:
        a, b, c = coefficients
    if len(coefficients) == 2:
        b, c = coefficients
    if len(coefficients) == 1:
        c = coefficients
    D = b ** 2 - 4 * a * c
    if D > 0:
        x1 = (- b + D ** 0.5) / (2 * a)
        x2 = (- b - D ** 0.5) / (2 * a)
    elif D == 0:
        x1 = - b / (2 * a)
    else:
        return None
    return x1, x2


print(sorted(solve(1, -3, 2)))

