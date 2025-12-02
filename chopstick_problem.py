"""
ST449 chopstick game
"""

def is_legal(tapping_hand, tapped_hand, state):
    if tapping_hand == tapped_hand: return False
    if state[tapping_hand] == 0: return False
    if state[tapped_hand] == 0 and not {tapping_hand, tapped_hand} == {'A', 'B'}: return False
    if state[tapped_hand] == 0 and state[tapping_hand] < 4: return False
    return True

def is_attacking(tapping_hand, tapped_hand, state):
    if state[tapping_hand] == 0: return False
    if tapped_hand not in ['C', 'D']: return False  
    return True

def generate_move(state_str):
    """Generate the best move for Player 1"""
    state = {'A': int(state_str[1]), 'B': int(state_str[3]), 'C': int(state_str[5]), 'D': int(state_str[7])}  # Fixed: was "if state ="
    possible_moves = ['AB', 'AC', 'AD', 'BA', 'BC', 'BD']
    h = {}
    
    for move in possible_moves:
        tapping_hand = move[0]
        tapped_hand = move[1]
        
        if is_legal(tapping_hand, tapped_hand, state):
            if is_attacking(tapping_hand, tapped_hand, state):  # Fixed: swapped order
                state_next = state.copy()
                state_next[tapped_hand] += state_next[tapping_hand]
                if state_next[tapped_hand] > 5:
                    state_next[tapped_hand] = 0
                # Fixed: missing h score calculation
                h[move] = (6 - state_next['C']) * (state_next['C'] != 0) + (6 - state_next['D']) * (state_next['D'] != 0)
            else:
                if state[tapped_hand] == 0 and state[tapping_hand] >= 4:  # Fixed: was tapped_hand
                    h[move] = 11
                else:
                    h[move] = 12
    
    best_move = min(h, key=h.get)
    return best_move