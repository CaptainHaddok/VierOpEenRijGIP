import  ScoreChecker as Checker
class Bord:
    def __init__(self, player1 = '1', player2 = '2'):
        self.rooster = [['.','.','.','.','.','.','.'],['.','.','.','.','.','.','.'],['.','.','.','.','.','.','.'],['.','.','.','.','.','.','.'],['.','.','.','.','.','.','.'],['.','.','.','.','.','.','.'],]
        self.winrate = 0
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
        score += Checker.Horizontal(self,self.player1)
        score += Checker.Vertical(self, self.player1)
        score += Checker.DiaDown(self, self.player1)
        score += Checker.DiaUp(self, self.player1)
        score -= Checker.Horizontal(self, self.player2)
        score -= Checker.Vertical(self, self.player2)
        score -= Checker.DiaUp(self, self.player2)
        score -= Checker.DiaDown(self, self.player2)

        return score

    def UpdateBord(self):
        self.winrate = self.CheckScore()

    def PutIn(self, row, player):
        curVal = self.rooster[0][row]
        Hoogte = 0

        while curVal == '.' and Hoogte != 6:
            curVal = self.rooster[Hoogte][row]
            if curVal == '.':
                Hoogte = Hoogte + 1
        if Hoogte !=0:
            self.rooster[Hoogte - 1][row] = player
        self.UpdateBord(self);

    def Checkwin(self):
        win = 0
        if Checker.Horizontal(self, self.player1) >= 1000000 or Checker.Vertical(self, self.player1) >= 1000000 or Checker.DiaDown(self, self.player1) >= 1000000 or Checker.DiaUp(self, self.player1) >= 1000000:
            win = 1
            return win
        if Checker.Horizontal(self, self.player2) >= 1000000 or Checker.Vertical(self, self.player2) >= 1000000 or Checker.DiaDown(self, self.player2) >= 1000000 or Checker.DiaUp(self, self.player2) >= 1000000:
            win = 2
            return win
        else:
            return win
