"""
此程序用于将24位颜色模式的图片转换为16位的图片(也就是RGB565模式),并将其读取出的像素数据写入头文件中。
主要用于开发TFT屏,在上面显示任意经过处理的图片

此项目创建于2024年6月7日02点36分
版本号1.1.2
我在原先的基础上添加了批量处理图片的功能

作者: Wei-RC
"""

'''
from PIL import Image

pic_path = 'C:/Users/86176/Desktop/xt.jpg'
file_path = "C:/Users/86176/Desktop/image.h"

def read_image(pic_path):
    img = Image.open(pic_path)
    old_w, old_h = img.size
    dim = (160, 128)   #目标尺寸
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

read_image(pic_path)
'''

#批量处理图片
import os
import glob
from PIL import Image

pic_folder = 'C:/Users/86176/Desktop/l'   #图片文件夹路径
output_path  = "C:/Users/86176/Desktop/image.h"

def batch_image(pic_folder):
    image_files = glob.glob(os.path.join(pic_folder + '/*.png'))   #获取图片文件夹路径下所有png图片
    
    img = Image.open(pic_folder)
    old_w, old_h = img.size
    dim = (160, 128)   #目标尺寸
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

    with open(output_path, "w") as f:
        f.write(text)

batch_image(pic_folder)