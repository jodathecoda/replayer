from tkinter import *
from tkinter import filedialog as fd
import re
import time

global hide
hide = 999 #to hide unused images, add this var to x and y

global bFileIsOpen
bFileIsOpen = False

global bFileFinished
bFileFinished = False

global storage
storage = []

global hand_pointer
hand_pointer = 0 #current hand

global number_of_hands
number_of_hands = 0

global step_pointer # current step in current hand
step_pointer = 0

global label_title

global actions
actions = []

global action_pointer
action_pointer = -1

global pool

ws = Tk()
ws.title('ReplayeR')
ws.geometry('965x545')
#ws.geometry('965x495')
ws.config(bg='black')
ws.iconbitmap("assets\\icons\\AA_small.ico")

class Table:
    def __init__(self, title, pot, potx, poty, flop1, flop1x, flop1y, flop2, flop2x, flop2y, flop3, flop3x, flop3y, turn1, turn1x, turn1y, river1, river1x, river1y):
        self.title = title
        self.pot = pot
        self.potx = potx
        self.poty = poty
        self.flop1 = flop1
        self.flop1x = flop1x
        self.flop1y = flop1y
        self.flop2 = flop2
        self.flop2x = flop2x
        self.flop2y = flop2y
        self.flop3 = flop3
        self.flop3x = flop3x
        self.flop3y = flop3y
        self.turn1 = turn1
        self.turn1x = turn1x
        self.turn1y = turn1y
        self.river1 = river1
        self.river1x = river1x
        self.river1y = river1y

global thetable
thetable = Table("", 0.0, 440, 285, "nocard", 385, 240, "nocard", 415, 240, "nocard", 445, 240, "nocard", 475, 240, "nocard", 505, 240)

class Player:
    def __init__(self, name, namex, namey, bet, betx, bety, stack, stackx, stacky,  seat, card1, card1x, card1y, card2, card2x, card2y, button, buttonx, buttony):
        self.name = name
        self.namex = namex
        self.namey = namey
        self.bet = bet
        self.betx = betx
        self.bety = bety
        self.stack = stack
        self.stackx = stackx
        self.stacky = stacky
        self.seat = seat
        self.card1 = card1
        self.card1x = card1x
        self.card1y = card1y
        self.card2 = card2
        self.card2x = card2x
        self.card2y = card2y
        self.button = button
        self.buttonx = buttonx
        self.buttony = buttony

global player1
global player2
global player3
global player4
global player5
global player6
global player7
global player8
#namex, namey, bet, betx, bety, stack, stackx, stacky,  seat, card1,   card1x,card1y card2, card2x, card2y button, buttonx, buttony):

player1 = Player("SitOut", 430, 450, 0.0, 500, 340, 0.0, 500, 450, 0, "", 435, 340, "", 470, 340, False, 415, 375)
player2 = Player("SitOut", 110, 450, 0.0, 330, 340, 0.0, 100, 410, 0, "", 260, 340, "", 295, 340, False, 240, 345)
player3 = Player("SitOut", 70, 260, 0.0, 255, 240, 0.0, 70, 290, 0, "", 190, 240, "", 225, 240, False, 205, 287)
player4 = Player("SitOut", 110, 70, 0.0, 330, 160, 0.0, 100, 110, 0, "", 260, 160, "", 295, 160, False, 240, 175) #4
player5 = Player("SitOut", 420, 70, 0.0, 500, 160, 0.0, 500, 70, 0, "", 435, 160, "", 470, 160, False, 415, 170) #5
player6 = Player("SitOut", 780, 70, 0.0, 610, 200, 0.0, 790, 110, 0, "", 635, 160, "", 670, 160, False, 700, 170) #6
player7 = Player("SitOut", 820, 260, 0.0, 610, 250, 0.0, 820, 290, 0, "", 700, 240, "", 730, 240, False, 740, 280) #7
player8 = Player("SitOut", 780, 450, 0.0, 610, 300, 0.0, 780, 410, 0, "", 640, 340, "", 675, 340, False, 715, 340) #8

pool = []
pool.append(player1)
pool.append(player2)
pool.append(player3)
pool.append(player4)
pool.append(player5)
pool.append(player6)
pool.append(player7)
pool.append(player8)

img = PhotoImage(file='assets\\table\\table5.png')

img_back = PhotoImage(file='assets\\buttons\\back_step.png')
img_play = PhotoImage(file='assets\\buttons\\play.png')
img_play_green = PhotoImage(file='assets\\buttons\\play_green.png')
img_pause = PhotoImage(file='assets\\buttons\\pause.png')
img_pause_red = PhotoImage(file='assets\\buttons\\pause_red.png')
img_forward = PhotoImage(file='assets\\buttons\\forward_step.png')
img_next = PhotoImage(file='assets\\buttons\\next.png')
img_previous = PhotoImage(file='assets\\buttons\\previous.png')
img_open = PhotoImage(file='assets\\buttons\\open.png')
img_settings = PhotoImage(file='assets\\buttons\\settings.png')

img_db = PhotoImage(file='assets\\chips\\db.png')

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

