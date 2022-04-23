recipe = list()
for i in range(int(input())):
    recipe.append(input())
print(", ".join([recipe[i] for i in range(len(recipe)) if "лук" not in recipe[i].lower()]))