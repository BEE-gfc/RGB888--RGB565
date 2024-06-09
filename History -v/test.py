'''
最后一次能正常运行的代码,留档出问题时参考
'''

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

import os
from PIL import Image

def batch_image(pic_folder, output_path):
    if not pic_folder or not os.path.exists(pic_folder):
        messagebox.showerror("错误", "请选择有效的文件夹！")
        return
    
    supported_formats = ['.jpg', '.jpeg', '.png', '.bmp', '.ico']
    all_files = os.listdir(pic_folder)
    def judg_format(file):
        for fmt in supported_formats:
            if file.lower().endswith(fmt):
                return True
        return False
    
    #pic_files = [file for file in os.listdir(pic_folder) if file.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.ico'))]
    #pic_files = glob.glob(os.path.join(pic_folder, '*.jpg'))   #不知道为什么这样就没问题了
    pic_files = [os.path.join(pic_folder, file) for file in all_files if judg_format(file)]

    if not pic_files:
        messagebox.showerror("错误", "目标路径下没有支持处理的文件")
        return

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
    folder_path = filedialog.askdirectory()
    if folder_path:
        entry.delete(0, tk.END)  # 清空输入框
        entry.insert(0, folder_path)  # 在输入框中插入选择的文件夹路径

def select_folder_connvert():
    folder_path = entry.get()
    output_path = os.path.join(folder_path, "images.h")
    batch_image(folder_path, output_path)

root = tk.Tk()
root.title("24bit -> 16bit")
root.geometry("360x200")

label = tk.Label(root, text="输入文件夹路径：")
label.grid(row=1, column=0, pady=90, padx=0)

entry = tk.Entry(root, width=25)
entry.grid(row=1, column=1)

select_button = tk.Button(root, text="...", command=select_folder)
select_button.grid(row=1, column=2)

convert_button = tk.Button(root, text="启动！", command=select_folder_connvert)
convert_button.grid(row=1, column=3, pady=20, padx=10)

root.mainloop()