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


def back():
    print("back")

def play():
    print("play")

def pause():
    print("pause")

def forward():
    print("forward")

def next():
    print("next")

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

#label_player1 = Label(height=1, width=6, text="Player1", bg='black')
label_player1 = Label(height=1, width=6, text="Player1", bg='black', fg='lightblue',font=('Times New Roman', 15, 'bold'))
label_player1.place(x=450, y=450)

label_player2 = Label(height=1, width=6, text="Player2", bg='black', fg='lightblue',font=('Times New Roman', 15, 'bold'))
label_player2.place(x=130, y=400)

label_player3 = Label(height=1, width=6, text="Player3", bg='black', fg='lightblue',font=('Times New Roman', 15, 'bold'))
label_player3.place(x=70, y=260)

label_player4 = Label(height=1, width=6, text="Player4", bg='black', fg='lightblue',font=('Times New Roman', 15, 'bold'))
label_player4.place(x=130, y=120)

button_back = Button(image = img_back, command = back)
button_back.place(x=360, y=500)

button_play = Button(image = img_play, command = play)
button_play.place(x=410, y=500)

button_pause = Button(image = img_pause, command = pause)
button_pause.place(x=460, y=500)

button_forward = Button(image = img_forward, command = forward)
button_forward.place(x=510, y=500)

button_next = Button(image = img_next, command = next)
button_next.place(x=560, y=500)

ws.mainloop()