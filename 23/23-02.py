from PIL import Image


im = Image.open("Рианна.jpeg")
pixels = im.load()  # список с пикселями
width, height = im.size  # ширина (x) и высота (y) изображения
list_r = list()
list_g = list()
list_b = list()
for i in range(width):
    for j in range(height):
        pass
        r, g, b = pixels[i, j]
        list_r.append(r)
        list_g.append(g)
        list_b.append(b)
result_r = sum(list_r) // len(list_r)
result_g = sum(list_g) // len(list_g)
result_b = sum(list_b) // len(list_b)
im = Image.new("RGB", (width, height), (result_r, result_g, result_b))
print(result_r, result_g, result_b)
im.save("Рианна2.jpg")

