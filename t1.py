#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'huangbinghe@gmail.com'

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu    # 导入菜单类

win = tk.Tk()
win.title('python gui test')
# win.geometry('500x300+100+50') #窗口大小位置widthxheight+x+y
win.resizable(0, 0)        # 禁止调整窗口大小
win.iconbitmap('zy.ico')

# 创建一个容器,
monty = ttk.LabelFrame(win, text=" Monty Python ")     # 创建一个容器，其父容器为win
# padx  pady   该容器外围需要留出的空余空间
monty.grid(column=0, row=0, padx=10, pady=10)
aLabel = ttk.Label(monty, text="A Label")

ttk.Label(monty, text="chooes a number").grid(column=1, padx=5, row=0)
ttk.Label(monty, text="enter a name:").grid(column=0, padx=5, row=0)


def _quit():
    """结束主事件循环"""
    win.quit()      # 关闭窗口
    win.destroy()   # 将所有的窗口小部件进行销毁，应该有内存回收的意思
    exit()


# 创建菜单栏功能
menuBar = Menu(win)
win.config(menu=menuBar)


# 创建一个名为File的菜单项
fileMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="File", menu=fileMenu)

# 在菜单项File下面添加一个名为New的选项
fileMenu.add_command(label="New")

# 在两个菜单选项中间添加一条横线
fileMenu.add_separator()

# 在菜单项下面添加一个名为Exit的选项
fileMenu.add_command(label="Exit", command=_quit)

# 在菜单栏中创建一个名为Help的菜单项
helpMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Help", menu=helpMenu)

# 在菜单栏Help下添加一个名为About的选项
helpMenu.add_command(label="About")


def click_me():
    action.configure(text='hello'+name.get()+' '+numberChosen.get())
    print('check3 is {} {}'.format(type(chvarEn.get()), chvarEn.get()))


# 按钮
action = ttk.Button(monty, text='click me', command=click_me)
action.grid(column=2, padx=5, row=1)

# 文本框
name = tk.StringVar()
nameEntered = ttk.Entry(monty, width=12, textvariable=name)
nameEntered.grid(column=0, padx=5, row=1)
nameEntered.focus()

# 下拉框
number = tk.StringVar()
numberChosen = ttk.Combobox(
    monty, width=12, textvariable=number, state='readonly')
numberChosen['values'] = (1, 2, 4, 8, 16, 32, 64)
numberChosen.grid(column=1, padx=5, row=1)
numberChosen.current(0)
# 复选框
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(monty, text="disabled",
                        variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, padx=5, sticky=tk.W)

chvarUn = tk.IntVar()
check2 = tk.Checkbutton(monty, text='unchecked', variable=chvarUn)
check2.select()
check2.grid(column=1, row=4, padx=5, sticky=tk.W)

chvarEn = tk.IntVar()
check3 = tk.Checkbutton(monty, text='enabled', variable=chvarEn)
check3.select()
check3.grid(column=2, row=4, padx=5, sticky=tk.W)

# 单选框
COLOR1 = "Blue"
COLOR2 = "Gold"
COLOR3 = "Chocolate1"
# 单选框回调


def radCall():
    radSel = radVar.get()
    if radSel == 1:
        win.configure(background=COLOR1)
    elif radSel == 2:
        win.configure(background=COLOR2)
    elif radSel == 3:
        win.configure(background=COLOR3)


radVar = tk.IntVar()
rad1 = tk.Radiobutton(monty, text=COLOR1, variable=radVar,
                      value=1, command=radCall)
rad1.grid(column=0, row=5, padx=5, sticky=tk.W)
rad2 = tk.Radiobutton(monty, text=COLOR2, variable=radVar,
                      value=2, command=radCall)
rad2.grid(column=1, row=5, padx=5, sticky=tk.W)
rad3 = tk.Radiobutton(monty, text=COLOR3, variable=radVar,
                      value=3, command=radCall)
rad3.grid(column=2, row=5, padx=5, sticky=tk.W)

# 滚动文本框
scr = scrolledtext.ScrolledText(monty, width=30, height=3, wrap=tk.WORD)
scr.grid(column=0, pady=10, columnspan=3)

# 创建一个容器,其父容器为monty
labelsFrame = ttk.LabelFrame(monty, text='Labels in a Frame')
labelsFrame.grid(column=1, row=7)

# 将标签放入到容器中
ttk.Label(labelsFrame, text='Label1').grid(column=0, row=0)
ttk.Label(labelsFrame, text='Label2').grid(column=1, row=0)
ttk.Label(labelsFrame, text='Label3').grid(column=2, row=0)

for child in labelsFrame.winfo_children():      # labelsFrame.winfo_children 可以获取labelsFrame容器的所有子部件的对象
    # 通过子部件对象的grid_configure()方法可以修改部件的属性
    child.grid_configure(padx=8, pady=4)


win.mainloop()
