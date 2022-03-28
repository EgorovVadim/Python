number = int(input())
war_Eurasia = True
war_Ostasia = False
for i in range(number):
    word = input()
    if word == "С кем война?":
        if war_Eurasia:
            print("Евразия")
        else:
            print("Остазия")
    elif word == "С кем мир?":
        if not war_Ostasia:
            print("Остазия")
        else:
            print("Евразия")
    elif word == "Меняем":
        war_Eurasia = not war_Eurasia
        war_Ostasia = not war_Ostasia
