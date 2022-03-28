number = int(input())
result = ""
cat_fined = False
for i in range(number):
    word = input()
    if ("Кот" in word or "кот" in word) and not cat_fined:
        result = "МЯУ"
        cat_fined = True
    elif not cat_fined:
        result = "НЕТ"
print(result)
