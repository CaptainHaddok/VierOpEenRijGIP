import Bord
import math
BestIndex = 0
def minimax(curDepth, nodeIndex,maxTurn, scores, Difficulty):
    if curDepth == Difficulty: return nodeIndex

    if maxTurn:
        Best = -10000000
        BestPos = 0
        for i in range(7):
            pos = minimax(curDepth+1,nodeIndex * 7 + i, False, scores, Difficulty)
            x = scores[pos]
            if x >= Best:
                Best = x
                BestPos = pos
        return BestPos
    else:
        Worst = 10000000
        WorstPos = 0
        for i in range(7):
            pos = minimax(curDepth + 1, nodeIndex * 7 + i, False, scores, Difficulty)
            x = scores[pos]
            if x <= Worst:
                Worst = x
                WorstPos = pos
        return WorstPos



def CalcValues(InpBord, Difficulty):
    values = {}
    for i in range(int(math.pow(7,Difficulty))):

        b = Bord.Bord("Test",InpBord.player1, InpBord.player2)
        for y in range(6):
            for x in range(7):
                b.rooster[y][x] = InpBord.rooster[y][x]

        for j in range(Difficulty):
            if j%2 == 0: player = b.player1
            else: player = b.player2
            b.PutIn(math.trunc(i/math.pow(7,Difficulty-j-1))%7,player)
        b.UpdateBord()
        values[i] = b.winrate
        if 3 * math.pow(7, Difficulty - 1) <= i or math.pow(7, Difficulty) - 3 * math.pow(7, Difficulty - 1) > i :values[i] += 1
    return values

def CalcBord(InpBord, Difficulty):
    #TODO: Winrates Optimalisatie
    return math.trunc(minimax(0,0,True,CalcValues(InpBord,Difficulty),Difficulty)/math.pow(7,Difficulty-1))