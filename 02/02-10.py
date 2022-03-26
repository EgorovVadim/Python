first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))
math_operation = input("Введите действие: ")
if math_operation == "+":
    print(first_number + second_number)
elif math_operation == "-":
    print(first_number - second_number)
elif math_operation == "*":
    print(first_number * second_number)
elif math_operation == "/":
    if second_number != 0:
        print(first_number / second_number)
    else:
        print("888888")
else:
    print("888888")
    