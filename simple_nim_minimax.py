def minimax(state, max_turn):
    if state == 0:
        return 1 if max_turn else -1

    possible_new_states = [
        state - take for take in [1, 2, 3] if take <= state
    ]

    if max_turn:
        scores = [
            minimax(new_state, max_turn=False) for new_state in possible_new_states
        ]
        return max(scores)
    else:
        scores = [
            minimax(new_state, max_turn=True) for new_state in possible_new_states
        ]
        return min(scores)




def best_move(state):
    for take in (1, 2, 3):
        new_state = state - take
        score = minimax(new_state, max_turn=False)
        print(f"Move from {state} to {new_state}: {score}")
        if score > 0:
            break
    return score, new_state


# print(minimax(6, True))
# print(minimax(6, False))

print(best_move(5))


#
# turns = deque(['max', 'mini'])
# deck = 6
#
# current_player = turns[0]
#
# turns.rotate(-1)
