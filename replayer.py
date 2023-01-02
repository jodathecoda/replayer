from tkinter import *

ws = Tk()
ws.title('PythonGuides')
ws.geometry('965x545')
ws.config(bg='black')

img = PhotoImage(file='assets\\table\\table5.png')
img_back = PhotoImage(file='assets\\buttons\\back_step.png')
img_play = PhotoImage(file='assets\\buttons\\play.png')
img_pause = PhotoImage(file='assets\\buttons\\pause.png')
img_forward = PhotoImage(file='assets\\buttons\\forward_step.png')
img_next = PhotoImage(file='assets\\buttons\\next.png')
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

button_back = Button(image = img_back)
button_back.place(x=360, y=500)

button_play = Button(image = img_play)
button_play.place(x=410, y=500)

button_pause = Button(image = img_pause)
button_pause.place(x=460, y=500)

button_forward = Button(image = img_forward)
button_forward.place(x=510, y=500)

button_next = Button(image = img_next)
button_next.place(x=560, y=500)

ws.mainloop()