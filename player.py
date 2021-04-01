import random as r


class Player:
    def __init(self):
        self.starting_money = 1500
        self.bankrupt = False
        self.triple_double = False

    def dice_roll(self):
        roll1 = r.randint(0, 6)
        roll2 = r.randint(0, 6)
        if roll1 == roll2:
            return "Double!"


