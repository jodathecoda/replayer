from tkinter import *
from tkinter import filedialog as fd
import re

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

ws = Tk()
ws.title('ReplayeR')
ws.geometry('965x545')
#ws.geometry('965x495')
ws.config(bg='black')
ws.iconbitmap("assets\\icons\\replayer_icon_small.ico")

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

player1 = Player("Empty", 430, 450, 0.0, 500, 340, 0.0, 500, 450, 0, "", 435, 340, "", 470, 340, False, 415, 375)
player2 = Player("Empty", 110, 450, 0.0, 330, 340, 0.0, 100, 410, 0, "", 260, 340, "", 295, 340, False, 240, 345)
player3 = Player("Empty", 70, 260, 0.0, 255, 240, 0.0, 70, 290, 0, "", 190, 240, "", 225, 240, False, 205, 287)
player4 = Player("Empty", 110, 70, 0.0, 330, 160, 0.0, 100, 110, 0, "", 260, 160, "", 295, 160, False, 240, 175) #4
player5 = Player("Empty", 420, 70, 0.0, 500, 160, 0.0, 500, 70, 0, "", 435, 160, "", 470, 160, False, 415, 170) #5
player6 = Player("Empty", 780, 70, 0.0, 610, 200, 0.0, 790, 110, 0, "", 635, 160, "", 670, 160, False, 700, 170) #6
player7 = Player("Empty", 820, 260, 0.0, 610, 250, 0.0, 820, 290, 0, "", 700, 240, "", 730, 240, False, 740, 280) #7
player8 = Player("Empty", 780, 450, 0.0, 610, 300, 0.0, 780, 410, 0, "", 640, 340, "", 675, 340, False, 715, 340) #8

#player1 = Player("Alice",21.2, 100.0, 4, "As", "Kh", "raise")

img = PhotoImage(file='assets\\table\\table5.png')
#img = PhotoImage(file='images\\visteon.png')

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
    print(line)
    # Check if the line starts with "Dealt"
    if line.startswith("Dealt to"):
        # Use a regular expression to find the cards
        match = re.search(r'\[([2-9TJQKA][shdc])\s([2-9TJQKA][shdc])\]', line)
        if match:
            # If a match is found, return the cards
            return match.group(1), match.group(2)
    # If the line does not start with "Dealt" or no match is found, return None
    return None


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
        inside_summary = False
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
                    player1.stack = round(float(floats[-1]),2)
                    player1.seat = int(match.group(1))
                elif int(match.group(1)) == 2:
                    player2.name = match.group(2)
                    player2.stack = round(float(floats[-1]),2)
                    player2.seat = int(match.group(1))
                elif int(match.group(1)) == 3:
                    player3.name = match.group(2)
                    player3.stack = round(float(floats[-1]),2)
                    player3.seat = int(match.group(1)) 
                elif int(match.group(1)) == 4:
                    player4.name = match.group(2)
                    player4.stack = round(float(floats[-1]),2)
                    player4.seat = int(match.group(1)) 
                elif int(match.group(1)) == 5:
                    player5.name = match.group(2)
                    player5.stack = round(float(floats[-1]),2)
                    player5.seat = int(match.group(1)) 
                elif int(match.group(1)) == 6:
                    player6.name = match.group(2)
                    player6.stack = round(float(floats[-1]),2)
                    player6.seat = int(match.group(1)) 
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
                    player1.stack -= round(float(floats[-1]),2)
                    thetable.pot += round(float(floats[-1]),2)
                if player2.name in line:
                    player2.bet = round(float(floats[-1]),2)
                    player2.stack -= round(float(floats[-1]),2)
                    thetable.pot += round(float(floats[-1]),2)
                if player3.name in line:
                    player3.bet = round(float(floats[-1]),2)
                    player3.stack -= round(float(floats[-1]),2)
                    thetable.pot += round(float(floats[-1]),2)
                if player4.name in line:
                    player4.bet = round(float(floats[-1]),2)
                    player4.stack -= round(float(floats[-1]),2)
                    thetable.pot += round(float(floats[-1]),2)
                if player5.name in line:
                    player5.bet = round(float(floats[-1]),2)
                    player5.stack -= round(float(floats[-1]),2)
                    thetable.pot += round(float(floats[-1]),2)
                if player6.name in line:
                    player6.bet = round(float(floats[-1]),2)
                    player6.stack -= round(float(floats[-1]),2)
                    thetable.pot += round(float(floats[-1]),2)
                if player7.name in line:
                    player7.bet = round(float(floats[-1]),2)
                    player7.stack -= round(float(floats[-1]),2)
                    thetable.pot += round(float(floats[-1]),2)
                if player8.name in line:
                    player8.bet = round(float(floats[-1]),2)
                    player8.stack -= round(float(floats[-1]),2)
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

    if not bFileIsOpen:
        open_f()

    print("back")
    button_play.config(image = img_play)
    button_pause.config(image = img_pause)

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

    if not bFileIsOpen:
        open_f()

    print("forward")
    button_play.config(image = img_play)
    button_pause.config(image = img_pause)

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

    if not bFileIsOpen:
        open_f()

    step_pointer = 0
    Pot = 0.0
    print("next")
    button_play.config(image = img_play)
    button_pause.config(image = img_pause)
    if bFileIsOpen and not bFileFinished and hand_pointer < number_of_hands:
        for l in storage[hand_pointer]:
            #print(l)
            inside_summary = False
           #print(l)
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
                extract_info(l)
            # If the flag is False, print the l
            elif not inside_summary:
                #print(l)
                extract_info(l)
        print_players_starting_info()

        hand_pointer += 1    
    if hand_pointer == number_of_hands:
        bFileFinished = True
        print("Last Hand")
    

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

    if not bFileIsOpen:
        open_f()

    step_pointer = 0
    Pot = 0.0

    print("previous")
    button_play.config(image = img_play)
    button_pause.config(image = img_pause)

    if bFileIsOpen and not bFileFinished and hand_pointer > 0:
        for l in storage[hand_pointer]:
            inside_summary = False
           #print(l)
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
                extract_info(l)
            # If the flag is False, print the l
            elif not inside_summary:
                extract_info(l)
        print_players_starting_info()
        hand_pointer -= 1
    if hand_pointer == 0:
        #bFileFinished = True
        print("First Hand")

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

