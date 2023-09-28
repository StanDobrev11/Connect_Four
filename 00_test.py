# lst = [None, 5, -7, 0]
#
# print(all(map(lambda x: x >= 0, lst)))
#

def make_board():
    return [['.'] * COLS for _ in range(ROWS)]


def current_state(self):
    state = [None] * COLS
    for row in range(ROWS - 1, -1, -1):
        if all(map(lambda x: x is not None, state)):
            break
        for col in range(COLS):
            if self.board[row][col] == '.' and state[col] is None:
                state[col] = row

    return state


def _valid(col):
    if col - 1 not in range(COLS):
        return False
    if board[0][col - 1] != '.':
        return False
    return True


def empty_space():
    count = 0
    for row in board:
        count += row.count('.')
    return count


def available_moves():
    for col in range(COLS):
        for row in range(ROWS - 1, -1, -1):
            if board[row][col] == '.':
                yield row, col
                break



ROWS, COLS = 6, 7
board = make_board()

# valid_col = False
# value = None
# while not valid_col:
#     column = input(f'Current player {"X"} -> choose column: ')
#     try:
#         value = int(column) - 1
#         if _valid(value + 1):
#             # if current_state()[value] >= 0:
#             valid_col = True
#         raise ValueError
#     except ValueError:
#         print('Please make a valid choice')
# print(value)


# print(available_moves())
print(list(available_moves()))
