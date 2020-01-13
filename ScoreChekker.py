import Bord
import array
def Check2InRow(inputBord, inputPlayer):
    score = 0
    for y in range(len(inputBord.rooster)):
        for x in range(len(inputBord.rooster[0])):
                if CheckForAmount(inputBord, x, y, 1, 0, inputPlayer) == 2: score +=1
                if CheckForAmount(inputBord, x, y, 0, 1, inputPlayer) == 2: score += 1
                if CheckForAmount(inputBord, x, y, 1, 1, inputPlayer) == 2: score += 1
                if CheckForAmount(inputBord, x, y, 1, -1, inputPlayer) == 2: score += 1
    return score * 2


def Check3InRow(inputBord, inputPlayer):
    score = 0
    for y in range(len(inputBord.rooster)):
        for x in range(len(inputBord.rooster[0])):
            if CheckForAmount(inputBord, x, y, 1, 0, inputPlayer) == 3: score += 1
            if CheckForAmount(inputBord, x, y, 0, 1, inputPlayer) == 3: score += 1
            if CheckForAmount(inputBord, x, y, 1, 1, inputPlayer) == 3: score += 1
            if CheckForAmount(inputBord, x, y, 1, -1, inputPlayer) == 3: score += 1
    return score * 5

def CheckWin(inputBord, inputPlayer):
    score = 0
    for y in range(len(inputBord.rooster)):
        for x in range(len(inputBord.rooster[0])):
            if CheckForAmount(inputBord, x, y, 1, 0, inputPlayer) == 4: score += 1
            if CheckForAmount(inputBord, x, y, 0, 1, inputPlayer) == 4: score += 1
            if CheckForAmount(inputBord, x, y, 1, 1, inputPlayer) == 4: score += 1
            if CheckForAmount(inputBord, x, y, 1, -1, inputPlayer) == 4: score += 1
    return score * 1000000
def CheckForAmount(inputBord,inpX,inpY,inpXDirection,inpYDirection, inpPlayer):
    amount = 0
    nOpen = 0
    nPlayer = 0
    for i in range(4):
        try:
            if inputBord.rooster[inpY + i * inpYDirection][inpX + i * inpXDirection] == '0':
                nOpen += 1
            if inputBord.rooster[inpY + i * inpYDirection][inpX + i * inpXDirection] == inpPlayer:
                nPlayer += 1
        except:
            pass
    if nOpen + nPlayer == 4: amount = nPlayer
    return amount

def Horizontal(inputBord,inpPlayer):
    score = 0
    for x in range(4):
        for y in range(6):
            Aantalplayer = 0
            empty = 0
            for i in range(4):
                if inputBord.rooster[y][x + i] == inpPlayer: Aantalplayer += 1
                if inputBord.rooster[y][x + i] == '0': empty += 1
            aantal = 0
            if empty + Aantalplayer == 4: aantal = Aantalplayer
            if aantal == 2: score += 2
            if aantal == 3 and inpPlayer == '1': score+= 5
            if aantal == 3 and inpPlayer != '1': score += 100
            if aantal == 4: score += 1000000
    return score
def Vertical(inputBord,inpPlayer):
    score = 0
    for x in range(7):
        for y in range(3):
            Aantalplayer = 0
            empty = 0
            for i in range(4):
                if inputBord.rooster[y + i][x] == inpPlayer: Aantalplayer += 1
                if inputBord.rooster[y + i][x] == '0': empty += 1
            aantal = 0
            if empty + Aantalplayer == 4: aantal = Aantalplayer
            if aantal == 2: score += 2
            if aantal == 3 and inpPlayer == '1': score += 5
            if aantal == 3 and inpPlayer != '1': score += 100
            if aantal == 4: score += 1000000
    return score
def DiaDown(inputBord,inpPlayer):
    score = 0
    for x in range(4):
        for y in range(3):
            Aantalplayer = 0
            empty = 0
            for i in range(4):
                if inputBord.rooster[y + i][x + i] == inpPlayer: Aantalplayer += 1
                if inputBord.rooster[y + i][x + i] == '0': empty += 1
            aantal = 0
            if empty + Aantalplayer == 4: aantal = Aantalplayer
            if aantal == 2: score += 2
            if aantal == 3 and inpPlayer == '1': score += 5
            if aantal == 3 and inpPlayer != '1': score += 100
            if aantal == 4: score += 1000000
    return score

def DiaUp(inputBord,inpPlayer):
    score = 0
    for x in range(4):
        for y in range(3,6):
            Aantalplayer = 0
            empty = 0
            for i in range(4):
                if inputBord.rooster[y - i][x + i] == inpPlayer: Aantalplayer += 1
                if inputBord.rooster[y - i][x + i] == '0': empty += 1
            aantal = 0
            if empty + Aantalplayer == 4: aantal = Aantalplayer
            if aantal == 2: score += 2
            if aantal == 3 and inpPlayer == '1': score += 5
            if aantal == 3 and inpPlayer != '1': score += 100
            if aantal == 4: score += 1000000
    return score

