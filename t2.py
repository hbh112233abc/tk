#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-05
# @Author  : huangbinghe (huangbinghe@gmail.com)
# @Link    : http://www.bingher.com
# @Version : $Id$

import os
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.messagebox import *
import threading

root = Tk()
root.wm_title('好好学习天天向上')  # 窗口标题
root.wm_geometry('600x500+650+200')  # 窗口大小width*height+x+y
root.iconbitmap('zy.ico')  # 窗口图标


class start_stop_thread(object):
    def __init__(self, **kw):
        super().__init__()

    def start_thread(self):
        # showinfo('开始', '爬虫开始启动了...')
        for i in range(100):
            scroll_bar.insert(END, 'test message {}\n'.format(i))
        vart.set('搞定 :)')

    def stop_thread(self):
        # showwarning('结束', '你结束了爬虫...')
        root.quit()


scroll_bar = ScrolledText(root, width=80, height=30,
                          bg='#ffffff')
scroll_bar.grid(column=0, row=0, padx=10, columnspan=3, sticky=N)

thread_new = start_stop_thread()
button = Button(root, text="确认爬取",  command=thread_new.start_thread)
button.grid(column=0, row=1, padx=20, sticky=E)
button_stop = Button(root, text="退出程序",
                     command=thread_new.stop_thread)
button_stop.grid(column=1, row=1, padx=20, sticky=E)

vart = StringVar()
vart.set('爬虫已准备,点击开始...')
label = Label(root, textvariable=vart, fg='red')
label.grid(column=2, row=1, padx=20, sticky=E)
root.mainloop()
