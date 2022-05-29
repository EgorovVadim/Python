def swap(first, second):
    third = first[:]
    for i in range(len(first)):
        first.pop()
    first.extend(second)
    for i in range(len(second)):
        second.pop()
    second.extend(third)


first = [1, 2, 3]
second = [4, 5, 6]
first_content = first[:]
second_content = second[:]
swap(first, second)
print(first, second_content, first == second_content)
print(second, first_content, second == first_content)