def display():
    global player1
    global player2
    global player3
    global player4
    global player5
    global player6
    global player7
    global player8

    button_f1.config(image = dealer(thetable.flop1))
    button_f2.config(image = dealer(thetable.flop2))
    button_f3.config(image = dealer(thetable.flop3))
    button_t1.config(image = dealer(thetable.turn1))
    button_r1.config(image = dealer(thetable.river1))
    button_pot.config(text = str(thetable.pot))


    label_player1.config(text=player1.name)
    ps1 = round(player1.stack,2)
    if player1.name == "SitOut":
        label_player1.place(x=9999, y=9999)
        label_player1_stack.place(x=9999, y=9999)
        button_bet1.place(x=9999, y=9999)
        button_p1c1.place(x=9999, y=9999)
        button_p1c2.place(x=9999, y=9999)
    else:
        label_player1.place(x=player1.namex, y=player1.namey)
        label_player1_stack.place(x=player1.stackx, y=player1.stacky)
        button_bet1.place(x=player1.betx, y=player1.bety)
        button_p1c1.place(x=player1.card1x, y=player1.card1y)
        button_p1c2.place(x=player1.card2x, y=player1.card2y)
    label_player1_stack.config(text=str(ps1))
    if player1.button:
        button_p1_db.place(x=player1.buttonx, y=player1.buttony)
    else:
        button_p1_db.place(x=9999, y=9999)

    button_bet1.config(text = str(player1.bet))
    button_p1c1.config(image = dealer(player1.card1))
    button_p1c2.config(image = dealer(player1.card2))

    label_player2.config(text=player2.name)
    ps2 = round(player2.stack,2)
    if player2.name == "SitOut":
        label_player2.place(x=9999, y=9999)
        label_player2_stack.place(x=9999, y=9999)
        button_bet2.place(x=9999, y=9999)
        button_p2c1.place(x=9999, y=9999)
        button_p2c2.place(x=9999, y=9999)
    else:
        label_player2.place(x=player2.namex, y=player2.namey)
        label_player2_stack.place(x=player2.stackx, y=player2.stacky)
        button_bet2.place(x=player2.betx, y=player2.bety)
        button_p2c1.place(x=player2.card1x, y=player2.card1y)
        button_p2c2.place(x=player2.card2x, y=player2.card2y)
    label_player2_stack.config(text=str(ps2))
    if player2.button:
        button_p2_db.place(x=player2.buttonx, y=player2.buttony)
    else:
        button_p2_db.place(x=9999, y=9999)
    button_bet2.config(text = str(player2.bet))
    button_p2c1.config(image = dealer(player2.card1))
    button_p2c2.config(image = dealer(player2.card2))

    label_player3.config(text=player3.name)
    ps3 = round(player3.stack,2)
    if player3.name == "SitOut":
        label_player3.place(x=9999, y=9999)
        label_player3_stack.place(x=9999, y=9999)
        button_bet3.place(x=9999, y=9999)
        button_p3c1.place(x=9999, y=9999)
        button_p3c2.place(x=9999, y=9999)
    else:
        label_player3.place(x=player3.namex, y=player3.namey)
        label_player3_stack.place(x=player3.stackx, y=player3.stacky)
        button_bet3.place(x=player3.betx, y=player3.bety)
        button_p3c1.place(x=player3.card1x, y=player3.card1y)
        button_p3c2.place(x=player3.card2x, y=player3.card2y)
    label_player3_stack.config(text=str(ps3))
    if player3.button:
        button_p3_db.place(x=player3.buttonx, y=player3.buttony)
    else:
        button_p3_db.place(x=9999, y=9999)
    button_bet3.config(text = str(player3.bet))
    button_p3c1.config(image = dealer(player3.card1))
    button_p3c2.config(image = dealer(player3.card2))

    label_player4.config(text=player4.name)
    ps4 = round(player4.stack,2)
    if player4.name == "SitOut":
        label_player4.place(x=9999, y=9999)
        label_player4_stack.place(x=9999, y=9999)
        button_bet4.place(x=9999, y=9999)
        button_p4c1.place(x=9999, y=9999)
        button_p4c2.place(x=9999, y=9999)
    else:
        label_player4.place(x=player4.namex, y=player4.namey)
        label_player4_stack.place(x=player4.stackx, y=player4.stacky)
        button_bet4.place(x=player4.betx, y=player4.bety)
        button_p4c1.place(x=player4.card1x, y=player4.card1y)
        button_p4c2.place(x=player4.card2x, y=player4.card2y)
    label_player4_stack.config(text=str(ps4))
    if player4.button:
        button_p4_db.place(x=player4.buttonx, y=player4.buttony)
    else:
        button_p4_db.place(x=9999, y=9999)
    button_bet4.config(text = str(player4.bet))
    button_p4c1.config(image = dealer(player4.card1))
    button_p4c2.config(image = dealer(player4.card2))

    label_player5.config(text=player5.name)
    ps5 = round(player5.stack,2)
    if player5.name == "SitOut":
        label_player5.place(x=9999, y=9999)
        label_player5_stack.place(x=9999, y=9999)
        button_bet5.place(x=9999, y=9999)
        button_p5c1.place(x=9999, y=9999)
        button_p5c2.place(x=9999, y=9999)
    else:
        label_player5.place(x=player5.namex, y=player5.namey)
        label_player5_stack.place(x=player5.stackx, y=player5.stacky)
        button_bet5.place(x=player5.betx, y=player5.bety)
        button_p5c1.place(x=player5.card1x, y=player5.card1y)
        button_p5c2.place(x=player5.card2x, y=player5.card2y)
    label_player5_stack.config(text=str(ps5))
    if player5.button:
        button_p5_db.place(x=player5.buttonx, y=player5.buttony)
    else:
        button_p5_db.place(x=9999, y=9999)
    button_bet5.config(text = str(player5.bet))
    button_p5c1.config(image = dealer(player5.card1))
    button_p5c2.config(image = dealer(player5.card2))

    label_player6.config(text=player6.name)
    ps6 = round(player6.stack,2)
    if player6.name == "SitOut":
        label_player6.place(x=9999, y=9999)
        label_player6_stack.place(x=9999, y=9999)
        button_bet6.place(x=9999, y=9999)
        button_p6c1.place(x=9999, y=9999)
        button_p6c2.place(x=9999, y=9999)
    else:
        label_player6.place(x=player6.namex, y=player6.namey)
        label_player6_stack.place(x=player6.stackx, y=player6.stacky)
        button_bet6.place(x=player6.betx, y=player6.bety)
        button_p6c1.place(x=player6.card1x, y=player6.card1y)
        button_p6c2.place(x=player6.card2x, y=player6.card2y)
    label_player6_stack.config(text=str(ps6))
    if player6.button:
        button_p6_db.place(x=player6.buttonx, y=player6.buttony)
    else:
        button_p6_db.place(x=9999, y=9999)
    button_bet6.config(text = str(player6.bet))
    button_p6c1.config(image = dealer(player6.card1))
    button_p6c2.config(image = dealer(player6.card2))

    label_player7.config(text=player7.name)
    ps7 = round(player7.stack,2)
    if player7.name == "SitOut":
    #if False:
        label_player7.place(x=9999, y=9999)
        label_player7_stack.place(x=9999, y=9999)
        button_bet7.place(x=9999, y=9999)
        button_p7c1.place(x=9999, y=9999)
        button_p7c2.place(x=9999, y=9999)
    else:
        label_player7.place(x=player7.namex, y=player7.namey)
        label_player7_stack.place(x=player7.stackx, y=player7.stacky)
        button_bet7.place(x=player7.betx, y=player7.bety)
        button_p7c1.place(x=player7.card1x, y=player7.card1y)
        button_p7c2.place(x=player7.card2x, y=player7.card2y)
    label_player7_stack.config(text=str(ps7))
    if player7.button:
        button_p7_db.place(x=player7.buttonx, y=player7.buttony)
    else:
        button_p7_db.place(x=9999, y=9999)
    button_bet7.config(text = str(player7.bet))
    button_p7c1.config(image = dealer(player7.card1))
    button_p7c2.config(image = dealer(player7.card2))

    label_player8.config(text=player8.name)
    ps8 = round(player8.stack,2)
    if player8.name == "SitOut":
    #if False:
        label_player8.place(x=9999, y=9999)
        label_player8_stack.place(x=9999, y=9999)
        button_bet8.place(x=9999, y=9999)
        button_p8c1.place(x=9999, y=9999)
        button_p8c2.place(x=9999, y=9999)
    else:
        label_player8.place(x=player8.namex, y=player8.namey)
        label_player8_stack.place(x=player8.stackx, y=player8.stacky)
        button_bet8.place(x=player8.betx, y=player8.bety)
        button_p8c1.place(x=player8.card1x, y=player8.card1y)
        button_p8c2.place(x=player8.card2x, y=player8.card2y)
    label_player8_stack.config(text=str(ps8))
    if player8.button:
        button_p8_db.place(x=player8.buttonx, y=player8.buttony)
    else:
        button_p8_db.place(x=9999, y=9999)
    button_bet8.config(text = str(player8.bet))
    button_p8c1.config(image = dealer(player8.card1))
    button_p8c2.config(image = dealer(player8.card2))

