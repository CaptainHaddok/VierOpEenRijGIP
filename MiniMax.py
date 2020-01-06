import Bord
import math


def minimax(depth, nodeIndex, maximizingPlayer,values, alpha, beta,Difficulty):
    # Terminating condition. i.e
    # leaf node is reached
    if depth == Difficulty:
        return values[nodeIndex]
    if maximizingPlayer:
        best = -10000000
        # Recur for left and right children
        for i in range(0, 7):
            val = minimax(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            # Alpha Beta Pruning
            if beta <= alpha:
                break
        return best
    else:
        best = 10000000
        # Recur for left and
        # right children
        for i in range(0, 7):
            val = minimax(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            # Alpha Beta Pruning
            if beta <= alpha:
                break
        return best

def CalcValues(Bord, Difficulty,Player):
    values = {}
    for i in range(int(math.pow(7,Difficulty))):
        b = Bord
        for j in range(Difficulty-1):
            b.PutIn(int(i % math.pow(7,j+1)),Player)
        values[i] = b.winrate
        if i % 7 == 3: values[i] += 1
    return values

    #TODO: Winrates geven
def CalcBord(Bord, Difficulty,Player):
    #TODO: Winrates wete wel
    return minimax(0, 0, True, CalcValues(Bord, Difficulty,Player), -10000000, 10000000, Difficulty)