def make_game_board(game_board_size: int) -> None:
    print(' ---' * game_board_size)
    for j in range(game_board_size):
        for i in range(game_board_size):
            current_coordinate = j * game_board_size + i + 1
            if current_coordinate < 10:
                print('|  ', end='')
            elif current_coordinate < 100:
                print('| ', end='')
            elif current_coordinate < 1000:
                print('|', end='')
            print(current_coordinate, end='')
        print('|')
    print(' ---' * game_board_size)


def check_win():
    pass


def main():
    pass


make_game_board(3)


if __name__ == '__main__':
    pass
