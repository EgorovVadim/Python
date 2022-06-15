from PIL import Image


im1 = Image.open("fish.jpg")
im2 = Image.open("space.jpg")
width, height = im1.size
new_image = Image.new("RGB", (width, height))
pixels1 = im1.load()
pixels2 = im2.load()
pixels = new_image.load()
for x in range(width):
    for y in range(height):
        r1, g1, b1 = pixels1[x, y]
        r2, g2, b2 = pixels2[x, y]
        r = 0.5 * r1 + 0.5 * r2
        g = 0.5 * g1 + 0.5 * g2
        b = 0.5 * b1 + 0.5 * b2
        pixels[x, y] = int(r), int(g), int(b)
new_image.save("image02.bmp")
