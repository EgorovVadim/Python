numbers = input().split(" ")
print(" ".join([str(int(numbers[i]) ** 2) for i in range(len(numbers)) if str(int(numbers[i]) ** 2)[-1] != "9" and
                 i % 2 == 0]))