def dealer(carta):
    if carta == "As":
        return img_card_As
    if carta == "Ks":
        return img_card_Ks
    if carta == "Qs":
        return img_card_Qs
    if carta == "Js":
        return img_card_Js
    if carta == "Ts":
        return img_card_Ts
    if carta == "9s":
        return img_card_9s
    if carta == "8s":
        return img_card_8s
    if carta == "7s":
        return img_card_7s
    if carta == "6s":
        return img_card_6s
    if carta == "5s":
        return img_card_5s
    if carta == "4s":
        return img_card_4s
    if carta == "3s":
        return img_card_3s
    if carta == "2s":
        return img_card_2s

    if carta == "Ah":
        return img_card_Ah
    if carta == "Kh":
        return img_card_Kh
    if carta == "Qh":
        return img_card_Qh
    if carta == "Jh":
        return img_card_Jh
    if carta == "Th":
        return img_card_Th
    if carta == "9h":
        return img_card_9h
    if carta == "8h":
        return img_card_8h
    if carta == "7h":
        return img_card_7h
    if carta == "6h":
        return img_card_6h
    if carta == "5h":
        return img_card_5h
    if carta == "4h":
        return img_card_4h
    if carta == "3h":
        return img_card_3h
    if carta == "2h":
        return img_card_2h
    
    if carta == "Ad":
        return img_card_Ad
    if carta == "Kd":
        return img_card_Kd
    if carta == "Qd":
        return img_card_Qd
    if carta == "Jd":
        return img_card_Jd
    if carta == "Td":
        return img_card_Td
    if carta == "9d":
        return img_card_9d
    if carta == "8d":
        return img_card_8d
    if carta == "7d":
        return img_card_7d
    if carta == "6d":
        return img_card_6d
    if carta == "5d":
        return img_card_5d
    if carta == "4d":
        return img_card_4d
    if carta == "3d":
        return img_card_3d
    if carta == "2d":
        return img_card_2d

    if carta == "Ac":
        return img_card_Ac
    if carta == "Kc":
        return img_card_Kc
    if carta == "Qc":
        return img_card_Qc
    if carta == "Jc":
        return img_card_Jc
    if carta == "Tc":
        return img_card_Tc
    if carta == "9c":
        return img_card_9c
    if carta == "8c":
        return img_card_8c
    if carta == "7c":
        return img_card_7c
    if carta == "6c":
        return img_card_6c
    if carta == "5c":
        return img_card_5c
    if carta == "4c":
        return img_card_4c
    if carta == "3c":
        return img_card_3c
    if carta == "2c":
        return img_card_2c
    if carta == "fo":
        return img_card_back_fo
    if carta == "ld":
        return img_card_back_ld
    
    return img_card_back
    

def print_players_starting_info():
    global player1
    global player2
    global player3
    global player4
    global player5
    global player6
    global player7
    global player8
    global thetable

    print("Pot is: " + str(thetable.pot))
    print(str(player1.seat) + " " + player1.name + " " + str(player1.stack) + " " + player1.card1 + " " + player1.card2 + " " + str(player1.bet) + " " + str(player1.button))
    print(str(player2.seat) + " " + player2.name + " " + str(player2.stack) + " " + player2.card1 + " " + player2.card2 + " " + str(player2.bet) + " " + str(player2.button))
    print(str(player3.seat) + " " + player3.name + " " + str(player3.stack) + " " + player3.card1 + " " + player3.card2 + " " + str(player3.bet) + " " + str(player3.button))
    print(str(player4.seat) + " " + player4.name + " " + str(player4.stack) + " " + player4.card1 + " " + player4.card2 + " " + str(player4.bet) + " " + str(player4.button))
    print(str(player5.seat) + " " + player5.name + " " + str(player5.stack) + " " + player5.card1 + " " + player5.card2 + " " + str(player5.bet) + " " + str(player5.button))
    print(str(player6.seat) + " " + player6.name + " " + str(player6.stack) + " " + player6.card1 + " " + player6.card2 + " " + str(player6.bet) + " " + str(player6.button))
    print(str(player7.seat) + " " + player7.name + " " + str(player7.stack) + " " + player7.card1 + " " + player7.card2 + " " + str(player7.bet) + " " + str(player7.button))
    print(str(player8.seat) + " " + player8.name + " " + str(player8.stack) + " " + player8.card1 + " " + player8.card2 + " " + str(player8.bet) + " " + str(player8.button))

