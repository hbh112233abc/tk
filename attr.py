from tkinter import * #引入所有类
xin = Tk();
b1 = Button(xin,text="波波")
b1['width'] = 20
b1['height'] = 4
b1.pack()
b2 = Button(xin,text="BOBO")
b2['width'] = 25
b2['background'] = 'red'
b2.pack()
xin.mainloop()