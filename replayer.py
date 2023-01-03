from tkinter import *

ws = Tk()
ws.title('ReplayeR')
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

img_card_2s = PhotoImage(file='assets\cards\\2spade.png')
img_card_2h = PhotoImage(file='assets\cards\\2hearts.png')
img_card_2d = PhotoImage(file='assets\cards\\2diamond.png')
img_card_2c = PhotoImage(file='assets\cards\\2clubs.png')

img_card_3s = PhotoImage(file='assets\cards\\3spade.png')
img_card_3h = PhotoImage(file='assets\cards\\3hearts.png')
img_card_3d = PhotoImage(file='assets\cards\\3diamond.png')
img_card_3c = PhotoImage(file='assets\cards\\3clubs.png')

img_card_4s = PhotoImage(file='assets\cards\\4spade.png')
img_card_4h = PhotoImage(file='assets\cards\\4hearts.png')
img_card_4d = PhotoImage(file='assets\cards\\4diamond.png')
img_card_4c = PhotoImage(file='assets\cards\\4clubs.png')

img_card_5s = PhotoImage(file='assets\cards\\5spade.png')
img_card_5h = PhotoImage(file='assets\cards\\5hearts.png')
img_card_5d = PhotoImage(file='assets\cards\\5diamond.png')
img_card_5c = PhotoImage(file='assets\cards\\5clubs.png')

img_card_6s = PhotoImage(file='assets\cards\\6spade.png')
img_card_6h = PhotoImage(file='assets\cards\\6hearts.png')
img_card_6d = PhotoImage(file='assets\cards\\6diamond.png')
img_card_6c = PhotoImage(file='assets\cards\\6clubs.png')

img_card_7s = PhotoImage(file='assets\cards\\7spade.png')
img_card_7h = PhotoImage(file='assets\cards\\7hearts.png')
img_card_7d = PhotoImage(file='assets\cards\\7diamond.png')
img_card_7c = PhotoImage(file='assets\cards\\7clubs.png')

img_card_8s = PhotoImage(file='assets\cards\\8spade.png')
img_card_8h = PhotoImage(file='assets\cards\\8hearts.png')
img_card_8d = PhotoImage(file='assets\cards\\8diamond.png')
img_card_8c = PhotoImage(file='assets\cards\\8clubs.png')

img_card_9s = PhotoImage(file='assets\cards\\9spade.png')
img_card_9h = PhotoImage(file='assets\cards\\9hearts.png')
img_card_9d = PhotoImage(file='assets\cards\\9diamond.png')
img_card_9c = PhotoImage(file='assets\cards\\9clubs.png')

img_card_Ts = PhotoImage(file='assets\cards\\Tspade.png')
img_card_Th = PhotoImage(file='assets\cards\\Thearts.png')
img_card_Td = PhotoImage(file='assets\cards\\Tdiamond.png')
img_card_Tc = PhotoImage(file='assets\cards\\Tclubs.png')

img_card_Js = PhotoImage(file='assets\cards\\Jspade.png')
img_card_Jh = PhotoImage(file='assets\cards\\Jhearts.png')
img_card_Jd = PhotoImage(file='assets\cards\\Jdiamond.png')
img_card_Jc = PhotoImage(file='assets\cards\\Jclubs.png')

img_card_Qs = PhotoImage(file='assets\cards\\Qspade.png')
img_card_Qh = PhotoImage(file='assets\cards\\Qhearts.png')
img_card_Qd = PhotoImage(file='assets\cards\\Qdiamond.png')
img_card_Qc = PhotoImage(file='assets\cards\\Qclubs.png')

img_card_Ks = PhotoImage(file='assets\cards\\Kspade.png')
img_card_Kh = PhotoImage(file='assets\cards\\Khearts.png')
img_card_Kd = PhotoImage(file='assets\cards\\Kdiamond.png')
img_card_Kc = PhotoImage(file='assets\cards\\Kclubs.png')

img_card_As = PhotoImage(file='assets\cards\\Aspade.png')
img_card_Ah = PhotoImage(file='assets\cards\\Ahearts.png')
img_card_Ad = PhotoImage(file='assets\cards\\Adiamond.png')
img_card_Ac = PhotoImage(file='assets\cards\\Aclubs.png')

img_card_back = PhotoImage(file='assets\cards\\back.png')
img_card_back_fo = PhotoImage(file='assets\cards\\back_fo.png')
img_card_back_ld = PhotoImage(file='assets\cards\\back_ld.png')
img_card_nocard = PhotoImage(file='assets\cards\\nocard.png')


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

label_player1 = Label(height=1, width=6, text="Player1", bg='black', fg='lightblue',font=('Times New Roman', 15, 'bold'))
label_player1.place(x=430, y=450)

label_player1_stack = Label(height=1, width=6, text="100", bg='black', fg='lightgreen',font=('Times New Roman', 15, 'bold'))
label_player1_stack.place(x=500, y=450)

button_p1c1 = Button(image = img_card_As)
button_p1c1.place(x=435, y=340)

button_p1c2 = Button(image = img_card_Kh)
button_p1c2.place(x=470, y=340)

button_bet1 = Button(text="", bg='blue', fg='yellow',font=('Times New Roman', 15, 'bold'))
button_bet1.place(x=500, y=340)

label_player2 = Label(height=1, width=6, text="Player2", bg='black', fg='lightblue',font=('Times New Roman', 15, 'bold'))
label_player2.place(x=110, y=450)