#label_player1 = Label(height=1, width=6, text="Player1", bg='black', fg='lightblue',font=('Times New Roman', 15, 'bold'))
#label_player1.place(x=430, y=450)

label_player1 = Label(height=1, width=6, text=player1.name, bg='black', fg='lightblue',font=('Times New Roman', 15, 'bold'))
label_player1.place(x=player1.namex, y=player1.namey)

label_player1_stack = Label(height=1, width=6, text="100", bg='black', fg='lightgreen',font=('Times New Roman', 15, 'bold'))
label_player1_stack.place(x=player1.stackx, y=player1.stacky)

button_p1_db = Button(image = img_db, bg='cornflowerblue')
button_p1_db.place(x=player1.buttonx, y=player1.buttony)

button_p1c1 = Button(image = img_card_As)
button_p1c1.place(x=player1.card1x, y=player1.card1y)

button_p1c2 = Button(image = img_card_Kh)
button_p1c2.place(x=player1.card2x, y=player1.card2y)

button_bet1 = Button(text="", bg='cornflowerblue', fg='yellow',font=('Times New Roman', 15, 'bold'))
button_bet1.place(x=player1.betx, y=player1.bety)

label_player2 = Label(height=1, width=6, text="Player2", bg='black', fg='lightblue',font=('Times New Roman', 15, 'bold'))
label_player2.place(x=player2.namex, y=player2.namey)

label_player2_stack = Label(height=1, width=6, text="100", bg='black', fg='lightgreen',font=('Times New Roman', 15, 'bold'))
label_player2_stack.place(x=player2.stackx, y=player2.stacky)

button_p2_db = Button(image = img_db, bg='cornflowerblue')
button_p2_db.place(x=player2.buttonx, y=player2.buttony)

button_p2c1 = Button(image = img_card_Qd)
button_p2c1.place(x=player2.card1x, y=player2.card1y)

