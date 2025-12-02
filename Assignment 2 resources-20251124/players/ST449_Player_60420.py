"""
ST449 Chopsticks - Improved bot with minimax lookahead
Replace 60420 with your candidate number
"""

def is_legal(tapping_hand, tapped_hand, state):
    if tapping_hand == tapped_hand: return False
    if state[tapping_hand] == 0: return False
    if state[tapped_hand] == 0 and not {tapping_hand, tapped_hand} == {'A', 'B'}: return False
    if state[tapped_hand] == 0 and state[tapping_hand] < 4: return False
    return True

def get_legal_moves(state, player):
    if player == 1:
        hands = ['A', 'B']
    else:
        hands = ['C', 'D']
    targets = ['A', 'B', 'C', 'D']
    
    moves = []
    for tapping in hands:
        for tapped in targets:
            if is_legal(tapping, tapped, state):
                moves.append(tapping + tapped)
    return moves

def apply_move(state, move):
    s = state.copy()
    tapping, tapped = move[0], move[1]
    x, y = s[tapping], s[tapped]
    
    # Split
    if tapped in ['A', 'B'] and tapping in ['A', 'B'] and y == 0:
        s[tapping] = (x + 1) // 2
        s[tapped] = x // 2
    elif tapped in ['C', 'D'] and tapping in ['C', 'D'] and y == 0:
        s[tapping] = (x + 1) // 2
        s[tapped] = x // 2
    # Tap
    else:
        if x + y > 5:
            s[tapped] = 0
        else:
            s[tapped] = x + y
    return s

def evaluate(state):
    if state['C'] == 0 and state['D'] == 0:
        return 1000
    if state['A'] == 0 and state['B'] == 0:
        return -1000
    
    score = 0
    if state['C'] == 0: score += 50
    if state['D'] == 0: score += 50
    if state['A'] == 0: score -= 30
    if state['B'] == 0: score -= 30
    score += state['C'] + state['D']
    score -= (state['A'] + state['B']) * 0.5
    return score

def minimax(state, depth, is_maximizing, alpha, beta):
    if state['C'] == 0 and state['D'] == 0:
        return 1000
    if state['A'] == 0 and state['B'] == 0:
        return -1000
    if depth == 0:
        return evaluate(state)
    
    if is_maximizing:
        max_eval = -9999
        moves = get_legal_moves(state, 1)
        if not moves:
            return evaluate(state)
        for move in moves:
            new_state = apply_move(state, move)
            eval_score = minimax(new_state, depth - 1, False, alpha, beta)
            max_eval = max(max_eval, eval_score)
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = 9999
        moves = get_legal_moves(state, 2)
        if not moves:
            return evaluate(state)
        for move in moves:
            new_state = apply_move(state, move)
            eval_score = minimax(new_state, depth - 1, True, alpha, beta)
            min_eval = min(min_eval, eval_score)
            beta = min(beta, eval_score)
            if beta <= alpha:
                break
        return min_eval

def generate_move(state_str):
    state = {'A': int(state_str[1]), 'B': int(state_str[3]), 
             'C': int(state_str[5]), 'D': int(state_str[7])}
    
    moves = get_legal_moves(state, 1)
    if not moves:
        return 'AC'
    
    best_move = None
    best_score = -9999
    
    for move in moves:
        new_state = apply_move(state, move)
        score = minimax(new_state, 3, False, -9999, 9999)
        if score > best_score:
            best_score = score
            best_move = move
    
    return best_move