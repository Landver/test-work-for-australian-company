import os
from PIL import Image, ImageFont, ImageDraw


SOURCE_IMAGES_DIR = './source-images'
OUTPUT_IMAGES_DIR = './output-images'

for filename in os.listdir(SOURCE_IMAGES_DIR):
    try:  # need try if file not an image
        img = Image.open(f'{SOURCE_IMAGES_DIR}/{filename}')
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("Roboto-Medium.ttf", 40)
        signature = f'©{filename}' \
                        .replace('-', ' ') \
                        .split('.')[0] \
                        .title()  # for example string "casey-horner.jpg" become "©Casey Horner"
        W, H = img.size  # image Width and Height
        w, h = draw.textsize(signature, font=font)  # text Width and Height
        x_axis, y_axis = ((W-w)/1.05, (H-h)/1.05)  # x, y axis for text position
        rgb_values = (255, 255, 255)  # color of the text for the picture

        draw.text((x_axis, y_axis), signature, rgb_values, font=font)
        img.save(f'{OUTPUT_IMAGES_DIR}/{filename}')
    except IOError:
        print(f'{filename} not an image file')
