soldiers = list()
for i in range(int(input())):
    soldiers.append(input())
k = int(input())
for i in range(0 + k - 1, len(soldiers) - 1, k - 1):
    soldiers.remove(soldiers[i])
for soldier in soldiers:
    print(soldier)
