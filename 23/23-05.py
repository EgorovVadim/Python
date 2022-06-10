from PIL import Image, ImageDraw


def board(num, size):
    width = num * size
    height = width
    im = Image.new("RGB", (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    for vertical in range(0, num, 2):
        for horizontal in range(num):
            if horizontal % 2 == 0:
                draw.rectangle(((vertical * size, horizontal * size),
                                (vertical * size + size, horizontal * size + size)), (0, 0, 0))
            else:
                draw.rectangle(((vertical * size + size, horizontal * size),
                                (vertical * size + size * 2, horizontal * size + size)), (0, 0, 0))
    im.save("doska.bmp")


board(8, 50)
