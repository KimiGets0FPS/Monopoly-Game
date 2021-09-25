from player import Player
import random
import time

player = Player()


with open('map.csv', 'r') as file:
    board = file.readline().split(', ')
print(board)


def main(round_num: int, players: int) -> None:
    round_num, players = int(round_num), int(players)
    if players <= 1:
        print('You have to have more than 1 player!')
        return
    for rounds in range(round_num):
        time.sleep(0.5)
        print(f'\nRound {rounds + 1}')
        for players in range(players):
            if player.bankrupted():
                break
            print(f"Player {players+1}'s turn")
            dice_roll = random.randint(0, 6)
            print(f"\nPlayer {players+1}'s rolled {dice_roll}")
            time.sleep(0.5)


if __name__ == '__main__':
    while True:
        times = input('Number of rounds: ')
        num_player = input('Number of players: ')
        if not times:
            times = 15
        if not num_player:
            num_player = 4
        main(times, num_player)
        if input('Do you want to go again (Yes or No): ').lower() == 'no':
            break
    print('Thanks for playing!')
