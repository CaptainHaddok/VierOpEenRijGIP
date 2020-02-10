import Bord
import array
import MiniMax
def Horizontal(inputBord,inpPlayer):
    score = 0
    win = 0
    for x in range(4):
        for y in range(6):
            Aantalplayer = 0
            empty = 0
            for i in range(4):
                if inputBord.rooster[y][x + i] == inpPlayer: Aantalplayer += 1
                if inputBord.rooster[y][x + i] == '.': empty += 1
            aantal = 0
            if empty + Aantalplayer == 4: aantal = Aantalplayer
            if aantal == 2: score += 2
            if aantal == 3 and inpPlayer == 'X': score += 5
            if aantal == 3 and inpPlayer != 'X': score += 100
            if aantal == 4 and inpPlayer == 'X':
                score += 1000000
            if aantal == 4 and inpPlayer != 'X':
                score += 1000000

    return score
def Vertical(inputBord,inpPlayer):
    score = 0
    win = False
    for x in range(7):
        for y in range(3):
            Aantalplayer = 0
            empty = 0
            for i in range(4):
                if inputBord.rooster[y + i][x] == inpPlayer: Aantalplayer += 1
                if inputBord.rooster[y + i][x] == '.': empty += 1
            aantal = 0
            if empty + Aantalplayer == 4: aantal = Aantalplayer
            if aantal == 2: score += 2
            if aantal == 3 and inpPlayer == 'X': score += 5
            if aantal == 3 and inpPlayer != 'X': score += 100
            if aantal == 4 and inpPlayer == 'X':
                score += 1000000
            if aantal == 4 and inpPlayer != 'X':
                score += 1000000

    return score
def DiaDown(inputBord,inpPlayer):
    score = 0
    win = False
    for x in range(4):
        for y in range(3):
            Aantalplayer = 0
            empty = 0
            for i in range(4):
                if inputBord.rooster[y + i][x + i] == inpPlayer: Aantalplayer += 1
                if inputBord.rooster[y + i][x + i] == '.': empty += 1
            aantal = 0
            if empty + Aantalplayer == 4: aantal = Aantalplayer
            if aantal == 2: score += 2
            if aantal == 3 and inpPlayer == 'X': score += 5
            if aantal == 3 and inpPlayer != 'X': score += 100
            if aantal == 4 and inpPlayer == 'X':
                score += 1000000
            if aantal == 4 and inpPlayer != 'X':
                score += 1000000

    return score

def DiaUp(inputBord,inpPlayer):
    score = 0
    win =False
    for x in range(4):
        for y in range(3,6):
            Aantalplayer = 0
            empty = 0
            for i in range(4):
                if inputBord.rooster[y - i][x + i] == inpPlayer: Aantalplayer += 1
                if inputBord.rooster[y - i][x + i] == '.': empty += 1
            aantal = 0
            if empty + Aantalplayer == 4: aantal = Aantalplayer
            if aantal == 2: score += 2
            if aantal == 3 and inpPlayer == 'X': score += 5
            if aantal == 3 and inpPlayer != 'X': score += 100
            if aantal == 4 and inpPlayer == 'X':
                score += 1000000
            if aantal == 4 and inpPlayer != 'X':
                score += 1000000

    return score
