'''
2024年6月8日14点41分
原先的命令行版本已经完成, 现在开始测试GUI版本,测试版本号0.1.4
此版本为测试版,因此仅有简单的功能,可能存在一些问题,后续将会进行优化和完善
其实命令行版本已经很好用了[手动狗头]
'''

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

import os
import glob
from PIL import Image

def batch_image(pic_folder, output_path):
    pic_files = glob.glob(os.path.join(pic_folder, '*.jpg'))   #获取图片文件夹路径下所有png图片
    
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
            
    messagebox.showinfo("完成", "图片转换成功！")

def select_folder():
    pic_folder = filedialog.askdirectory()
    output_path = os.path.join(pic_folder, "images.h")
    batch_image(pic_folder, output_path)

root = tk.Tk()
root.title("Image Converter")

select_button = tk.Button(root, text="选择文件夹", command=select_folder)
select_button.pack()

root.mainloop()