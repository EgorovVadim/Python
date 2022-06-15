import xlsxwriter


def export_check(text):
    workbook = xlsxwriter.Workbook('res2.xlsx')
    worksheet = workbook.add_worksheet()
    text = text.split()
    s = 0
    for i in range(len(text)):
        name = text[i].split('\t')[0]
        price = text[i].split('\t')[1]
        n = text[i].split('\t')[2]
        worksheet.write(i, 0, name)
        worksheet.write(i, 1, float(price))
        worksheet.write(i, 2, int(n))
        worksheet.write(i, 3, '=B' + str(i + 1) + '*C' + str(i + 1))
        s += 1
    worksheet.write(s, 0, 'Итого')
    worksheet.write(s, 3, '=SUM(D1:D' + str(s) + ')')
    workbook.close()

