'''
测试版之前的问题基本都修改完了,图片转数组的基本功能已经完全没问题,现在开始进行模块化,后续考虑将此脚本发展为一个功能丰富的软件
就先从gui界面开始模块化,本人近些天才开始接触了解Python这个语言,还不太熟练,作为实验工程,很多地方可能不够成熟和完美,还请各位大佬多多指教

作者: Wei-RC
时间: 2024-06-11-03-36
'''

import tkinter as tk
from pic_GUI import PicGUI

root = tk.Tk()
app = PicGUI(root)
root.mainloop()