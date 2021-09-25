class Player:
    def __init__(self):
        self.money = 1500
        self.bankrupt = False

    def bankrupted(self):
        if (self.money <= 10 and self.bankrupt is False) or self.bankrupt is True:
            self.bankrupt = True
            return True
        return False

    def double_roll(self, current, previous):
        if previous == current:
            return True
        return False

    def test(self, subtracted):
        self.money -= subtracted
        return


if __name__ == '__main__':
    player = Player()
    print(player.bankrupted())
    player.test(1990)
    print(player.bankrupted())
