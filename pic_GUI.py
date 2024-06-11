'''
我将原来实现提取图像数据转为数组的代码改成了类,以方便维护调用,后期进行扩展其他新功能也更方便
'''

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
from PIL import Image

class PicGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("24bit -> 16bit 0.2.0-beta")
        self.root.geometry("360x200")

        self.label = tk.Label(self.root, text="图片路径：")
        self.label.place(x=0, y=170)

        self.entry = tk.Entry(self.root, width=25)
        self.entry.place(x=60, y=170)

        # 新增部分，用于输入缩放后的宽度
        self.label_width = tk.Label(self.root, text="宽：")
        self.label_width.place(x=0, y=115)

        self.entry_width = tk.Entry(self.root, width=5)
        self.entry_width.place(x=30, y=115)

        # 新增部分，用于输入缩放后的高度
        self.label_height = tk.Label(self.root, text="高：")
        self.label_height.place(x=0, y=140)

        self.entry_height = tk.Entry(self.root, width=5)
        self.entry_height.place(x=30, y=140)

        self.select_button = tk.Button(self.root, text="...", command=self.select_folder)
        self.select_button.place(x=250, y=165)

        self.convert_button = tk.Button(self.root, text="启动！", command=self.select_folder_convert)
        self.convert_button.place(x=270, y=165)

    def select_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.entry.delete(0, tk.END)  # 清空输入框
            self.entry.insert(0, folder_path)  # 在输入框中插入选择的文件夹路径

    def select_folder_convert(self):
        folder_path = self.entry.get()
        output_path = os.path.join(folder_path, "images.h")

        try:
            new_width = int(self.entry_width.get())  # 获取宽度输入框中的值
            new_height = int(self.entry_height.get())  # 获取高度输入框中的值
        except ValueError:
            messagebox.showerror("", "请输入有效宽高！")
            return

        if new_width <= 0 or new_height <= 0:
            messagebox.showerror("", "宽度和高度必须大于0")
            return

        if not folder_path:
            messagebox.showerror("", "请选择图片路径！")
            return
        self.batch_image(folder_path, output_path, new_width, new_height)

    def batch_image(self, pic_folder, output_path, new_width, new_height):
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
    
        pic_files = [os.path.join(pic_folder, file) for file in all_files if judg_format(file,supported_formats)]

        if not pic_files:
            messagebox.showerror("", "目标路径下没有支持处理的文件")
            return

        progress_bar = ttk.Progressbar(self.root, mode="determinate", length=150)    #创建进度条,由于得确认开始执行转换功能才建立进度条,因此放在判断文件是否存在的后面
        progress_bar.place(x=210, y=0)

        with open(output_path, "w") as f:
            progress_step = 100 / len(pic_files)    #计算每个文件处理的进度因此需要放在循环内
            for idx, picf in enumerate(pic_files):
                img = Image.open(picf)
                img.thumbnail((new_width, new_height), Image.ANTIALIAS)

                text =''
                new_w, new_h = img.size
                text += f"#IMAGE_WIDTH  {new_w}\n"
                text += f"#IMAGE_HEIGHT {new_h}\n"
                text += f"uint16_t static const PROGMEM l{idx+1}[] = {{\n"

                for y in range(new_h):
                    for x in range(new_w):
                        rgb565 = ((img.getpixel((x, y))[0] & 0xf8) << 8) + ((img.getpixel((x, y))[1] & 0xfc) << 3) + (img.getpixel((x, y))[2] >> 3)
                        text += f"{hex(rgb565)}, "
                    text += "\n"

                text += "};\n\n"
                f.write(text)

                progress_bar['value'] = (idx + 1) * progress_step   #更新进度条
                self.root.update_idletasks()   #更新界面
            
        messagebox.showinfo("完成", "图片转换成功！")
        progress_bar.destroy()   #销毁进度条
    pass

def run_gui():
    root = tk.Tk()
    #app = PicGUI(root)
    root.mainloop()

if __name__ == "__main__":
    run_gui()