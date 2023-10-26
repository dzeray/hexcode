from PIL import Image
from resizeimage import resizeimage
import webcolors
from colorthief import ColorThief
import _json


image_path = 'img.jpeg'
new_max_width = 1800
image_colors = []

with open(image_path, 'r+b') as f:
    with Image.open(f) as image:
        smaller_image = resizeimage.resize_width(image, 345)
        smaller_image.save('new_image.jpeg', image.format)

    color_thief = ColorThief('new_image.jpeg')
    color_palette = color_thief.get_palette(color_count=10, quality=10)
    for color in color_palette:
        print(webcolors.rgb_to_hex(color))
