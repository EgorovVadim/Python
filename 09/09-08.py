menu = ["щи", "борщ", "щавелевый суп", "овсяный суп", "суп по-чабански"]
for i in range(int(input())):
    if i > 4:
        i %= 5
    print(menu[i])

