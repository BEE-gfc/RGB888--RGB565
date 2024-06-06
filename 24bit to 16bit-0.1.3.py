"""
此程序用于将24位颜色模式的图片转换为16位的图片(也就是RGB565模式),并将其读取出的像素数据写入头文件中。
主要用于开发TFT屏,在上面显示任意经过处理的图片

此项目创建于2024年6月7日02点36分
版本号0.1.3
我在原先的基础上添加了批量处理图片的功能,并且修改了一些细节
后续将会添加更多功能,并且开发图形化交互界面以便于使用，欢迎大家提出宝贵意见

作者: Wei-RC
"""

import os
import glob
from PIL import Image

pic_folder = 'C:/Users/86176/Desktop/l'   #图片文件夹路径
output_path  = "C:/Users/86176/Desktop/image.h"

def batch_image(pic_folder, output_path):
    pic_files = glob.glob(os.path.join(pic_folder, '*.png'))   #获取图片文件夹路径下所有png图片
    
    with open(output_path, "w") as f:
        for idx, pic_files in enumerate(pic_files):
            img = Image.open(pic_files)
            img.thumbnail((160, 128), Image.ANTIALIAS)

            text =''
            new_w, new_h = img.size
            text += f"#define IMAGE_WIDTH  {new_w}\n"
            text += f"#define IMAGE_HEIGHT {new_h}\n"
            text += f"uint16_t static const PROGMEM l{idx+1}[] = {{\n"

            for y in range(new_h):
                for x in range(new_w):
                    rgb565 = ((img.getpixel((x, y))[0] & 0xf8) << 8) + ((img.getpixel((x, y))[1] & 0xfc) << 3) + (img.getpixel((x, y))[2] >> 3)
                    text += f"{hex(rgb565)}, "
                text += "\n"

            text += "};\n\n"
            f.write(text)

batch_image(pic_folder, output_path)