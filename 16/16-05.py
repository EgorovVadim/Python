friend_list = dict()


def add_friends(name_of_person, list_of_friends):
    friend_list[name_of_person] = list_of_friends


def are_friends(name_of_person1, name_of_person2):
    name_friends = friend_list.get(name_of_person1)
    if name_of_person2 in name_friends:
        return True
    else:
        return False


def print_friends(name_of_person):
    return friend_list.get(name_of_person)


add_friends("Алла", ["Марина", "Иван"])
print(are_friends("Алла", "Мария"))
add_friends("Алла", ["Мария"])
print(are_friends("Алла", "Мария"))