button_p2c2 = Button(image = img_card_Qc)
button_p2c2.place(x=player2.card2x, y=player2.card2y)

button_bet2 = Button(text="", bg='cornflowerblue', fg='yellow',font=('Times New Roman', 15, 'bold'))
button_bet2.place(x=player2.betx, y=player2.bety)

label_player3 = Label(height=1, width=6, text="Player3", bg='black', fg='lightblue',font=('Times New Roman', 15, 'bold'))
label_player3.place(x=player3.namex, y=player3.namey)

label_player3_stack = Label(height=1, width=6, text="100", bg='black', fg='lightgreen',font=('Times New Roman', 15, 'bold'))
label_player3_stack.place(x=player3.stackx, y=player3.stacky)

button_p3_db = Button(image = img_db, bg='cornflowerblue')
button_p3_db.place(x=player3.buttonx, y=player3.buttony)

button_p3c1 = Button(image = img_card_2s)
button_p3c1.place(x=player3.card1x, y=player3.card1y)

button_p3c2 = Button(image = img_card_7s)
button_p3c2.place(x=player3.card2x, y=player3.card2y)

button_bet3 = Button(text="", bg='cornflowerblue', fg='yellow',font=('Times New Roman', 15, 'bold'))
button_bet3.place(x=player3.betx, y=player3.bety)

label_player4 = Label(height=1, width=6, text="Player4", bg='black', fg='lightblue',font=('Times New Roman', 15, 'bold'))
label_player4.place(x=player4.namex, y=player4.namey)

label_player4_stack = Label(height=1, width=6, text="100", bg='black', fg='lightgreen',font=('Times New Roman', 15, 'bold'))
label_player4_stack.place(x=player4.stackx, y=player4.stacky)

button_bet4 = Button(text="", bg='cornflowerblue', fg='yellow',font=('Times New Roman', 15, 'bold'))
button_bet4.place(x=player4.betx, y=player4.bety)

button_p4_db = Button(image = img_db, bg='cornflowerblue')
button_p4_db.place(x=player4.buttonx, y=player4.buttony)

button_p4c1 = Button(image = img_card_Jh)
button_p4c1.place(x=player4.card1x, y=player4.card1y)

button_p4c2 = Button(image = img_card_Jd)
button_p4c2.place(x=player4.card2x, y=player4.card2y)

label_player5 = Label(height=1, width=6, text="Player5", bg='black', fg='lightblue',font=('Times New Roman', 15, 'bold'))
label_player5.place(x=player5.namex, y=player5.namey)

button_bet5 = Button(text="", bg='cornflowerblue', fg='yellow',font=('Times New Roman', 15, 'bold'))
button_bet5.place(x=player5.betx, y=player5.bety)

label_player5_stack = Label(height=1, width=6, text="100", bg='black', fg='lightgreen',font=('Times New Roman', 15, 'bold'))
label_player5_stack.place(x=player5.stackx, y=player5.stacky)

button_p5_db = Button(image = img_db, bg='cornflowerblue')
button_p5_db.place(x=player5.buttonx, y=player5.buttony)

button_p5c1 = Button(image = img_card_back_fo)
button_p5c1.place(x=player5.card1x, y=player5.card1y)

button_p5c2 = Button(image = img_card_back_ld)
button_p5c2.place(x=player5.card2x, y=player5.card2y)

label_player6 = Label(height=1, width=6, text="Player6", bg='black', fg='lightblue',font=('Times New Roman', 15, 'bold'))
label_player6.place(x=player6.namex, y=player6.namey)

label_player6_stack = Label(height=1, width=6, text="100", bg='black', fg='lightgreen',font=('Times New Roman', 15, 'bold'))
label_player6_stack.place(x=player6.stackx, y=player6.stacky)

button_p6c1 = Button(image = img_card_back)
button_p6c1.place(x=player6.card1x, y=player6.card1y)

button_p6_db = Button(image = img_db, bg='cornflowerblue')
button_p6_db.place(x=player6.buttonx, y=player6.buttony)

button_p6c2 = Button(image = img_card_back)
button_p6c2.place(x=player6.card2x, y=player6.card2y)