def extract_cards(line):
    #print(line)
    # Check if the line starts with "Dealt"
    if line.startswith("Dealt to"):
        # Use a regular expression to find the cards
        match = re.search(r'\[([2-9TJQKA][shdc])\s([2-9TJQKA][shdc])\]', line)
        if match:
            # If a match is found, return the cards
            return match.group(1), match.group(2)
    # If the line does not start with "Dealt" or no match is found, return None
    return None

def extract_cards_gather(line):
    card_regex = r"\b([A-Z0-9][a-z])\b"

    # Find all the matches in the line
    matches = re.findall(card_regex, line)
    print(matches)
    return matches

def clear_seats():
    global player1
    global player2
    global player3
    global player4
    global player5
    global player6
    global player7
    global player8
    global thetable
    global label_title

    thetable.flop1 = ""
    thetable.flop2 = ""
    thetable.flop3 = ""
    thetable.turn1 = ""
    thetable.river1 = ""


    player1.bet = 0.0
    player1.card1 = ""
    player1.card2 = ""
    player1.card1 = img_back
    player1.card2 = img_back

    player2.bet = 0.0
    player2.card1 = ""
    player2.card2 = ""
    player2.card1 = img_back
    player2.card2 = img_back

    player3.bet = 0.0
    player3.card1 = ""
    player3.card2 = ""
    player3.card1 = img_back
    player3.card2 = img_back

    player4.bet = 0.0
    player4.card1 = ""
    player4.card2 = ""
    player4.card1 = img_back
    player4.card2 = img_back

    player5.bet = 0.0
    player5.card1 = ""
    player5.card2 = ""
    player5.card1 = img_back
    player5.card2 = img_back

    player6.bet = 0.0
    player6.card1 = ""
    player6.card2 = ""
    player6.card1 = img_back
    player6.card2 = img_back

    player7.bet = 0.0
    player7.card1 = ""
    player7.card2 = ""
    player7.card1 = img_back
    player7.card2 = img_back

    player8.bet = 0.0
    player8.card1 = ""
    player8.card2 = ""
    player8.card1 = img_back
    player8.card2 = img_back

def extract_info(line):
    global player1
    global player2
    global player3
    global player4
    global player5
    global player6
    global player7
    global player8
    global thetable
    global label_title

    if line.startswith("PokerStars"):
        # If it is, set the flag to False
        thetable.title = line
        label_title.config(text=thetable.title)

    if line.startswith("Dealt to"):
        cards = extract_cards(line)
        if player1.name in line:
            player1.card1 = cards[0]
            player1.card2 = cards[1]
        elif player2.name in line:
            player2.card1 = cards[0]
            player2.card2 = cards[1]
        elif player3.name in line:
            player3.card1 = cards[0]
            player3.card2 = cards[1]
        elif player4.name in line:
            player4.card1 = cards[0]
            player4.card2 = cards[1]
        elif player5.name in line:
            player5.card1 = cards[0]
            player5.card2 = cards[1]
        elif player6.name in line:
            player6.card1 = cards[0]
            player6.card2 = cards[1]
        elif player7.name in line:
            player7.card1 = cards[0]
            player7.card2 = cards[1]
        elif player8.name in line:
            player8.card1 = cards[0]
            player8.card2 = cards[1]

    if line.startswith("Table") and "button" in line:
        ints = re.findall(r'\d+', line)
        #print("DB is: " + str(ints[-1]))
        player1.button = False
        player2.button = False
        player3.button = False
        player4.button = False
        player5.button = False
        player6.button = False
        db = str(ints[-1])
        if '1' in db:
            player1.button = True
        elif '2' in db:
            player2.button = True
        elif '3' in db:
            player3.button = True
        elif '4' in db:
            player4.button = True
        elif '5' in db:
            player5.button = True
        elif '6' in db:
            player6.button = True
        else:
            print("error finding the Button!")


    # Check if the line starts with "Seat"
    if line.startswith("Seat") and "folded" not in line and "collected" not in line:
        # Use a regular expression to find the first integer and name
        match = re.search(r'(\d+):\s([A-Za-z]+(?:\s[A-Za-z]+)*)', line)
        if match:
            # If a match is found, find all floats in the line
            floats = re.findall(r'[-+]?\d*\.\d+|\d+', line)
            if floats:
                # If any floats are found, return the first integer, name, and last float
                if int(match.group(1)) == 1:
                    player1.name = match.group(2)  
                    player1.seat = int(match.group(1))
                    ps1 = float(floats[-1])
                    player1.stack = round(ps1,2) 
                elif int(match.group(1)) == 2:
                    player2.name = match.group(2)  
                    player2.seat = int(match.group(1))
                    ps2 = float(floats[-1])
                    player2.stack = round(ps2,2)
                elif int(match.group(1)) == 3:
                    player3.name = match.group(2)  
                    player3.seat = int(match.group(1))
                    ps3 = float(floats[-1])
                    player3.stack = round(ps3,2)
                elif int(match.group(1)) == 4:
                    player4.name = match.group(2)  
                    player4.seat = int(match.group(1))
                    ps4 = float(floats[-1])
                    player4.stack = round(ps4,2)
                elif int(match.group(1)) == 5:
                    player5.name = match.group(2)  
                    player5.seat = int(match.group(1))
                    ps5 = float(floats[-1])
                    player5.stack = round(ps5,2)
                elif int(match.group(1)) == 6:
                    player6.name = match.group(2)  
                    player6.seat = int(match.group(1))
                    ps6 = float(floats[-1])
                    player6.stack = round(ps6,2)
                elif int(match.group(1)) == 7:
                    player7.name = match.group(2)  
                    player7.seat = int(match.group(1))
                    ps7 = float(floats[-1])
                    player7.stack = round(ps7,2)
                elif int(match.group(1)) == 8:
                    player8.name = match.group(2)  
                    player8.seat = int(match.group(1))
                    ps8 = float(floats[-1])
                    player8.stack = round(ps8,2)
                else:
                    pass
    if "posts" in line:
        match = re.search(r'(\d+):\s([A-Za-z]+(?:\s[A-Za-z]+)*)', line)
        if True:
            # If a match is found, find all floats in the line
            floats = re.findall(r'[-+]?\d*\.\d+|\d+', line)
            if floats:
                if player1.name in line:
                    player1.bet = round(float(floats[-1]),2)
                    ps1 = player1.stack
                    ps1 -= float(floats[-1])
                    player1.stack = round(ps1,2)
                    thetable.pot += round(float(floats[-1]),2)
                if player2.name in line:
                    player2.bet = round(float(floats[-1]),2)
                    ps2 = player2.stack
                    ps2 -= float(floats[-1])
                    player2.stack = round(ps2,2)
                    thetable.pot += round(float(floats[-1]),2)
                if player3.name in line:
                    player3.bet = round(float(floats[-1]),2)
                    ps3 = player3.stack
                    ps3 -= float(floats[-1])
                    player3.stack = round(ps3,2)
                    thetable.pot += round(float(floats[-1]),2)
                if player4.name in line:
                    player4.bet = round(float(floats[-1]),2)
                    ps4 = player4.stack
                    ps4 -= float(floats[-1])
                    player4.stack = round(ps4,2)
                    thetable.pot += round(float(floats[-1]),2)
                if player5.name in line:
                    player5.bet = round(float(floats[-1]),2)
                    ps5 = player5.stack
                    ps5 -= float(floats[-1])
                    player5.stack = round(ps5,2)
                    thetable.pot += round(float(floats[-1]),2)
                if player6.name in line:
                    player6.bet = round(float(floats[-1]),2)
                    ps6 = player6.stack
                    ps6 -= float(floats[-1])
                    player6.stack = round(ps6,2)
                    thetable.pot += round(float(floats[-1]),2)
                if player7.name in line:
                    player7.bet = round(float(floats[-1]),2)
                    ps7 = player7.stack
                    ps7 -= float(floats[-1])
                    player7.stack = round(ps7,2)
                    thetable.pot += round(float(floats[-1]),2)
                if player8.name in line:
                    player8.bet = round(float(floats[-1]),2)
                    ps8 = player8.stack
                    ps8 -= float(floats[-1])
                    player8.stack = round(ps8,2)
                    thetable.pot += round(float(floats[-1]),2)


