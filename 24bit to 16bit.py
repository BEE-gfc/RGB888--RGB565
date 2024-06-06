"""
This is a video that can convert an image with a 24-bit color mode to 16-bit, which is RGB565
And the data it converts to is stored in an array
I wrote this tool mainly for displaying some pictures on the TFT screen
I created this project at 23:01 on June 4, 2024.
当前版本1.0.0
"""

from PIL import Image

im = 'C:/Users/86176/Desktop/xt.jpg'
pic = 'xt.jpg'
file_path = "C:/Users/86176/Desktop/image.h"

def read_image(im):
    img = Image.open('C:/Users/86176/Desktop/xt.jpg')
    old_w, old_h = img.size
    dim = (160, 128)   #target size
    img.thumbnail(dim, Image.ANTIALIAS)

    text =''
    new_w = img.size[0]
    new_h = img.size[1]

    text += "#define IMAGE_WIDTH  %d\n" % new_w
    text += "#define IMAGE_HEIGHT %d\n" % new_h
    text += "uint16_t static const PROGMEM image[] = {\n"

    for y in range(0, new_h):
        for x in range(0, new_w):
            rgb565 = ((img.getpixel((x, y))[0] & 0xf8) << 8) + ((img.getpixel((x, y))[1] & 0xfc) << 3) + (img.getpixel((x, y))[2] >> 3)

            new_rgb565 = str(hex(rgb565))

            if (x == new_w -1 and y == new_h -1):
                text += "%s" % new_rgb565
            elif (x == new_w -1):
                text += "%s,\n" % new_rgb565
            else:
                text += "%s, " % new_rgb565

    text += "\n};"

    with open(file_path, "w") as f:
        f.write(text)

read_image(pic)

#以下是通过AI修饰的代码

'''
from PIL import Image

file_path = "C:/Users/86176/Desktop/image.h"
pic = 'C:/Users/86176/Desktop/xt.jpg'

def read_image(pic):
    img = Image.open(pic)
    old_w, old_h = img.size
    dim = (160, 128)   # 目标尺寸
    img.thumbnail(dim, Image.ANTIALIAS)

    text =''
    new_w, new_h = img.size

    text += "#define IMAGE_WIDTH  %d\n" % new_w
    text += "#define IMAGE_HEIGHT %d\n" % new_h
    text += "uint16_t static const PROGMEM image[] = {\n"

    for y in range(0, new_h):
        for x in range(0, new_w):
            rgb565 = ((img.getpixel((x, y))[0] & 0xf8) << 8) + ((img.getpixel((x, y))[1] & 0xfc) << 3) + (img.getpixel((x, y))[2] >> 3)
            new_rgb565 = str(hex(rgb565))

            if (x == new_w - 1 and y == new_h - 1):
                text += "%s" % new_rgb565
            elif (x == new_w - 1):
                text += "%s,\n" % new_rgb565
            else:
                text += "%s, " % new_rgb565

    text += "\n};"

    with open(file_path, "w") as f:
        f.write(text)

read_image(pic)
'''