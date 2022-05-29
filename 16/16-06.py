alphabet = ["а", "у", "о", "ы", "и", "э", "я", "ю", "ё", "е"]
translated_text = ""


def translate(text):
    global translated_text
    for word in text.split():
        for char in word:
            if char not in alphabet and char.islower():
                translated_text += char
            elif char.isupper() and char.lower() not in alphabet:
                translated_text += char.upper()
        translated_text += " "


translate("Удивительный факт, но текст на языке НЕРАЗБОРЧИВО оказывается довольно просто читать. Достаточно небольшой тренировки - и вы сможете это делать.")
print(translated_text)