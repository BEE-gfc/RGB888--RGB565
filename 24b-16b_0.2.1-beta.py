'''
图形交互界面建立完了,存在一些问题,目前这个版本功能基本完善,已经能稳定运行,就先不改了
增加了个小功能,可以自定义想要缩放的尺寸,并且添加了进度条

作者: Wei-RC
'''

import tkinter as tk
from tkinter import filedialog, messagebox, ttk

import os
from PIL import Image

def batch_image(pic_folder, output_path, new_width, new_height):
    if not pic_folder or not os.path.exists(pic_folder):
        messagebox.showwarning("", "请选择有效文件夹！")
        return
    
    supported_formats = {'.jpg', '.jpeg', '.png', '.bmp', '.ico'}
    all_files = os.listdir(pic_folder)
    def judg_format(file,supported_formats):
        for fmt in supported_formats:
            if file.lower().endswith(fmt):
                return True
        return False
    
    #pic_files = glob.glob(os.path.join(pic_folder, '*.jpg'))   #不知道为什么这样就没问题了
    pic_files = [os.path.join(pic_folder, file) for file in all_files if judg_format(file,supported_formats)]

    if not pic_files:
        messagebox.showerror("", "目标路径下没有支持处理的文件")
        return

    progress_bar = ttk.Progressbar(root, mode="determinate", length=150)    #创建进度条,由于得确认开始执行转换功能才建立进度条,因此放在判断文件是否存在的后面
    progress_bar.place(x=210, y=0)

    with open(output_path, "w") as f:
        progress_step = 100 / len(pic_files)    #计算每个文件处理的进度因此需要放在循环内
        for idx, picf in enumerate(pic_files):
            img = Image.open(picf)
            img.thumbnail((new_width, new_height), Image.ANTIALIAS)

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

            progress_bar['value'] = (idx + 1) * progress_step   #更新进度条
            root.update_idletasks()   #更新界面
            
    messagebox.showinfo("完成", "图片转换成功！")

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        entry.delete(0, tk.END)  # 清空输入框
        entry.insert(0, folder_path)  # 在输入框中插入选择的文件夹路径

def select_folder_connvert():
    folder_path = entry.get()
    output_path = os.path.join(folder_path, "images.h")

    try:
        new_width = int(entry_width.get())  # 获取宽度输入框中的值
        new_height = int(entry_height.get())  # 获取高度输入框中的值
    except ValueError:
        messagebox.showerror("", "请输入有效宽高！")
        return

    if new_width <= 0 or new_height <= 0:
        messagebox.showerror("", "宽度和高度必须大于0")
        return

    if not folder_path:
        messagebox.showerror("", "请选择图片路径！")
        return
    batch_image(folder_path, output_path, new_width, new_height)


root = tk.Tk()
root.title("24bit -> 16bit 0.2.0-beta")
root.geometry("360x200")

label = tk.Label(root, text="图片路径：")
label.place(x=0, y=170)

entry = tk.Entry(root, width=25)
entry.place(x=60, y=170)

# 新增部分，用于输入缩放后的宽度
label_width = tk.Label(root, text="宽：")
label_width.place(x=0, y=115)

entry_width = tk.Entry(root, width=5)
entry_width.place(x=30, y=115)

# 新增部分，用于输入缩放后的高度
label_height = tk.Label(root, text="高：")
label_height.place(x=0, y=140)

entry_height = tk.Entry(root, width=5)
entry_height.place(x=30, y=140)

select_button = tk.Button(root, text="...", command=select_folder)
select_button.place(x=250, y=165)

convert_button = tk.Button(root, text="启动！", command=select_folder_connvert)
convert_button.place(x=270, y=165)

root.mainloop()