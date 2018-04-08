from tkinter import *
def xinlabel (event):
    #global xin
    s = Label(xin,text="事件函数!")
    s.pack();

xin = Tk();
b1 = Button(xin,text="点我弹出文字1");
b2 = Button(xin,text="点我弹出文字2");
#特别理解好b1 = 那个Button,就绑定那个事件,也就是编程中的 对象 , 不是生活中的对象
b1.bind("<Button-1>",xinlabel)
b1.pack()
b2.pack()
xin.mainloop()
"""
bind
第一个参数是绑定<Button-1>按钮,前面是事件对象,其中1,2,3 分别代表鼠标左键,中,右
第二个参数是函数名,不要带任何标点符号,不然出错
<KeyPress-A>表示 A 键被按下，其中的 A 可以换成其他 的键位。
<Control-V>表示按下的是 Ctrl 和 V 键，V 可以换成其他 键位。
<F1>表示按下的是 F1 键，对于 Fn 系列的，都可以随便
"""