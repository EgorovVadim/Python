from docxtpl import DocxTemplate


doc = DocxTemplate("test01.docx")
context = {
    'place': "В нашем актовом зале ",
    'time': "В 12:30 ",
    'items': ["Кругляк Елена Степановна  ",
              'Иванова Марина Владимировна  ',
              "Лескова Анастасия Федоровна"]
}
doc.render(context)
doc.save("res.docx")
