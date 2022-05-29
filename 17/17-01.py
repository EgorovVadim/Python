phareses = list()


def parrot(phrase):
    if phrase in phareses:
        print(phrase)
    else:
        phareses.append(phrase)


parrot("Привет")
parrot("Как тебя зовут?")
parrot("Привет")

