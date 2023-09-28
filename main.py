from players import HumanPlayer, RandomComputerPlayer


class ConnectFour:

    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None

    def make_board(self):
        return [['.'] * COLS for _ in range(ROWS)]

    def print_board(self):
        for row in self.board:
            print(' '.join(map(str, row)))
        print(' '.join(map(str, range(1, COLS + 1))))

    def is_valid(self, col):
        if col - 1 not in range(COLS):
            return False
        if self.board[0][col - 1] != '.':
            return False
        return True

    def empty_squares(self):
        return True if all(map(lambda x: x >= 0, self.current_state())) else False

    def current_state(self):
        state = [None] * COLS
        for row in range(ROWS - 1, -1, -1):
            if all(map(lambda x: x is not None, state)):
                break
            for col in range(COLS):
                if self.board[row][col] == '.' and state[col] is None:
                    state[col] = row

        return state

    def validation(self, row, col, letter):
        if row in range(ROWS) and col in range(COLS):
            return True

        return False

    def make_move(self, letter, player_col):
        for row in range(ROWS - 1, -1, -1):
            if not self.board[row][player_col] == '.':
                continue

            self.board[row][player_col] = letter
            if self.winner(letter, row, player_col):
                self.current_winner = letter
            return True
        return False

    def winner(self, letter, player_row, player_col):
        directions = {
            (1, 0),  # down
            (0, 1),  # right
            (-1, 1),  # top right
            (1, 1),  # bottom right
        }
        for x, y in directions:
            count = 1
            for i in range(1, 4):
                next_row = player_row + x * i
                next_col = player_col + y * i
                if not self.validation(next_row, next_col, letter):
                    break
                if self.board[next_row][next_col] == letter:
                    count += 1
            for i in range(1, 4):
                next_row = player_row - x * i
                next_col = player_col - y * i
                if not self.validation(next_row, next_col, letter):
                    break
                if self.board[next_row][next_col] == letter:
                    count += 1

            if count >= 4:
                return True
        return False


def play(main, x_player, o_player, print_game=True):
    if print_game:
        main.print_board()

    letter = 'X'
    while main.empty_squares():
        if letter == 'O':
            column = o_player.get_move(main)
        else:
            column = x_player.get_move(main)
        if main.make_move(letter, column):
            if print_game:
                print(f'Player {letter} hs chosen column {column + 1}')
                main.print_board()
                print('')
            if main.current_winner:
                print(f'Player {letter} hs WON')
                return letter

        letter = 'O' if letter == 'X' else 'X'


ROWS, COLS = 6, 7

if __name__ == '__main__':
    x_pl = HumanPlayer('X')
    o_pl = RandomComputerPlayer('O')
    t = ConnectFour()
    play(t, x_pl, o_pl, print_game=True)
