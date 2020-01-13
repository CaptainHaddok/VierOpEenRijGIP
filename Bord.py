import  ScoreChekker as Chekker
import array
class Bord:
    def __init__(self, naam = "Bord", player1 = '1', player2 = '2',winrate = 0):
        self.naam = naam
        self.rooster = [['.','.','.','.','.','.','.'],['.','.','.','.','.','.','.'],['.','.','.','.','.','.','.'],['.','.','.','.','.','.','.'],['.','.','.','.','.','.','.'],['.','.','.','.','.','.','.'],]
        self.winrate = winrate
        self.player1 = player1
        self.player2 = player2

    def __str__(self):
        stringOut = ""
        for i in range(len(self.rooster)):
            stringOut = stringOut + "\n|"
            for j in range(len(self.rooster[0])):
                stringOut = stringOut + str(self.rooster[i][j]) + "|"
        return stringOut

    def CheckScore(self):
        score = 0
        score += Chekker.Horizontal(self,self.player1)
        score += Chekker.Vertical(self, self.player1)
        score += Chekker.DiaDown(self, self.player1)
        score += Chekker.DiaUp(self, self.player1)
        score -= Chekker.Horizontal(self, self.player2)
        score -= Chekker.Vertical(self, self.player2)
        score -= Chekker.DiaUp(self, self.player2)
        score -= Chekker.DiaDown(self, self.player2)

        return score

    def UpdateBord(self):
        self.winrate = self.CheckScore()

    def PutIn(self, row, player):
        curVal = '.'
        Hoogte = 0

        while curVal == '.' and Hoogte != 6:
            curVal = self.rooster[Hoogte][row]
            if curVal == '.':
                Hoogte = Hoogte + 1
        if Hoogte !=0: self.rooster[Hoogte - 1][row] = player

