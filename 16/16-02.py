def discriminant(b, c):
    return b ** 2 - 4 * c


def smaller_root(p,q):
    x1 = (-p + discriminant(p, q) ** 0.5) / 2
    x2 = (-p - discriminant(p, q) ** 0.5) / 2
    if x1 > x2:
        return x2
    return x1


def larger_root(p,q):
    x1 = (-p + discriminant(p, q) ** 0.5) / 2
    x2 = (-p - discriminant(p, q) ** 0.5) / 2
    if x1 > x2:
        return x1
    return x2


def main(p, q):
    print(discriminant(p, q))
    print(smaller_root(p, q), larger_root(p, q))

