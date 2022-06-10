from PIL import Image, ImageDraw


def picture(file_name, width, height, sky_color="#87CEEB", ocean_color="#017B92", boat_color="#874535", sail_color="#FFFFFF", sun_color="#FFCF40"):
    im = Image.new("RGB", (width, height), sky_color)
    draw = ImageDraw.Draw(im)
    draw.rectangle(((0, height * 0.8), (width, height)), ocean_color)
    draw.ellipse(((int(0.8 * width), -int(0.2 * height)), (int(1.2 * width), int(0.2 * height))), sun_color)
    draw.rectangle(((width * 0.49, height * 0.30), (width * 0.51, height * 0.65)), boat_color)
    draw.polygon((((width * 0.25), (height * 0.65)),
                 ((width * 0.75), (height * 0.65)),
                 ((width * 0.70), (height * 0.85)),
                 ((width * 0.30), (height * 0.85))), boat_color)
    draw.polygon((((width * 0.51), (height * 0.3)),
                   ((width * 0.66), (height * 0.45)),
                   ((width * 0.51), (height * 0.6))), sail_color)
    im.save(file_name)



picture("test.bmp", 1000, 800)