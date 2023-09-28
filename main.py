import operator

from players import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer


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

    def available_moves(self):
        for col in range(COLS):
            for row in range(ROWS - 1, -1, -1):
                if self.board[row][col] == '.':
                    yield row, col
                    break

    def any_empty_space(self):
        return "." in self.board[0]

    def num_empty_spaces(self):
        count = 0
        for row in self.board:
            count += row.count('.')
        return count

    @staticmethod
    def validation(row, col):
        if row in range(ROWS) and col in range(COLS):
            return True
        return False

    def get_count(self, letter, row, col, dx, dy, operator_func):
        current_count = 0
        for i in range(1, 4):
            next_row = operator_func(row, dx * i)
            next_col = operator_func(col, dy * i)
            if not self.validation(next_row, next_col):
                break
            if self.board[next_row][next_col] == letter:
                current_count += 1
            else:
                break
        return current_count

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
            count = (
                    self.get_count(letter, player_row, player_col, x, y, operator.add)
                    + self.get_count(letter, player_row, player_col, x, y, operator.sub) + 1
            )
            if count >= 4:
                return True
        return False


def play(main, x_player, o_player, print_game=True):
    if print_game:
        main.print_board()

    letter = 'X'
    while main.any_empty_space():
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
                raise SystemExit
                # return letter

        letter = 'O' if letter == 'X' else 'X'
    if main.num_empty_spaces() == 0:
        print('DRAW')


ROWS, COLS = 4, 6

if __name__ == '__main__':
    x_pl = HumanPlayer('X')
    o_pl = HumanPlayer('O')
    t = ConnectFour()
    play(t, x_pl, o_pl, print_game=True)
