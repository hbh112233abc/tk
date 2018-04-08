#!/usr/bin/python
# -*- coding: UTF-8 -*-
from tkinter.messagebox import *


showinfo(title="你好",message="How are you")

showwarning(title="警告",message="非法入侵")

showerror(title="错误",message="哎呀,出错了")

res = askquestion(title="问一下",message="中山路怎么走?")
print('askquestion:',res)

res = askokcancel(title="问一下",message="走不走?")
print('askokcancel:',res)

res = askyesno(title="问一下",message="走不走?")
print('askyesno:',res)

res = askyesnocancel(title="问一下",message="走不走?")
print('askyesnocancel:',res)

res = askretrycancel(title="再试一下",message="好不好?")
print('askretrycancel:',res)