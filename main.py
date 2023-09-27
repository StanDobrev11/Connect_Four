from collections import deque


def print_(mtrx):
    for row in mtrx:
        print(' '.join(map(str, row)))
    print(' '.join(str(x) for x in range(1, len(mtrx[0]) + 1)))


def place_coin(mtrx, col, mark, row):  # TOP TO BOTTOM
    if row >= ROWS or mtrx[row][col] != '.':
        mtrx[row - 1][col] = mark
        return
    if mtrx[row][col] == '.':
        place_coin(mtrx, col, mark, row + 1)


def win(mtrx, col, row=0):
    def check_horizontals():
        horizontal_count = 1
        for c in range(col - 1, -1, -1):
            if c < 0 or mtrx[row][c] != mark:
                break
            horizontal_count += 1
        for c in range(col + 1, COLS):
            if c >= COLS or mtrx[row][c] != mark:
                break
            horizontal_count += 1
        return True if horizontal_count >= 4 else False

    def check_verticals():
        vertical_count = 1
        # for r in range(row - 1, -1, -1):
        #     if r < 0 or mtrx[r][col] != mark:
        #         break
        #     vertical_count += 1
        for r in range(row + 1, ROWS):
            if r >= ROWS or mtrx[r][col] != mark:
                break
            vertical_count += 1
        return True if vertical_count >= 4 else False

    def check_left_diagonal():  # row - col
        left_count = 1
        left_diag_key = row - col
        for r in range(row - 1, -1, -1):
            for c in range(col - 1, -1, -1):
                if r - c == left_diag_key:
                    if r < 0 or c < 0 or mtrx[r][c] != mark:
                        break
                    left_count += 1
        for r in range(row + 1, ROWS):
            for c in range(col + 1, COLS):
                if r - c == left_diag_key:
                    if r >= ROWS or c >= COLS or mtrx[r][c] != mark:
                        break
                    left_count += 1
        return True if left_count >= 4 else False

    def check_right_diagonal():
        right_count = 1
        right_diag_key = row + col
        for r in range(row - 1, -1, -1):
            for c in range(col + 1, COLS):
                if r + c == right_diag_key:
                    if r >= ROWS or c >= COLS or mtrx[r][c] != mark:
                        break
                    right_count += 1
        for r in range(row + 1, ROWS):
            for c in range(col - 1, -1, -1):
                if r + c == right_diag_key:
                    if r < 0 or c < 0 or mtrx[r][c] != mark:
                        break
                    right_count += 1
        return True if right_count >= 4 else False

    for row in range(ROWS):
        if mtrx[row][col] != '.':
            break
    mark = mtrx[row][col]
    if (check_horizontals() or
            check_verticals() or
            check_left_diagonal() or
            check_right_diagonal()):
        return True


def draw(mtrx):
    if '.' not in mtrx[0]:
        return True
    return False


def is_valid(col):
    if col - 1 not in range(COLS):
        return False
    if matrix[0][col - 1] != '.':
        return False
    return True


def players(count):
    players_marks_mapper = {
        2: ('X', 'O'),
        3: ('X', 'Y', 'Z'),
        4: ('X', 'Y', 'A', 'B')
    }
    turns = []
    for plr in range(1, count + 1):
        turns.append((plr, players_marks_mapper[count][plr - 1]))
    return turns


def possible_new_states(state):
    for col, row in enumerate(state):
        yield state[:col] + (row - 1,) + state[col + 1:]

def evaluate(state, is_maximizing):
    pass



def get_current_state(mtrx):
    cur_state = [None] * COLS
    for row in range(ROWS - 1, -1, -1):
        for col in range(COLS):
            if mtrx[row][col] == '.' and cur_state[col] is None:
                cur_state[col] = row
    return tuple(cur_state)


ROWS, COLS = 6, 7
matrix = [['.'] * COLS for _ in range(ROWS)]

while True:
    players_count = int(input("How many players (2-4): "))
    try:
        if players_count not in range(2, 5):
            raise ValueError
        else:
            break
    except ValueError:
        print("Not valid number")
player_turns = deque(players(players_count))

while True:
    print_(matrix)
    cur_player = player_turns[0][0]
    player_mark = player_turns[0][1]

    while True:
        column = int(input(f'Current player {cur_player} -({player_mark}) -> choose col: '))
        try:
            if not is_valid(column):
                print('Not valid column')
            else:
                break
        except ValueError:
            print('Please make a choice')

    column -= 1
    place_coin(matrix, column, player_mark, row=0)

    state = get_current_state(matrix)
    print(state)
    print(list(possible_new_states(state)))

    if win(matrix, column):
        print(f'Winner is Player {cur_player}')
        print_(matrix)
        break
    elif draw(matrix):
        print('No winner, game is DRAW')
        print_(matrix)
        break
    player_turns.rotate(-1)
    print()
