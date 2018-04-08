#!/usr/bin/python
# -*- coding: UTF-8 -*-
from tkinter import *
tk = Tk()
# 一级菜单对象
m = Menu(tk)
# 一级子菜单
fm = Menu(m,tearoff=False)
# 子菜单列
fm.add_command(label="打开")
fm.add_command(label="导入")
# 下拉菜单分隔
fm.add_separator()
fm.add_command(label="退出")
# 为一级创建多级菜单
m.add_cascade(label="文件",menu=fm)
tk.config(menu=m)

tk.mainloop()