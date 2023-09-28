import random

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
                    if main.current_state()[value] >= 0:
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


ROWS, COLS = 6, 7

player = HumanPlayer('X')

