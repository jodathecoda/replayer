from tkinter import *

ws = Tk()
ws.title('PythonGuides')
ws.geometry('965x545')
ws.config(bg='black')

img = PhotoImage(file='assets\\table\\table5.png')

img_back = PhotoImage(file='assets\\buttons\\back_step.png')
img_play = PhotoImage(file='assets\\buttons\\play.png')
img_play_green = PhotoImage(file='assets\\buttons\\play_green.png')
img_pause = PhotoImage(file='assets\\buttons\\pause.png')
img_pause_red = PhotoImage(file='assets\\buttons\\pause_red.png')
img_forward = PhotoImage(file='assets\\buttons\\forward_step.png')
img_next = PhotoImage(file='assets\\buttons\\next.png')
img_open = PhotoImage(file='assets\\buttons\\open.png')
img_settings = PhotoImage(file='assets\\buttons\\settings.png')

img_card_back = PhotoImage(file='assets\cards\\back.png')

img_card_2c = PhotoImage(file='assets\cards\\2clubs.png')
img_card_2d = PhotoImage(file='assets\cards\\2diamond.png')


def back():
    print("back")
    button_play.config(image = img_play)
    button_pause.config(image = img_pause)

def play():
    print("play")
    button_play.config(image = img_play_green)
    button_pause.config(image = img_pause)

def pause():
    print("pause")
    button_pause.config(image = img_pause_red)
    button_play.config(image = img_play)

def forward():
    print("forward")
    button_play.config(image = img_play)
    button_pause.config(image = img_pause)

def next():
    print("next")
    button_play.config(image = img_play)
    button_pause.config(image = img_pause)

def open_f():
    print("open")
    button_play.config(image = img_play)
    button_pause.config(image = img_pause)

def settings():
    print("settings")
    button_play.config(image = img_play)
    button_pause.config(image = img_pause)

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
label_player1.place(x=430, y=450)

label_player1_stack = Label(height=1, width=6, text="100", bg='black', fg='lightgreen',font=('Times New Roman', 15, 'bold'))
label_player1_stack.place(x=500, y=450)

button_p1c1 = Button(image = img_card_2c)
button_p1c1.place(x=435, y=340)

button_p1c2 = Button(image = img_card_2d)
button_p1c2.place(x=470, y=340)


label_player2 = Label(height=1, width=6, text="Player2", bg='black', fg='lightblue',font=('Times New Roman', 15, 'bold'))
label_player2.place(x=130, y=400)

label_player2_stack = Label(height=1, width=6, text="100", bg='black', fg='lightgreen',font=('Times New Roman', 15, 'bold'))
label_player2_stack.place(x=130, y=430)

label_player3 = Label(height=1, width=6, text="Player3", bg='black', fg='lightblue',font=('Times New Roman', 15, 'bold'))
label_player3.place(x=70, y=260)

label_player3_stack = Label(height=1, width=6, text="100", bg='black', fg='lightgreen',font=('Times New Roman', 15, 'bold'))
label_player3_stack.place(x=70, y=290)

label_player4 = Label(height=1, width=6, text="Player4", bg='black', fg='lightblue',font=('Times New Roman', 15, 'bold'))
label_player4.place(x=120, y=120)

label_player4_stack = Label(height=1, width=6, text="100", bg='black', fg='lightgreen',font=('Times New Roman', 15, 'bold'))
label_player4_stack.place(x=100, y=150)

label_player5 = Label(height=1, width=6, text="Player5", bg='black', fg='lightblue',font=('Times New Roman', 15, 'bold'))
label_player5.place(x=420, y=70)

label_player5_stack = Label(height=1, width=6, text="100", bg='black', fg='lightgreen',font=('Times New Roman', 15, 'bold'))
label_player5_stack.place(x=500, y=70)

label_player6 = Label(height=1, width=6, text="Player6", bg='black', fg='lightblue',font=('Times New Roman', 15, 'bold'))
label_player6.place(x=780, y=120)

label_player6_stack = Label(height=1, width=6, text="100", bg='black', fg='lightgreen',font=('Times New Roman', 15, 'bold'))
label_player6_stack.place(x=790, y=150)

label_player7 = Label(height=1, width=6, text="Player7", bg='black', fg='lightblue',font=('Times New Roman', 15, 'bold'))
label_player7.place(x=820, y=260)

label_player7_stack = Label(height=1, width=6, text="100", bg='black', fg='lightgreen',font=('Times New Roman', 15, 'bold'))
label_player7_stack.place(x=820, y=290)

label_player8 = Label(height=1, width=6, text="Player8", bg='black', fg='lightblue',font=('Times New Roman', 15, 'bold'))
label_player8.place(x=780, y=400)

label_player8_stack = Label(height=1, width=6, text="100", bg='black', fg='lightgreen',font=('Times New Roman', 15, 'bold'))
label_player8_stack.place(x=780, y=430)

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

button_open = Button(image = img_open, command = open_f)
button_open.place(x=60, y=10)

button_settings = Button(image = img_settings, command = settings)
button_settings.place(x=10, y=10)

ws.mainloop()