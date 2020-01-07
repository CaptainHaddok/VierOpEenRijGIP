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
            val = minimax(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta,Difficulty)
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
            val = minimax(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta,Difficulty)
            best = min(best, val)
            beta = min(beta, best)
            # Alpha Beta Pruning
            if beta <= alpha:
                break
        return best

def CalcValues(InpBord, Difficulty):
    values = {}
    for i in range(int(math.pow(7,Difficulty))):

        b = Bord.Bord("Test",InpBord.player1, InpBord.player2) #Bord kopiëren
        for y in range(6):                                     #Bord kopiëren
            for x in range(7):                                 #Bord kopiëren
                b.rooster[y][x] = InpBord.rooster[y][x]        #Bord kopiëren

        for j in range(Difficulty):
            if j%2 == 0: player = b.player1                    #PlayerBepalen
            else: player = b.player2                           #PlayerBepalen
            b.PutIn(math.trunc(i/math.pow(7,Difficulty-j-1))%7,player)
        b.UpdateBord()
        values[i] = b.winrate
        if 3 * math.pow(7, Difficulty - 1) <= i or math.pow(7, Difficulty) - 3 * math.pow(7, Difficulty - 1) > i :values[i] += 1
    return values

    #TODO: Winrates geven
def CalcBord(InpBord, Difficulty):
    #TODO: Winrates wete wel
    return minimax(0, 0, True, CalcValues(InpBord,Difficulty), -10000000, 10000000, Difficulty)