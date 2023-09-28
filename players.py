import random
from functools import cache


class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, main):
        while True:
            column = input(f'Current player {self.letter} -> choose column: ')
            try:
                value = int(column) - 1
                if main.is_valid(value + 1):
                    break
                raise ValueError
            except ValueError:
                print('Please make a valid choice')
        return value


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, main):
        column = random.choice(range(COLS))
        return column


class SmartComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, main):
        if main.num_empty_spaces() > ROWS * COLS - 5:
            column = random.choice(range(COLS))
        else:
            column = self.minimax(main, self.letter)['position'][1]
        return column

    @cache
    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        # check if previous move is winning
        if state.current_winner == other_player:
            return {
                'position': None,
                'score': 1 * (state.num_empty_spaces() + 1)
                if other_player == max_player
                else -1 * (state.num_empty_spaces() + 1)
            }
        elif not state.any_empty_space():
            return {'position': None, 'score': 0}
        # TODO evaluation is not correct for the game in question
        # evaluation
        if player == max_player:
            best = {'position': None, 'score': -float('inf')}
        else:
            best = {'position': None, 'score': float('inf')}
        # TODO not working properly. Should check on each possible move for the original board state to maximize the
        #  count of the symbols and to minimize opponent's count if is getting to a win.
        # possible moves
        for possible_move in state.available_moves():
            row, col = possible_move
            state.make_move(player, col)
            simulated_score = self.minimax(state, other_player)  # simulate game after making move

            # undo the move
            state.board[row][col] = '.'
            state.current_winner = None
            simulated_score['position'] = possible_move

            if player == max_player:  # X is max player
                if simulated_score['score'] > best['score']:
                    best = simulated_score
            else:
                if simulated_score['score'] < best['score']:
                    best = simulated_score
        return best


ROWS, COLS = 4, 6
