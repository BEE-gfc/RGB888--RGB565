'''
软件说明
'''

import tkinter as tk
import pyautogui

class readme:
    def show_add_info(self):
        add_info_window = tk.Toplevel(self.root)
        add_info_window.geometry("500x320")
        add_info_text = tk.Text(add_info_window, wrap='word', state='normal', font=('Arial', 11))
        add_info_text.pack(expand=True, fill='both')

        add_info_content = """
2024-06-11
V.0.1.0
        
2025/3/29
V.0.4.0
新增flac音频文件封装封面功能
"""
        add_info_text.insert("1.0", add_info_content)
        add_info_text.config(state='disabled')

    def __init__(self, root):
        self.root = root

        self.readme_text = tk.Text(self.root, wrap='word', state='normal', height=15, width=60, font=('Comic Sans MS', 10))
        self.readme_text.pack(expand=True, fill='both')  # 使用expand和fill来填充整个父容器

        readme_content = """
        软件全名: 
                     集成处理实验室
        Integrated Processing Laboratory
        
        版本: V0.3.0
        作者: Wei-RC
        简单说明:

        本软件是用纯Python编写的图像处理软件
        本想用C++来编写,但是最近在学习Python
        于是就当作练手项目来做了

        这个版本我新增了逐帧提取GIF的功能
        暂时无法将GIF直接提取为jpg格式
        主要是需要做一些转换程序
        而这样做会使原图失真
        或者出现一些奇奇怪怪的问题
        出来的图片可能很奇怪,得不偿失
        如非必要我暂时不会添加此功能
        敬请期待后续研究成果吧!
        所以这个jpg的按钮就当是个摆设吧
        优化了一些界面上的细节
        如果有其他需求或者问题,欢迎联系我:

        WeChat: 半兮'烟雨^
        微信号: RXnw_CNTT0603
        QQ: 3460433495
        B站: @cnttbvc
        """
        self.readme_text.insert("1.0", readme_content)
        self.readme_text.config(state='disabled')
        
        # 创建按钮
        add_info_button = tk.Button(self.root, text="开发日志", command=self.show_add_info)
        add_info_button.pack(side="bottom", anchor="se")  # 将按钮显示在右下角，并且稍微突出显示

class MousePosition:
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.create_widgets()
        self.update_mouse_position()

    def create_widgets(self):
        self.position_label = tk.Label(self.parent_frame, text="鼠标坐标: (0, 0)", font=("Arial", 12))
        self.position_label.pack(pady=20)

    def update_mouse_position(self):
        x, y = pyautogui.position()
        self.position_label.config(text=f"x:{x}, y:{y}")
        self.parent_frame.after(50, self.update_mouse_position)  # 每50毫秒更新一次

'''
import pyautogui

try:
    while True:
        # 获取鼠标在屏幕上的坐标
        x, y = pyautogui.position()
        print(f"鼠标坐标: ({x}, {y})", end='\r')
except KeyboardInterrupt:
    print("\n程序已结束")
'''