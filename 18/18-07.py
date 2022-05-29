a, b, c = input().split()
D = int(b) ** 2 - 4 * int(a) * int(c)
if D > 0:
    print((-int(b) - D ** 0.5) / (2 * int(a)), (-int(b) + D ** 0.5) / (2 * int(a)))
elif D == 0:
    print(-int(b) / (2 * int(a)))

