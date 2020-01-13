import Bord
import math
BestIndex = 0
def minimax(curDepth, nodeIndex,maxTurn, Difficulty,InpBord):
    if curDepth == Difficulty: return nodeIndex

    if maxTurn:
        Best = -1000000000
        BestPos = 0
        for i in range(7):
            pos = minimax(curDepth+1,nodeIndex * 7 + i, False, Difficulty,InpBord)
            x = CalcValue(InpBord,Difficulty,pos)
            if x >= Best:
                Best = x
                BestPos = pos
        return BestPos
    else:
        Worst = 1000000000
        WorstPos = 0
        for i in range(7):
            pos = minimax(curDepth + 1, nodeIndex * 7 + i, True, Difficulty,InpBord)
            x = CalcValue(InpBord, Difficulty, pos)
            if x <= Worst:
                Worst = x
                WorstPos = pos
        return WorstPos



def CalcValue(InpBord, Difficulty,i):
    b = Bord.Bord("Test", InpBord.player1, InpBord.player2)
    for y in range(6):
        for x in range(7):
            b.rooster[y][x] = InpBord.rooster[y][x]

    for j in range(Difficulty):
        if j % 2 == 0:
            player = b.player1
        else:
            player = b.player2
        b.PutIn(math.trunc(i / math.pow(7, Difficulty - j - 1)) % 7, player)
    b.UpdateBord()
    value = b.winrate
    if 3 * math.pow(7, Difficulty - 1) <= i or math.pow(7, Difficulty) - 3 * math.pow(7, Difficulty - 1) > i: value += 1
    return value
def CalcBord(InpBord, Difficulty):
    #TODO: Alfa Beta Pruning
    return math.trunc(minimax(0,0,True,Difficulty,InpBord)/math.pow(7,Difficulty-1))