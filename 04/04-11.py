number = int(input())
average_iq = 0
for i in range(1, number + 1):
    iq = int(input())
    average_iq += iq
    if iq > average_iq // i:
        print(">")
    elif iq == average_iq // i:
        print("0")
    else:
        print("<")
