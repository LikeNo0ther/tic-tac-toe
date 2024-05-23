from random import choice

game_board_size = int(input('укажите размер стороны игровой доски:'))
board = list(range(1, game_board_size**2 + 1))
possible_moves = board.copy()
players = ('player', 'computer')


def draw_game_board(game_board_size: int) -> None:
    print(' ---' * game_board_size)
    for j in range(game_board_size):
        for i in range(game_board_size):
            current_coordinate = j * game_board_size + i
            if board[current_coordinate] in ('X', 'O'):
                print('|  ', end='')
            elif board[current_coordinate] < 10:
                print('|  ', end='')
            elif board[current_coordinate] < 100:
                print('| ', end='')
            elif board[current_coordinate] < 1000:
                print('|', end='')
            print(board[current_coordinate], end='')
        print('|')
    print(' ---' * game_board_size)


def check_win(move=int, win_size=int) -> bool:
    # определяем индексы столбца и строки хода
    if move % game_board_size != 0:
        col_ind = move % game_board_size - 1
        row_ind = move // game_board_size
    else:
        col_ind = game_board_size - 1
        row_ind = move // game_board_size - 1
    print(f'индекс столбца хода: {col_ind}')
    print(f'индекс строки хода: {row_ind}')

    # определяем левый индекс квадрата проверки выигрыша
    if (col_ind - win_size + 1) <= 0:
        left_ind = 0 + game_board_size * row_ind
        print(f'левая граница квадрата проверки: {left_ind}')
    else:
        left_ind = col_ind - win_size + game_board_size * row_ind + 1
        print(f'левая граница квадрата проверки: {left_ind}')

    # определяем правый индекс квадрата проверки выигрыша
    if (game_board_size - (col_ind + win_size - 1)) <= 0:
        right_ind = game_board_size + game_board_size * row_ind - 1
        print(f'правая граница квадрата проверки: {right_ind}')
    else:
        right_ind = col_ind + win_size + game_board_size * row_ind - 1
        print(f'правая граница квадрата проверки: {right_ind}')

    # определяем верхний индекс квадрата проверки выигрыша
    if (row_ind - win_size + 1) <= 0:
        top_ind = move - 1 - game_board_size * row_ind
        print(f'верхняя граница квадрата проверки: {top_ind}')
    else:
        top_ind = move - 1 - game_board_size * (win_size - 1)
        print(f'верхняя граница квадрата проверки: {top_ind}')

    # определяем нижний индекс квадрата проверки выигрыша
    if (game_board_size - (row_ind + win_size - 1)) <= 0:
        down_ind = move - 1 + game_board_size * (game_board_size - row_ind - 1)
        print(f'нижняя граница квадрата проверки: {down_ind}')
    else:
        down_ind = move - 1 + game_board_size * (win_size - 1)
        print(f'нижняя граница квадрата проверки: {down_ind}')

    # проверка выигрыша по горизантали
    counter = 1
    for i in range(left_ind + 1, right_ind + 1):
        if board[i] == board[i - 1]:
            counter += 1
    if counter >= win_size:
        return True

    # проверка выигрыша по вертикали
    counter = 1
    for i in range(top_ind + game_board_size, down_ind + 1, game_board_size):
        if board[i] == board[i-game_board_size]:
            counter += 1
    if counter >= win_size:
        return True

    # 1-я проверка по диагонали
    for_start = min(right_ind + 1 - move, (move - 1 - top_ind)//game_board_size)
    start = move - (game_board_size - 1) * (for_start) - 1
    print(f'старт {start}')

    for_end = min(move-left_ind, (1 + (down_ind + 1 - move)//game_board_size))
    end = move + (game_board_size - 1) * (for_end - 1) - 1
    print(f'финиш {end}')

    counter = 1
    for i in range(start + game_board_size - 1, end + 1, game_board_size - 1):
        if board[i - game_board_size + 1] == board[i]:
            counter += 1
    if counter >= win_size:
        return True

    # 2-я проверка по диагонали
    for_start = min(right_ind - move + 1, (1 + (down_ind + 1 - move)//game_board_size))

    start = move + (game_board_size + 1) * (for_start - 1)

    pass


draw_game_board(game_board_size)
check_win(44, 3)


def main():
    return
    computer_move = choice(possible_moves)
    first_step = choice(players)
    draw_game_board(game_board_size)
    print('Первым ходит:', first_step)
    if first_step == 'computer':
        computer_move = choice(possible_moves)
        possible_moves.remove(computer_move)
        board[computer_move-1] = 'X'
        print(possible_moves)
        draw_game_board(5)
    else:
        player_move = int(input('Введите координату:'))
        possible_moves.remove(player_move)
        board[player_move-1] = 'X'
        print(possible_moves)
        draw_game_board(5)


main()


if __name__ == '__main__':
    pass
