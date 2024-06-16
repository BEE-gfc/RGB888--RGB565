'''
测试版之前的问题基本都修改完了,图片转数组的基本功能已经完全没问题,现在开始进行模块化,后续考虑将此脚本发展为一个功能丰富的软件
就先从gui界面开始模块化,本人近些天才开始接触了解Python这个语言,还不太熟练,作为实验工程,很多地方可能不够成熟和完美,还请各位大佬多多指教

作者: Wei-RC
时间: 2024-06-11-03-36
'''

import tkinter as tk
from tkinter import ttk
from pic_GUI import PicGUI
from gif_GUI import Gif_P
from Readme import readme

def show_imgarray():
    tab_control.select(0)  # 选中图像数组选项卡

def show_gif_extraction():
    tab_control.select(1)  # 选中GIF提取选项卡

def show_Readme():
    tab_control.select(2)

root = tk.Tk()
root.iconbitmap(r'C:\Users\86176\Desktop\Project Library\VSC-E\Wei-RC-Lab\Python-lab\image\t.ico')
root.title("集成处理实验室")
root.geometry("400x400")
root.minsize(400, 400)
root.resizable(False, False)

# 选项卡控件
tab_control = ttk.Notebook(root)

imgarray_frame = ttk.Frame(tab_control)
gif_extraction_frame = ttk.Frame(tab_control)
Readme_frame = ttk.Frame(tab_control)

tab_control.add(imgarray_frame, text="▼")
tab_control.add(gif_extraction_frame, text="▲")
tab_control.add(Readme_frame, text="README")
tab_control.pack(expand=1, fill="both")
#实例化类
PicGUI(imgarray_frame)
Gif_P(gif_extraction_frame)
readme(Readme_frame)

root.mainloop()