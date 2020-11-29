import random


def roll(count=0, doubles=0):
    if doubles == 3:
        return False
    roll_count = 0
    double_roll = False
    for _ in range(2):
        choice = random.choice([1, 2, 3, 4, 5, 6])
        if roll_count == choice:
            double_roll = True
        roll_count += choice
    if double_roll:
        again = roll(count + roll_count, doubles + 1)
        return again
    else:
        return count + roll_count


class Player:
    def __init__(self, board):
        self.board = board
        self.player_id = len(self.board.players)
        #* Getting Bankrupted
        self.bankrupt = False
        #* Getting jailed
        self.jail = False
        #* Money for each player
        self.money = 1500
        self.jail_chance_card = False
        self.status = 1
        self.board.add_player(self)
    
    def more_money(self, more):
        self.money += more
    
    def less_money(self, less):
        self.money -= less
        if self.money < 0:
            self.bankrupt = True
    
    def bankrupt_and_losing(self):
        self.money = 0
        self.status = 0
        
    
