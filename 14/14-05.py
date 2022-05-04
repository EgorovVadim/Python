def triangle(a, b, c):
    if a + b > c or a + c > b or c + b > a:
        print("Это треугольник")
    else:
        print("Это не треугольник")
