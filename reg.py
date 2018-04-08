#!/usr/bin/python
# -*- coding: UTF-8 -*-
from tkinter import *


def reg():
    s1 = e1.get()
    s2 = e2.get()
    t1 = len(s1)
    t2 = len(s2)
    if s1 == '111' and s2 == '111':
        c['text'] = '登录成功'
    else:
        c['text'] = '用户名或密码错误'
        e1.delete(0,t1)
        e2.delete(0,t2)

tk = Tk()
l1 = Label(tk,text="用户名:")
l1.grid(row=0,column=1,sticky=W)
e1 = Entry(tk)
e1.grid(row=0,column=1,sticky=E)

l2 = Label(tk,text="密码:")
l2.grid(row=1,column=0,sticky=W)
e2 = Entry(tk)
e2.grid(row=1,column=1,sticky=E)

b1 = Button(tk,text="登录",comman=reg)
b1.grid(row=2,column=1,sticky=E)

c = Label(tk,text='')
c.grid(row=3)
tk.mainloop()