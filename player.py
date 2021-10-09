class Player:
    def __init__(self, money=1500):
        self.money = money
        self.bankrupt = False

    def double_roll(self, current, previous):
        if previous == current:
            return True
        return False

    def test(self, subtracted):
        self.money -= subtracted
        return


if __name__ == '__main__':
    player = Player()