def back():
    global bFileIsOpen
    global bFileFinished
    global storage
    global hand_pointer
    global number_of_hands
    global step_pointer
    global player1
    global player2
    global player3
    global player4
    global player5
    global player6
    global player7
    global player8
    global thetable
    global actions
    global action_pointer

    if not bFileIsOpen:
        open_f()

    print("back")
    button_play.config(image = img_play)
    button_pause.config(image = img_pause)
    if action_pointer:
        action_pointer -= 1
    gather_info_from_action()
    #print_players_starting_info()
    display()

def play():
    global bFileIsOpen
    global bFileFinished
    global storage
    global hand_pointer
    global number_of_hands
    global step_pointer
    global player1
    global player2
    global player3
    global player4
    global player5
    global player6
    global player7
    global player8
    global thetable
    global actions
    global action_pointer

    if not bFileIsOpen:
        open_f()

    print("play")
    button_play.config(image = img_play_green)
    button_pause.config(image = img_pause)

def pause():
    global bFileIsOpen
    global bFileFinished
    global storage
    global hand_pointer
    global number_of_hands
    global step_pointer
    global player1
    global player2
    global player3
    global player4
    global player5
    global player6
    global player7
    global player8
    global thetable
    global actions
    global action_pointer

    if not bFileIsOpen:
        open_f()

    print("pause")
    button_pause.config(image = img_pause_red)
    button_play.config(image = img_play)

def forward():
    global bFileIsOpen
    global bFileFinished
    global storage
    global hand_pointer
    global number_of_hands
    global step_pointer
    global player1
    global player2
    global player3
    global player4
    global player5
    global player6
    global player7
    global player8
    global thetable
    global actions
    global action_pointer

    if not bFileIsOpen:
        open_f()
    
    print("forward")
    button_play.config(image = img_play)
    button_pause.config(image = img_pause)
    action_pointer += 1
    gather_info_from_action()
    #print_players_starting_info()
    display()

