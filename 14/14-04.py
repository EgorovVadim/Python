def who_are_you_and_hello():
    chars = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", "?"]
    correct = False
    while True:
        name = input()
        if len(name.split()) == 1 and name[0].isupper() and name[1:-1].islower():
            for char in name:
                if char not in chars:
                    correct = True
                else:
                    correct = False
        if correct:
            print("Привет,", name + "!")

