class Player:
    def __init__(self, name, bet, stack, seat, card1, card2, action):
        self.name = name
        self.bet = bet
        self.stack = stack
        self.seat = seat
        self.card1 = card1
        self.card2 = card2
        self.action = action

player1 = Player("Alice",21.2, 100.0, 4, "As", "Kh", "raise")