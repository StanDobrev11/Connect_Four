def minimax(state, is_maximizing):
    if (score := evaluate(state, is_maximizing)) is not None:
        return score

    return (max if is_maximizing else min)(
        minimax(new_state, is_maximizing=not is_maximizing) for new_state in possible_new_states(state)
    )


def best_move(state):
    return max(
        (minimax(new_state, is_maximizing=False), new_state)
        for new_state in possible_new_states(state)
    )


def possible_new_states(state):
    return [state - take for take in (1, 2, 3) if take <= state]


def evaluate(state, is_maximizing):
    """
    Evaluates end state of the game and returns appropriate win/loose value
    :param state: int
    :param is_maximizing: bool value representing player's turn
    :return: end value, +1 for winning, -1 for loosing
    """
    if state == 3:
        return 1 if is_maximizing else -1


