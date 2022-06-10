from PIL import Image


r, g, b = input().split()
im = Image.new("RGB", (500, 500), (255 - int(r), 255 - int(g), 255 - int(b)))
im.save("01.jpg")
