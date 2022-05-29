check_number = 1
total_cost = 0
check_list = list()


def add_item(item_name, item_cost):
    check_list.append({item_name: item_cost})


def print_receipt():
    global check_number, total_cost, check_list
    if len(check_list) == 0:
        return
    print("Чек", str(check_number) + ". Всего предметов:", len(check_list))
    for item in check_list:
        for item_name, item_cost in item.items():
            print(item_name, " - ", item_cost)
            total_cost += item_cost
    print("Итого:", total_cost)
    print("-" * 5)
    check_number += 1
    total_cost = 0
    check_list = list()


add_item('Блокнот', 100)
print_receipt()

add_item('Ручка', 70)
print_receipt()
print_receipt()

add_item('Булочка', 15)
add_item('Булочка', 15)
add_item('Чай', 5)
print_receipt()

add_item('Булочка', 15)
add_item('Булочка', 15)




