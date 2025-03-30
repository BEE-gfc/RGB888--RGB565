'''
测试版之前的问题基本都修改完了,图片转数组的基本功能已经完全没问题,现在开始进行模块化,后续考虑将此脚本发展为一个功能丰富的软件
就先从gui界面开始模块化,本人近些天才开始接触了解Python这个语言,还不太熟练,作为实验工程,很多地方可能不够成熟和完美,还请各位大佬多多指教

作者: Wei-RC
时间: 2024-06-11-03-36
'''

import os
import sys
import tkinter as tk
from tkinter import ttk
from pic_GUI import PicGUI
from gif_GUI import Gif_P
from flac_add import Add_Flac_Cover
from Readme import readme,MousePosition

def show_imgarray():
    tab_control.select(0)  # 选中图像数组选项卡

def show_gif_extraction():
    tab_control.select(1)  # 选中GIF提取选项卡

def show_Add_Flac_Cover():
    tab_control.select(2)  # 选中添加封面选项卡

def show_Readme():
    tab_control.select(3)

root = tk.Tk()
# root.iconbitmap(r'C:\Users\86176\Desktop\Project Library\VSC-E\Wei-RC-Lab\Python-lab\image\t.ico')
root.title("集成处理实验室")
root.geometry("400x400")
root.minsize(400, 400)
root.resizable(False, False)

# 选项卡控件
tab_control = ttk.Notebook(root)

imgarray_tab = ttk.Frame(tab_control)
Add_Flac_Cover_frame = ttk.Frame(tab_control)
gif_tab = ttk.Frame(tab_control)
mouse_position_frame = ttk.Frame(tab_control)
Readme_frame = ttk.Frame(tab_control)

tab_control.add(imgarray_tab, text="RGB888图像数组")
tab_control.add(gif_tab, text="GIF")
tab_control.add(Add_Flac_Cover_frame, text="FLAC封面")  # 新增选项卡
tab_control.add(mouse_position_frame, text="坐标")
tab_control.add(Readme_frame, text="帮助文档")
tab_control.pack(expand=1, fill="both")
#实例化类
PicGUI(imgarray_tab)
Gif_P(gif_tab)
Add_Flac_Cover(Add_Flac_Cover_frame)
MousePosition(mouse_position_frame)
readme(Readme_frame)

root.mainloop()