import Bord
import math

def minimax(curDepth, nodeIndex,maxTurn, scores, Difficulty):
    if curDepth == Difficulty: return scores[nodeIndex]

    if maxTurn:
        Best = -10000000
        for i in range(7):
            x = minimax(curDepth+1,nodeIndex * 7 + i, False, scores, Difficulty)
            if x >= Best: Best = x
        return x
    else:
        Worst = 10000000
        for i in range(7):
            x = minimax(curDepth+1,nodeIndex * 7 + i, True, scores, Difficulty)
            if x <= Worst: Worst = x
        return x



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
    #TODO: Winrates wete wel
    return minimax(0,0,True,CalcValues(InpBord,Difficulty),Difficulty)