def gather_info_from_action():
    global bFileIsOpen
    global bFileFinished
    global storage
    global hand_pointer
    global number_of_hands
    global step_pointer
    global player1
    global player2
    global player3
    global player4
    global player5
    global player6
    global player7
    global player8
    global thetable
    global label_title
    global actions

    infoto = actions[action_pointer]
    if action_pointer < 0:
        #go to previous hand
        previous()
    if (action_pointer +1 == len(actions)):
        #go to next hand
        next()

    print(infoto)
    if 'raises' in infoto:
        for p in pool:
            if p.name in infoto:
                floats = re.findall(r'[-+]?\d*\.\d+|\d+', infoto)
                if floats:
                    p.bet = float(floats[-1])
                    p.stack -= float(floats[-1])
                    bet = round(p.bet,2)
                    stack = round(p.stack,2)
                    p.bet = bet
                    p.stack = stack

    if 'bets' in infoto:
        for p in pool:
            if p.name in infoto:
                floats = re.findall(r'[-+]?\d*\.\d+|\d+', infoto)
                if floats:
                    p.bet += float(floats[-1])
                    p.stack -= float(floats[-1])
                    bet = round(p.bet,2)
                    stack = round(p.stack,2)
                    p.bet = bet
                    p.stack = stack

    if 'calls' in infoto:
        for p in pool:
            if p.name in infoto:
                floats = re.findall(r'[-+]?\d*\.\d+|\d+', infoto)
                if floats:
                    p.bet += float(floats[-1])
                    p.stack -= float(floats[-1])
                    bet = round(p.bet,2)
                    stack = round(p.stack,2)
                    p.bet = bet
                    p.stack = stack

    raw_pot  = player1.bet + player2.bet + player3.bet + player4.bet + player5.bet + player6.bet + player7.bet + player8.bet
    thetable.pot = round(raw_pot,2)

    if 'folds' in infoto:
        if player1.name in infoto:
            player1.card1 = "fo"
            player1.card2 = "ld"
            #print_players_starting_info()
        if player2.name in infoto:
            player2.card1 = "fo"
            player2.card2 = "ld"
        if player3.name in infoto:
            player3.card1 = "fo"
            player3.card2 = "ld"
        if player4.name in infoto:
            player4.card1 = "fo"
            player4.card2 = "ld"
        if player5.name in infoto:
            player5.card1 = "fo"
            player5.card2 = "ld"
        if player6.name in infoto:
            player6.card1 = "fo"
            player6.card2 = "ld"
        if player7.name in infoto:
            player7.card1 = "fo"
            player7.card2 = "ld"
        if player8.name in infoto:
            player8.card1 = "fo"
            player8.card2 = "ld"
    
    if 'shows' in infoto:
        cards = extract_cards_gather(infoto)
        if player1.name in infoto:
            player1.card1 = cards[0]
            player1.card2 = cards[1]
        elif player2.name in infoto:
            player2.card1 = cards[0]
            player2.card2 = cards[1]
        elif player3.name in infoto:
            player3.card1 = cards[0]
            player3.card2 = cards[1]
        elif player4.name in infoto:
            player4.card1 = cards[0]
            player4.card2 = cards[1]
        elif player5.name in infoto:
            player5.card1 = cards[0]
            player5.card2 = cards[1]
        elif player6.name in infoto:
            player6.card1 = cards[0]
            player6.card2 = cards[1]
        elif player7.name in infoto:
            player7.card1 = cards[0]
            player7.card2 = cards[1]
        elif player8.name in infoto:
            player8.card1 = cards[0]
            player8.card2 = cards[1]
    
    if "*** FLOP ***" in infoto:
        cards = extract_cards_gather(infoto)
        thetable.flop1 = cards[0]
        thetable.flop2 = cards[1]
        thetable.flop3 = cards[2]
    if "*** TURN ***" in infoto:
        cards = extract_cards_gather(infoto)
        thetable.flop1 = cards[0]
        thetable.flop2 = cards[1]
        thetable.flop3 = cards[2]
        thetable.turn1 = cards[3]
    if "*** RIVER ***" in infoto:
        cards = extract_cards_gather(infoto)
        thetable.flop1 = cards[0]
        thetable.flop2 = cards[1]
        thetable.flop3 = cards[2]
        thetable.turn1 = cards[3]
        thetable.river1 = cards[4]
    if "*** SUMMARY ***" in infoto:
        pass
        #clear cards
        '''
        player1.card1 = ""
        player1.card2 = ""
        player2.card1 = ""
        player2.card2 = ""
        player3.card1 = ""
        player3.card2 = ""
        player4.card1 = ""
        player4.card2 = ""
        player5.card1 = ""
        player5.card2 = ""
        player6.card1 = ""
        player6.card2 = ""
        player7.card1 = ""
        player7.card2 = ""
        player8.card1 = ""
        player8.card2 = ""
        '''

    label_subs.config(text=infoto)

def next():
    global bFileIsOpen
    global bFileFinished
    global storage
    global hand_pointer
    global number_of_hands
    global step_pointer
    global player1
    global player2
    global player3
    global player4
    global player5
    global player6
    global player7
    global player8
    global thetable
    global label_title
    global actions
    global action_pointer

    if not bFileIsOpen:
        open_f()

    thetable.pot = 0.0
    step_pointer = 0
    #print("next")
    button_play.config(image = img_play)
    button_pause.config(image = img_pause)
    if bFileIsOpen and not bFileFinished and hand_pointer < number_of_hands:
        for l in storage[hand_pointer]:
            #print(l)
            inside_summary = False
            if 'checks' in l:
                actions.append(l)
            if 'raises' in l:
                actions.append(l)
            if 'bets' in l:
                actions.append(l)
            if 'calls' in l:
                actions.append(l)
            if 'folds' in l:
                actions.append(l)
            if 'shows' in l:
                actions.append(l)
            if "*** SUMMARY ***" in l:
                actions.append(l)
                pass
            if "*** FLOP ***" in l:
                actions.append(l)
            if "*** TURN ***" in l:
                actions.append(l)
            if "*** RIVER ***" in l:
                actions.append(l)
           # Check if the l is "*** SUMMARY ***"
            if "*** SUMMARY ***" in l:
                # If it is, set the flag to True
                inside_summary = True
            # Check if the l is empty
            elif "PokerStars" in l:
                # If it is, set the flag to False
                inside_summary = False
                thetable.title = l
                label_title.config(text=thetable.title)
                clear_seats()
                extract_info(l)
            # If the flag is False, print the l
            elif not inside_summary:
                clear_seats
                extract_info(l)
        #print_players_starting_info()

        hand_pointer += 1    
    if hand_pointer == number_of_hands:
        bFileFinished = True
        print("Last Hand")
    #print_players_starting_info()
    display()
    

