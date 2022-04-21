clients = list()
for i in range(int(input())):
    clients.append(int(input()))
for elem in clients:
    print(elem)
print()
for i in range(len(clients)):
    print(clients[i] * 3)
