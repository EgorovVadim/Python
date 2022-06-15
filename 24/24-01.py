from PIL import Image


def twist_image(input_file_name, output_file_name):
    im = Image.open(input_file_name)
    width, height = im.size
    im1 = im.crop((0, 0, width // 2, height))
    im2 = im.crop((width // 2, 0, width, height))
    new_image = Image.new("RGB", (width, height))
    new_image.paste(im2, (0, 0))
    new_image.paste(im1, (width // 2, 0))
    new_image.save(output_file_name)


twist_image("statement-image.jpg", "image01.bmp")