def previous():
    global bFileIsOpen
    global bFileFinished
    global storage
    global hand_pointer
    global number_of_hands
    global step_pointer
    global player1
    global player2
    global player3
    global player4
    global player5
    global player6
    global player7
    global player8
    global thetable
    global label_title
    global actions

    if not bFileIsOpen:
        open_f()

    step_pointer = 0
    thetable.pot = 0.0

    print("previous")
    button_play.config(image = img_play)
    button_pause.config(image = img_pause)

    if bFileIsOpen and not bFileFinished and hand_pointer > 0:
        for l in storage[hand_pointer]:
            inside_summary = False
            if 'checks' in l:
                actions.append(l)
            if 'raises' in l:
                actions.append(l)
            if 'bets' in l:
                actions.append(l)
            if 'calls' in l:
                actions.append(l)
            if 'folds' in l:
                actions.append(l)
            if 'shows' in l:
                actions.append(l)
            if "*** FLOP ***" in l:
                actions.append(l)
            if "*** TURN ***" in l:
                actions.append(l)
            if "*** RIVER ***" in l:
                actions.append(l)
           # Check if the l is "*** SUMMARY ***"
            if "*** SUMMARY ***" in l:
                # If it is, set the flag to True
                inside_summary = True
            # Check if the l is empty
            elif "PokerStars" in l:
                # If it is, set the flag to False
                inside_summary = False
                thetable.title = l
                label_title.config(text=thetable.title)
                clear_seats()
                extract_info(l)
            # If the flag is False, print the l
            elif not inside_summary:
                clear_seats()
                extract_info(l)
        #print_players_starting_info()
        hand_pointer -= 1
    if hand_pointer == 0:
        #bFileFinished = True
        print("First Hand")
    #print_players_starting_info()
    display()

def open_f():
    global bFileIsOpen
    global bFileFinished
    global storage
    global hand_pointer
    global number_of_hands
    global step_pointer
    global player1
    global player2
    global player3
    global player4
    global player5
    global player6
    global player7
    global player8
    global thetable

    print("open")
    button_play.config(image = img_play)
    button_pause.config(image = img_pause)
    filename_log = fd.askopenfilename()
    # Open the file for reading
    with open(filename_log, 'r') as f:
        bFileIsOpen = True
        # Initialize an empty list to store the lines
        # Iterate over the lines of the file
        for line in f:
            if 'PokerStars' in line:
                storage.append([])
                #thetable.title = line
                #label_title.config(text=thetable.title)
                storage[-1].append(line)
            # Otherwise, add the line to the latest list
            else:
                storage[-1].append(line)
        number_of_hands = len(storage)
    next()
        
def settings():
    global bFileIsOpen
    global bFileFinished
    global storage
    global hand_pointer
    global number_of_hands
    global step_pointer
    global player1
    global player2
    global player3
    global player4
    global player5
    global player6
    global player7
    global player8
    global thetable

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


label_player1 = Label(height=1, width=6, text=player1.name, bg='black', fg='lightblue',font=('Times New Roman', 15, 'bold'))
#label_player1.place(x=player1.namex, y=player1.namey)
label_player1.place(x=9999, y=9999)

label_player1_stack = Label(height=1, width=6, text="100", bg='black', fg='lightgreen',font=('Times New Roman', 15, 'bold'))
label_player1_stack.place(x=9999, y=9999)

button_p1_db = Button(image = img_db, bg='cornflowerblue')
button_p1_db.place(x=9999, y=9999)

button_p1c1 = Button(image = img_card_As)
button_p1c1.place(x=9999, y=9999)

button_p1c2 = Button(image = img_card_Kh)
button_p1c2.place(x=9999, y=9999)

button_bet1 = Button(text="", bg='cornflowerblue', fg='yellow',font=('Times New Roman', 15, 'bold'))
button_bet1.place(x=9999, y=9999)

label_player2 = Label(height=1, width=6, text="Player2", bg='black', fg='lightblue',font=('Times New Roman', 15, 'bold'))
label_player2.place(x=9999, y=9999)

label_player2_stack = Label(height=1, width=6, text="100", bg='black', fg='lightgreen',font=('Times New Roman', 15, 'bold'))
label_player2_stack.place(x=9999, y=9999)

button_p2_db = Button(image = img_db, bg='cornflowerblue')
button_p2_db.place(x=9999, y=9999)

button_p2c1 = Button(image = img_card_Qd)
button_p2c1.place(x=9999, y=9999)

button_p2c2 = Button(image = img_card_Qc)
button_p2c2.place(x=9999, y=9999)

button_bet2 = Button(text="", bg='cornflowerblue', fg='yellow',font=('Times New Roman', 15, 'bold'))
button_bet2.place(x=9999, y=9999)

label_player3 = Label(height=1, width=6, text="Player3", bg='black', fg='lightblue',font=('Times New Roman', 15, 'bold'))
label_player3.place(x=9999, y=9999)

label_player3_stack = Label(height=1, width=6, text="100", bg='black', fg='lightgreen',font=('Times New Roman', 15, 'bold'))
label_player3_stack.place(x=9999, y=9999)

button_p3_db = Button(image = img_db, bg='cornflowerblue')
button_p3_db.place(x=9999, y=9999)

button_p3c1 = Button(image = img_card_2s)
button_p3c1.place(x=9999, y=9999)

button_p3c2 = Button(image = img_card_7s)
button_p3c2.place(x=9999, y=9999)

button_bet3 = Button(text="", bg='cornflowerblue', fg='yellow',font=('Times New Roman', 15, 'bold'))
button_bet3.place(x=9999, y=9999)

label_player4 = Label(height=1, width=6, text="Player4", bg='black', fg='lightblue',font=('Times New Roman', 15, 'bold'))
label_player4.place(x=9999, y=9999)

label_player4_stack = Label(height=1, width=6, text="100", bg='black', fg='lightgreen',font=('Times New Roman', 15, 'bold'))
label_player4_stack.place(x=9999, y=9999)

button_bet4 = Button(text="", bg='cornflowerblue', fg='yellow',font=('Times New Roman', 15, 'bold'))
button_bet4.place(x=9999, y=9999)

button_p4_db = Button(image = img_db, bg='cornflowerblue')
button_p4_db.place(x=9999, y=9999)

