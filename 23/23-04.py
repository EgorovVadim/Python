from PIL import Image, ImageDraw


def gradient(color):
    width = 512
    height = 200
    if color == "R":
        new_color = (255, 0, 0)
    elif color == "B":
        new_color= (0, 255, 0)
    elif color == "G":
        new_color = (0, 0, 255)
    new_image = Image.new("RGB", (width, height), (0, 0, 0))
    draw = ImageDraw.Draw(new_image)
    for cur_pos in range(0, width):
            draw.line((cur_pos, 0, cur_pos, height), fill=(cur_pos, 0, 0), width=1)
    new_image.save("kartinka.bmp")


gradient("R")