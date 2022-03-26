string = input("Введите сообщение: ")
cost_rub = len(string) * 40 // 100
cost_cop = len(string) * 40 % 100
print(str(cost_rub) + " р. " + str(cost_cop) + " коп.")