label_player2_stack = Label(height=1, width=6, text="100", bg='black', fg='lightgreen',font=('Times New Roman', 15, 'bold'))
label_player2_stack.place(x=100, y=410)

button_p2c1 = Button(image = img_card_Qd)
button_p2c1.place(x=260, y=340)

button_p2c2 = Button(image = img_card_Qc)
button_p2c2.place(x=295, y=340)

button_bet2 = Button(text="", bg='blue', fg='yellow',font=('Times New Roman', 15, 'bold'))
button_bet2.place(x=330, y=340)

label_player3 = Label(height=1, width=6, text="Player3", bg='black', fg='lightblue',font=('Times New Roman', 15, 'bold'))
label_player3.place(x=70, y=260)

label_player3_stack = Label(height=1, width=6, text="100", bg='black', fg='lightgreen',font=('Times New Roman', 15, 'bold'))
label_player3_stack.place(x=70, y=290)

button_p3c1 = Button(image = img_card_2s)
button_p3c1.place(x=190, y=240)

button_p3c2 = Button(image = img_card_7s)
button_p3c2.place(x=225, y=240)

button_bet3 = Button(text="", bg='blue', fg='yellow',font=('Times New Roman', 15, 'bold'))
button_bet3.place(x=255, y=240)

label_player4 = Label(height=1, width=6, text="Player4", bg='black', fg='lightblue',font=('Times New Roman', 15, 'bold'))
label_player4.place(x=110, y=70)

label_player4_stack = Label(height=1, width=6, text="100", bg='black', fg='lightgreen',font=('Times New Roman', 15, 'bold'))
label_player4_stack.place(x=100, y=110)

button_bet4 = Button(text="", bg='blue', fg='yellow',font=('Times New Roman', 15, 'bold'))
button_bet4.place(x=330, y=160)

button_p4c1 = Button(image = img_card_Jh)
button_p4c1.place(x=260, y=160)

button_p4c2 = Button(image = img_card_Jd)
button_p4c2.place(x=295, y=160)

label_player5 = Label(height=1, width=6, text="Player5", bg='black', fg='lightblue',font=('Times New Roman', 15, 'bold'))
label_player5.place(x=420, y=70)

button_bet5 = Button(text="", bg='blue', fg='yellow',font=('Times New Roman', 15, 'bold'))
button_bet5.place(x=500, y=160)

label_player5_stack = Label(height=1, width=6, text="100", bg='black', fg='lightgreen',font=('Times New Roman', 15, 'bold'))
label_player5_stack.place(x=500, y=70)

button_p5c1 = Button(image = img_card_back_fo)
button_p5c1.place(x=435, y=160)

button_p5c2 = Button(image = img_card_back_ld)
button_p5c2.place(x=470, y=160)

label_player6 = Label(height=1, width=6, text="Player6", bg='black', fg='lightblue',font=('Times New Roman', 15, 'bold'))
label_player6.place(x=780, y=70)

label_player6_stack = Label(height=1, width=6, text="100", bg='black', fg='lightgreen',font=('Times New Roman', 15, 'bold'))
label_player6_stack.place(x=790, y=110)

button_p6c1 = Button(image = img_card_back)
button_p6c1.place(x=635, y=160)

button_p6c2 = Button(image = img_card_back)
button_p6c2.place(x=670, y=160)

button_bet6 = Button(text="", bg='blue', fg='yellow',font=('Times New Roman', 15, 'bold'))
button_bet6.place(x=610, y=200)

label_player7 = Label(height=1, width=6, text="Player7", bg='black', fg='lightblue',font=('Times New Roman', 15, 'bold'))
label_player7.place(x=820, y=260)

label_player7_stack = Label(height=1, width=6, text="100", bg='black', fg='lightgreen',font=('Times New Roman', 15, 'bold'))
label_player7_stack.place(x=820, y=290)

button_p7c1 = Button(image = img_card_nocard, bg='blue')
button_p7c1.place(x=700, y=240)

button_p7c2 = Button(image = img_card_nocard, bg='blue')
button_p7c2.place(x=730, y=240)

button_bet7 = Button(text="", bg='blue', fg='yellow',font=('Times New Roman', 15, 'bold'))
button_bet7.place(x=610, y=250)

label_player8 = Label(height=1, width=6, text="Player8", bg='black', fg='lightblue',font=('Times New Roman', 15, 'bold'))
label_player8.place(x=780, y=450)

label_player8_stack = Label(height=1, width=6, text="100", bg='black', fg='lightgreen',font=('Times New Roman', 15, 'bold'))
label_player8_stack.place(x=780, y=410)

button_p8c1 = Button(image = img_card_nocard, bg='blue')
button_p8c1.place(x=640, y=340)

button_p8c2 = Button(image = img_card_nocard, bg='blue')
button_p8c2.place(x=675, y=340)

button_bet8 = Button(text="", bg='blue', fg='yellow',font=('Times New Roman', 15, 'bold'))
button_bet8.place(x=610, y=300)

# Board Cards
button_f1 = Button(image = img_card_4h)
button_f1.place(x=385, y=240)

button_f2 = Button(image = img_card_5h)
button_f2.place(x=415, y=240)

button_f3 = Button(image = img_card_7s)
button_f3.place(x=445, y=240)

button_t1 = Button(image = img_card_back)
button_t1.place(x=475, y=240)

button_r1 = Button(image = img_card_back)
button_r1.place(x=505, y=240)

button_pot = Button(text="2.87", bg='green', fg='yellow',font=('Times New Roman', 15, 'bold'))
button_pot.place(x=400, y=285)


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