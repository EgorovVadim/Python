def print_statistics(arr):
    arr.sort()
    if len(arr) == 0:
        return print(0, 0, 0, 0, 0, sep="\n")
    avr = sum(arr) / len(arr)
    med = (arr[int(len(arr) / 2 - 1)] + arr[int(len(arr) / 2)]) / 2
    return print(len(arr), avr, min(arr), max(arr), med, sep="\n")