button_bet6 = Button(text="", bg='cornflowerblue', fg='yellow',font=('Times New Roman', 15, 'bold'))
button_bet6.place(x=player6.betx, y=player6.bety)

label_player7 = Label(height=1, width=6, text="Player7", bg='black', fg='lightblue',font=('Times New Roman', 15, 'bold'))
label_player7.place(x=player7.namex, y=player7.namey)

label_player7_stack = Label(height=1, width=6, text="100", bg='black', fg='lightgreen',font=('Times New Roman', 15, 'bold'))
label_player7_stack.place(x=player7.stackx, y=player7.stacky)

button_p7_db = Button(image = img_db, bg='cornflowerblue')
button_p7_db.place(x=player7.buttonx, y=player7.buttony)

button_p7c1 = Button(image = img_card_nocard, bg='cornflowerblue')
button_p7c1.place(x=player7.card1x, y=player7.card1y)

button_p7c2 = Button(image = img_card_nocard, bg='cornflowerblue')
button_p7c2.place(x=player7.card2x, y=player7.card2y)

button_bet7 = Button(text="", bg='cornflowerblue', fg='yellow',font=('Times New Roman', 15, 'bold'))
button_bet7.place(x=player7.betx, y=player7.bety)

label_player8 = Label(height=1, width=6, text="Player8", bg='black', fg='lightblue',font=('Times New Roman', 15, 'bold'))
label_player8.place(x=player8.namex, y=player8.namey)

label_player8_stack = Label(height=1, width=6, text="100", bg='black', fg='lightgreen',font=('Times New Roman', 15, 'bold'))
label_player8_stack.place(x=player8.stackx, y=player8.stacky)

button_p8_db = Button(image = img_db, bg='cornflowerblue')
button_p8_db.place(x=player8.buttonx, y=player8.buttony)

button_p8c1 = Button(image = img_card_nocard, bg='cornflowerblue')
button_p8c1.place(x=player8.card1x, y=player8.card1y)

button_p8c2 = Button(image = img_card_nocard, bg='cornflowerblue')
button_p8c2.place(x=player8.card2x, y=player8.card2y)

button_bet8 = Button(text="", bg='cornflowerblue', fg='yellow',font=('Times New Roman', 15, 'bold'))
button_bet8.place(x=player8.betx, y=player8.bety)

# Board Cards
button_f1 = Button(image = img_card_4h)
button_f1.place(x=thetable.flop1x, y=thetable.flop1y)

button_f2 = Button(image = img_card_5h)
button_f2.place(x=thetable.flop2x, y=thetable.flop2y)

button_f3 = Button(image = img_card_7s)
button_f3.place(x=thetable.flop3x, y=thetable.flop3y)

button_t1 = Button(image = img_card_back)
button_t1.place(x=thetable.turn1x, y=thetable.turn1y)

button_r1 = Button(image = img_card_back)
button_r1.place(x=thetable.river1x, y=thetable.river1y)

button_pot = Button(text="2.87", bg='green', fg='yellow',font=('Times New Roman', 15, 'bold'))
button_pot.place(x=thetable.potx, y=thetable.poty)


label_title = Label(text=thetable.title, bg='black', fg='red',font=('Times New Roman', 13, 'bold'))
label_title.place(x=125,y= 10)

button_previous = Button(image = img_previous, command = previous)
button_previous.place(x=340, y=500)

button_back = Button(image = img_back, command = back)
button_back.place(x=390, y=500)

button_play = Button(image = img_play, command = play)
button_play.place(x=440, y=500)

button_pause = Button(image = img_pause, command = pause)
button_pause.place(x=490, y=500)

button_forward = Button(image = img_forward, command = forward)
button_forward.place(x=540, y=500)

button_next = Button(image = img_next, command = next)
button_next.place(x=590, y=500)

button_open = Button(image = img_open, command = open_f)
button_open.place(x=60, y=10)
#button_open.place(x=560, y=10)

button_settings = Button(image = img_settings, command = settings)
button_settings.place(x=10, y=10)
#button_settings.place(x=510, y=10)

ws.mainloop()