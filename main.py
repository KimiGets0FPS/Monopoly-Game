from player import Player
import random
import time

player = Player()


mapped = {}
with open('map.json', 'r') as file:
    for i in range(39):
        mapped[i] = file.readline().split('\n')
print(mapped)

player_info = {}


def main(info: dict, round_num=15, players=4) -> None:
    if players <= 1:
        print('You have to have more than 1 player!')
        return
    for rounds in range(round_num):
        time.sleep(0.5)
        print(f'\nRound {rounds+1}')
        for players in range(players):
            time.sleep(0.5)
            if info[players][0] <= 10 or info[players][2]:
                info[players][2] = True
                print(f"- - - - -\n{players+1} is bankrupted, skipped...\n- - - - - -")
                time.sleep(2)
            else:
                print(f"Player {players+1}'s turn")
                dice_roll = random.randint(0, 6)
                print(f"\nPlayer {players+1}'s rolled {dice_roll}")


if __name__ == '__main__':
    while True:
        times = input('Number of rounds: ')
        num_player = input('Number of players: ')
        for i in range(int(num_player)):
            player_info[i] = [1500, True, False]  # Money; Previous Roll; Bankrupt;
        main(player_info, int(times), int(num_player))
        if input('Do you want to go again (Yes or No): ').lower() == 'no':
            break
    print('Thanks for playing!')
