from random import choice


def draw_board_line(rownum: int) -> str:
    line = []
    for i in range(game_board_size):
        current_coordinate = rownum * game_board_size + i
        if board[current_coordinate] in ('X', 'O'):
            line.append("|  ")
        elif board[current_coordinate] < 10:
            line.append("|  ")
        elif board[current_coordinate] < 100:
            line.append("| ")
        elif board[current_coordinate] < 1000:
            line.append("|")
        line.append(str(board[current_coordinate]))
    line.append("|")
    return "".join(line)


def draw_game_board(game_board_size: int) -> str:
    """
    Функция принимает на вход заданный размер доски и
    отрисовывает её текущее состояние с учетом сделанных ходов.
    """
    
    lines = []
    lines.append(" ---" * game_board_size)
    for rownum in range(game_board_size):
        lines.append(draw_board_line(rownum))
    lines.append(' ---' * game_board_size)
    return "\n".join(lines)


def check_win(move: int) -> bool:
    """
    Функция принимает на вход сделанный ход и
    проверяет, был ли он выигрышным.
    """

    # определяем индексы столбца и строки хода
    if move % game_board_size != 0:
        col_ind = move % game_board_size - 1
        row_ind = move // game_board_size
    else:
        col_ind = game_board_size - 1
        row_ind = move // game_board_size - 1

    # определяем левый индекс горизонтальной проверки выигрыша
    if (col_ind - win_size + 1) <= 0:
        left_ind = 0 + game_board_size * row_ind
    else:
        left_ind = col_ind - win_size + game_board_size * row_ind + 1

    # определяем правый индекс горизонтальной проверки выигрыша
    if (game_board_size - (col_ind + win_size - 1)) <= 0:
        right_ind = game_board_size + game_board_size * row_ind - 1
    else:
        right_ind = col_ind + win_size + game_board_size * row_ind - 1

    # проверка выигрыша по горизантали
    counter = 1
    for i in range(left_ind + 1, right_ind + 1):
        if board[i] == board[i - 1]:
            counter += 1
    if counter >= win_size:
        return True

    # определяем верхний индекс вертикальной проверки выигрыша
    if (row_ind - win_size + 1) <= 0:
        top_ind = move - 1 - game_board_size * row_ind
    else:
        top_ind = move - 1 - game_board_size * (win_size - 1)

    # определяем нижний индекс вертикальной проверки выигрыша
    if (game_board_size - (row_ind + win_size - 1)) <= 0:
        down_ind = move - 1 + game_board_size * (game_board_size - row_ind - 1)
    else:
        down_ind = move - 1 + game_board_size * (win_size - 1)

    # проверка выигрыша по вертикали
    counter = 1
    for i in range(top_ind + game_board_size, down_ind + 1, game_board_size):
        if board[i] == board[i-game_board_size]:
            counter += 1
    if counter >= win_size:
        return True

    # 1-я проверка по диагонали
    start_i = min(right_ind + 1 - move, (move - 1 - top_ind)//game_board_size)
    start = move - (game_board_size - 1) * start_i - 1

    end_i = min(move - 1 - left_ind, (down_ind + 1 - move)//game_board_size)
    end = move + (game_board_size - 1) * end_i - 1

    counter = 1
    for i in range(start + game_board_size - 1, end + 1, game_board_size - 1):
        if board[i - game_board_size + 1] == board[i]:
            counter += 1
    if counter >= win_size:
        return True

    # 2-я проверка по диагонали
    start_i = min(move - 1 - left_ind, (move - 1 - top_ind)//game_board_size)
    start = move - (game_board_size + 1) * start_i - 1

    end_i = min(right_ind + 1 - move, (down_ind + 1 - move)//game_board_size)
    end = move + (game_board_size + 1) * end_i - 1

    counter = 1
    for i in range(start + game_board_size + 1, end + 1, game_board_size + 1):
        if board[i - game_board_size - 1] == board[i]:
            counter += 1
    if counter >= win_size:
        return True
    return False


def main() -> None:
    game_over = False
    player_1 = True
    current_player_comp = choice(players)
    print('Первым ходит:', current_player_comp)
    while not game_over:
        print(draw_game_board(game_board_size))
        if player_1:
            mark = 'X'
            if current_player_comp:
                move = choice(possible_moves)
                possible_moves.remove(move)
                board[move-1] = mark
                print(f'Компьютер сходил: {move}')
                if len(possible_moves) == 0:
                    print('Ничья')
                    return
            else:
                move = int(input('Укажите доступную координату'))
                possible_moves.remove(move)
                board[move-1] = mark
                if len(possible_moves) == 0:
                    print('Ничья')
                    return
        else:
            mark = 'O'
            if current_player_comp:
                move = choice(possible_moves)
                possible_moves.remove(move)
                board[move-1] = mark
                print(f'Компьютер сходил: {move}')
                if len(possible_moves) == 0:
                    print('Ничья')
                    return
            else:
                move = int(input('Укажите доступную координату'))
                possible_moves.remove(move)
                board[move-1] = mark
                if len(possible_moves) == 0:
                    print('Ничья')
                    return
        player_1 = not(player_1)
        current_player_comp = not(current_player_comp)
        game_over = check_win(move)
    print(f'Конец игры: победили {mark}')
    print(draw_game_board(game_board_size))


if __name__ == '__main__':
    game_board_size = int(input('Укажите размер стороны игровой доски:'))
    win_size = int(input('Сколько совпадений нужно для победы?'))
    board = list(range(1, game_board_size**2 + 1))
    possible_moves = board.copy()
    players = (True, False)
    main()
