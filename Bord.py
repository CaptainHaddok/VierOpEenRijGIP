import  ScoreChekker as Chekker

class Bord:
    def __init__(self, naam = "Bord", player1 = '1', player2 = '2',winrate = 0):
        self.naam = naam
        self.rooster = [['0','0','0','0','0','0','0'],['0','0','0','0','0','0','0'],['0','0','0','0','0','0','0'],['0','0','0','0','0','0','0'],['0','0','0','0','0','0','0'],['0','0','0','0','0','0','0'],]
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
        score += Chekker.Check2InRow(self, self.player1)
        score += Chekker.Check3InRow(self, self.player1)
        score += Chekker.CheckMiddle(self, self.player1)
        score += Chekker.CheckWin(self, self.player1)
        #score -= Chekker.Check2InRow(self, self.player2)
        score -= Chekker.Check3InRow(self, self.player2)
        return score
        # TODO: functies fixen

    def UpdateBord(self):
        self.winrate = self.CheckScore()

    def PutIn(self, row, player):
        curVal = '0'
        curPos = 0

        while curVal == '0' and curPos != 6:
            curVal = self.rooster[curPos][row]
            if curVal == '0':
                curPos = curPos + 1
        self.rooster[curPos - 1][row] = player
        self.UpdateBord()
        
        #Kanker
        #lmao
        #jksdhfkhsdjfgdjsbvgkjjdfbv j;