button_p4c1 = Button(image = img_card_Jh)
button_p4c1.place(x=9999, y=9999)

button_p4c2 = Button(image = img_card_Jd)
button_p4c2.place(x=9999, y=9999)

label_player5 = Label(height=1, width=6, text="Player5", bg='black', fg='lightblue',font=('Times New Roman', 15, 'bold'))
label_player5.place(x=9999, y=9999)

button_bet5 = Button(text="", bg='cornflowerblue', fg='yellow',font=('Times New Roman', 15, 'bold'))
button_bet5.place(x=9999, y=9999)

label_player5_stack = Label(height=1, width=6, text="100", bg='black', fg='lightgreen',font=('Times New Roman', 15, 'bold'))
label_player5_stack.place(x=9999, y=9999)

button_p5_db = Button(image = img_db, bg='cornflowerblue')
button_p5_db.place(x=9999, y=9999)

button_p5c1 = Button(image = img_card_back_fo)
button_p5c1.place(x=9999, y=9999)

button_p5c2 = Button(image = img_card_back_ld)
button_p5c2.place(x=9999, y=9999)

label_player6 = Label(height=1, width=6, text="Player6", bg='black', fg='lightblue',font=('Times New Roman', 15, 'bold'))
label_player6.place(x=9999, y=9999)

label_player6_stack = Label(height=1, width=6, text="100", bg='black', fg='lightgreen',font=('Times New Roman', 15, 'bold'))
label_player6_stack.place(x=9999, y=9999)

button_p6c1 = Button(image = img_card_back)
button_p6c1.place(x=9999, y=9999)

button_p6_db = Button(image = img_db, bg='cornflowerblue')
button_p6_db.place(x=9999, y=9999)

button_p6c2 = Button(image = img_card_back)
button_p6c2.place(x=9999, y=9999)

button_bet6 = Button(text="", bg='cornflowerblue', fg='yellow',font=('Times New Roman', 15, 'bold'))
button_bet6.place(x=9999, y=9999)

label_player7 = Label(height=1, width=6, text="Player7", bg='black', fg='lightblue',font=('Times New Roman', 15, 'bold'))
label_player7.place(x=9999, y=9999)

label_player7_stack = Label(height=1, width=6, text="100", bg='black', fg='lightgreen',font=('Times New Roman', 15, 'bold'))
label_player7_stack.place(x=9999, y=9999)

button_p7_db = Button(image = img_db, bg='cornflowerblue')
button_p7_db.place(x=9999, y=9999)

button_p7c1 = Button(image = img_card_nocard, bg='cornflowerblue')
button_p7c1.place(x=9999, y=9999)

button_p7c2 = Button(image = img_card_nocard, bg='cornflowerblue')
button_p7c2.place(x=9999, y=9999)

button_bet7 = Button(text="", bg='cornflowerblue', fg='yellow',font=('Times New Roman', 15, 'bold'))
button_bet7.place(x=9999, y=9999)

label_player8 = Label(height=1, width=6, text="Player8", bg='black', fg='lightblue',font=('Times New Roman', 15, 'bold'))
label_player8.place(x=9999, y=9999)

label_player8_stack = Label(height=1, width=6, text="100", bg='black', fg='lightgreen',font=('Times New Roman', 15, 'bold'))
label_player8_stack.place(x=9999, y=9999)

button_p8_db = Button(image = img_db, bg='cornflowerblue')
button_p8_db.place(x=9999, y=9999)

button_p8c1 = Button(image = img_card_nocard, bg='cornflowerblue')
button_p8c1.place(x=9999, y=9999)

button_p8c2 = Button(image = img_card_nocard, bg='cornflowerblue')
button_p8c2.place(x=9999, y=9999)

button_bet8 = Button(text="", bg='cornflowerblue', fg='yellow',font=('Times New Roman', 15, 'bold'))
button_bet8.place(x=9999, y=9999)

# Board Cards
button_f1 = Button(image = img_card_Jh)
button_f1.place(x=thetable.flop1x, y=thetable.flop1y)

button_f2 = Button(image = img_card_As)
button_f2.place(x=thetable.flop2x, y=thetable.flop2y)

button_f3 = Button(image = img_card_back)
button_f3.place(x=thetable.flop3x, y=thetable.flop3y)

button_t1 = Button(image = img_card_back)
button_t1.place(x=thetable.turn1x, y=thetable.turn1y)

button_r1 = Button(image = img_card_back)
button_r1.place(x=thetable.river1x, y=thetable.river1y)

button_pot = Button(text="ReplayeR", bg='green', fg='yellow',font=('Times New Roman', 15, 'bold'))
button_pot.place(x=thetable.potx, y=thetable.poty)


label_title = Label(text=thetable.title, bg='black', fg='red',font=('Times New Roman', 13, 'bold'))
label_title.place(x=55,y= 10)

button_previous = Button(image = img_previous, command = previous)
#button_previous.place(x=340, y=500)
button_previous.place(x=9999, y=9999)

button_back = Button(image = img_back, command = back)
#button_back.place(x=390, y=500)
button_back.place(x=9999, y=9999)

button_play = Button(image = img_play, command = play)
#button_play.place(x=440, y=500)
button_play.place(x=9999, y=9999)

button_pause = Button(image = img_pause, command = pause)
#button_pause.place(x=490, y=500)
button_pause.place(x=9999, y=9999)

button_forward = Button(image = img_forward, command = forward)
button_forward.place(x=490, y=500)
#button_forward.place(x=540, y=500)

button_next = Button(image = img_next, command = next)
#button_next.place(x=590, y=500)
button_next.place(x=9999, y=9999)

button_open = Button(image = img_open, command = open_f)
button_open.place(x=450, y=500)
#button_open.place(x=560, y=10)

button_settings = Button(image = img_settings, command = settings)
#button_settings.place(x=10, y=10)
button_settings.place(x=9999, y=9999)

label_subs = Label(text="", bg='black', fg='goldenrod',font=('Times New Roman', 13, 'bold'))
label_subs.place(x=10,y= 490)

ws.mainloop()