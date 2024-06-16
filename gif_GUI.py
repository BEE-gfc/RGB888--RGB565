'''
这是新增的一个小模块,可以将 GIF 图像的每一帧提取出来,并保存为指定格式,暂时支持·jpg·和·png·格式,这个模块的功能暂未完善
2024年6月12日12点29分
'''


#这是原始版本，功能不完整，主要是后期修改出问题了能够回来做参考
""" import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
from PIL import Image


class Gif_P:
    def __init__(self, root):
        self.root = root
        self.label = tk.Label(self.root, text="提取GIF")
        self.label.pack()

        self.label = tk.Label(self.root, text="GIF路径:")
        self.label.place(x=0, y=280)

        self.entry = tk.Entry(self.root, width=25)
        self.entry.place(x=60, y=280)

        self.extract_button = tk.Button(self.root, text="分解！", command=self.extract_gif_frames_handler)
        self.extract_button.place(x=250, y=275)

        self.var = tk.StringVar()
        
        self.jpg_radio = tk.Radiobutton(self.root, variable=self.var, value=".jpg", text=".jpg")
        self.jpg_radio.place(x=180, y=305)
        
        self.var.set(".png")  # 默认选.png
        self.png_radio = tk.Radiobutton(self.root, variable=self.var, value=".png", text=".png")
        self.png_radio.place(x=100, y=305)

    def extract_gif_frames_handler(self):
        output_format = self.var.get()
        gif_folder = self.entry.get()

        if not gif_folder:
            messagebox.showwarning("", "请选择有效文件！")
            return

        # 读取用户输入的GIF文件
        try:
            gif_image = Image.open(gif_folder)
            gif_name = os.path.splitext(os.path.basename(gif_folder))[0]  # 获取GIF图像的文件名
            output_folder = os.path.join(os.path.dirname(gif_folder), f"{gif_name}_frames")  # 创建以GIF文件名命名的文件夹路径

            # 如果文件夹不存在则创建
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)

            # 逐帧保存为指定格式
            for i in range(gif_image.n_frames):
                gif_image.seek(i)
                frame = gif_image.copy()
                frame.save(os.path.join(output_folder, f"{i}{output_format}"))

            messagebox.showinfo("完成", f"GIF提取成功,保存在{output_folder}文件夹中！")
        except Exception as e:
            messagebox.showerror("错误", f"提取转换GIF帧时发生错误:{e}") """



import tkinter as tk
from tkinter import filedialog, messagebox
import os
from PIL import Image, ImageTk, ImageSequence
import windnd

class Gif_P:
    def __init__(self, root):
        self.root = root
        self.frame_index = 0
        self.gif_path = ""
        self.frames = []
        self.update_id = None

        self.label = tk.Label(self.root, text="逐帧提取GIF")
        self.label.pack()

        canvas = tk.Canvas(self.root, width=400, height=400)
        canvas.pack()
        canvas.create_rectangle(99, 39, 304, 244, outline='black')
        center_x = (403) / 2
        center_y = (284) / 2
        canvas.create_text(center_x, center_y, text="我要GIF", fill="black") 

        windnd.hook_dropfiles(self.root, func=self.handle_dropped_files)

        self.label = tk.Label(self.root)
        self.label.pack()

        self.button_choose = tk.Button(self.root, text="来张GIF", command=self.choose_gif)
        self.button_choose.place(x=170, y=270)

        # self.label_gif_path = tk.Label(self.root, text="提取路径:")
        # self.label_gif_path.place(x=20, y=310)

        # self.entry_gif_path = tk.Entry(self.root, width=30)
        # self.entry_gif_path.place(x=80, y=310)

        self.extract_button = tk.Button(self.root, text="分解！", command=self.extract_gif_frames_handler)
        self.extract_button.place(x=280, y=305)

        self.var = tk.StringVar()
        
        self.jpg_radio = tk.Radiobutton(self.root, variable=self.var, value=".jpg", text=".jpg")
        self.jpg_radio.place(x=210, y=310)
        
        self.var.set(".png")  # 默认选.png
        self.png_radio = tk.Radiobutton(self.root, variable=self.var, value=".png", text=".png")
        self.png_radio.place(x=130, y=310)

    def resize_gif(self, input_path, target_size):
        with Image.open(input_path) as img:
            frames = [frame.copy() for frame in ImageSequence.Iterator(img)]
            resized_frames = []
            for frame in frames:
                frame.thumbnail(target_size, Image.ANTIALIAS)
                resized_frames.append(ImageTk.PhotoImage(frame))
            return resized_frames

    def handle_dropped_files(self, files):
        new_gif_path = files[0].decode('utf-8')
        self.load_and_play_gif(new_gif_path)

    def choose_gif(self):
        new_gif_path = filedialog.askopenfilename(filetypes=[("GIF", "*.gif")])
        if new_gif_path:
            self.load_and_play_gif(new_gif_path)

    def load_and_play_gif(self, new_gif_path):
        if new_gif_path.endswith(".gif"):
            if self.gif_path != new_gif_path:
                self.gif_path = new_gif_path
                resized_frames = self.resize_gif(self.gif_path, (200, 200))
                self.frames = resized_frames
                self.frame_index = 0
                if self.update_id:
                    self.label.after_cancel(self.update_id)
                self.update_id = self.label.after(50, self.update_gif)
        else:
            messagebox.showerror("嘿~", "我只吃GIF文件哦")

    def update_gif(self):
        if self.frames:
            self.label.config(image=self.frames[self.frame_index])
            self.label.place(x=100, y=63)
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            self.update_id = self.label.after(50, self.update_gif)

    def extract_gif_frames_handler(self):
        output_format = self.var.get()
        gif_folder = self.gif_path

        if not gif_folder:
            messagebox.showwarning("", "请选择有效文件！")
            return

        try:
            gif_image = Image.open(gif_folder)
            gif_name = os.path.splitext(os.path.basename(gif_folder))[0]
            output_folder = os.path.join(os.path.dirname(gif_folder), f"{gif_name}_frames")  # 直接以选择的 GIF 文件同名的文件夹路径

            if not os.path.exists(output_folder):
                os.makedirs(output_folder)

            for i in range(gif_image.n_frames):
                gif_image.seek(i)
                frame = gif_image.copy()
                frame.save(os.path.join(output_folder, f"{i}{output_format}"))

            messagebox.showinfo("完成", f"GIF提取成功,保存在 {output_folder} 文件夹中！")
        except Exception as e:
            messagebox.showerror("错误", f"提取GIF时发生错误：{e}")