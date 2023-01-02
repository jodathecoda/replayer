from tkinter import *

ws = Tk()
ws.title('PythonGuides')
ws.geometry('950x540')
ws.config(bg='black')

img = PhotoImage(file='assets\\table\\table5.png')
img_back = PhotoImage(file='assets\\buttons\\button_back.png')
label = Label(
    ws,
    image=img
)
label.place(x=0, y=0)

text = Text(
    ws,
    height=10,
    width=53
)
#text.place(x=30, y=50)

button_back = Button(
    ws,
    text='SEND',
    relief=RAISED,
    font=('Arial Bold', 18),
    image = img_back
)
button_back.place(x=190, y=250)

ws.mainloop()