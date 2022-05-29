worker_dict = dict()


def setup_profile(name, vacation_dates):
    worker_dict[name] = {"vacation_date": vacation_dates}


def print_application_for_leave():
    for name, values in worker_dict.items():
        for date in values:
            print(f"Заявление на отпуск в период {name}. {worker_dict[name][date]}")


def print_holiday_money_claim(amount):
    for name, values in worker_dict.items():
        print(f"Прошу выплатить {amount} отпускных денег. {name}")


def print_attorney_letter(to_whom):
    for name, values in worker_dict.items():
        for date in values:
            print(f"На время отпуска в период {worker_dict[name][date]} моим заместителем назначается {to_whom}. {name}")



setup_profile("Иван Петров", "1 июня – 20 июня")
print_application_for_leave()
print_application_for_leave()
print_holiday_money_claim("15 тысяч пиастров")
print_attorney_letter("Василий Васильев")

