def print_document(pages):
    result = list()
    for page in pages:
        cur_page = page.split()
        if cur_page[0] == "Секретно":
            result.append("Дальнейшие материалы засекречены")
            return print(*result, sep="\n")
        result.append(page)
    result.append("Напечатано без купюр")
    return print(*result, sep="\n")


print_document(["Пустой трёп", "который", "никому не интересен"])