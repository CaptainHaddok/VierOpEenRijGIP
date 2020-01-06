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

def CalcValues(InpBord, Difficulty):
    values = {}
    for i in range(int(math.pow(7,Difficulty))):

        b = Bord.Bord("Test",InpBord.player1, InpBord.player2)
        for y in range(6):
            for x in range(7):
                b.rooster[y][x] = InpBord.rooster[y][x]

        for i in range(Difficulty):
            if i % 2 == 0: player = b.player1
            else: player = b.player2
            b.PutIn(int(math.trunc(math.pow(7,Difficulty)/(math.pow(7,Difficulty-i-1)))),player)
    return values

    #TODO: Winrates geven
def CalcBord(InpBord, Difficulty):
    #TODO: Winrates wete wel
    return minimax(0, 0, True, CalcValues(InpBord,Difficulty), -10000000, 10000000, Difficulty)