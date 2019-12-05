import Bord as B
def Check2InRow(inputBord, inputPlayer):
    score = 0
    player = inputPlayer
    bord = inputBord
    for y in range(len(bord.rooster)):          #checken voor elke plaats in het rooster
        for x in range(len(bord.rooster[0])):
            if bord.rooster[y][x] == player:    #als het de speler is voor wie we score willen bepalen
                Xcheck = True                   # Variabelen klaarzetten om te zien of alle richtingen gecheckt moeten worden
                Ycheck = True
                DiaDownCheck = True
                DiaUpCheck = True
                for i in range(3):              #Je moet voor zowel de direct naast huidige pos als die daarnaast en die daarnaast checken
                    if x+1+i >= len(bord.rooster[0]): Xcheck = False                            #Checken voor alle rihtingen of die plaats voor te checken echt bestaat
                    if y+1+i >= len(bord.rooster): Ycheck = False                               # Zo niet dan hoef je ook niet meer te kijken of die daarna wel bestaat
                    if x+1+i >= len(bord.rooster[0]) or y+1+i >= len(bord.rooster): DiaDownCheck = False
                    if x+1+i >= len(bord.rooster[0]) or y-1-i < 0: DiaUpCheck = False

                    if Xcheck == True:                                                    #als ze bestaan, checken of het een plaats van speler 1 is, dan score +1
                        if bord.rooster[y][x+1+i] == player: score +=1                    #als het dan geen nul is, moet het wel speler 2 zijn, en dan is alles daarna ook geen 4 op een rij meer
                        elif bord.rooster[y][x+1+i] != '0': Xcheck = False
                    if Ycheck == True:
                        if bord.rooster[y+1+i][x] == player: score +=1
                        elif bord.rooster[y+1+i][x] != '0': Ycheck = False
                    if DiaDownCheck == True:
                        if bord.rooster[y+1+i][x+1+i] == player: score +=1
                        elif bord.rooster[y+1+i][x+1+i] != '0': DiaDownCheck = False
                    if DiaUpCheck == True:
                        if bord.rooster[y-1-i][x+1+i] == player: score +=1
                        elif bord.rooster[y-1-i][x+1+i] != '0': DiaUpCheck = False
    return score


def Check3InRow(inputBord, inputPlayer):
    score = 0
    # TODO: cheker fixen
    return score


def CheckMiddle(inputBord, inputPlayer):
    score = 0
    # TODO: cheker fixen
    return score


def CheckWin(inputBord, inputPlayer):
    score = 0
    # TODO: cheker fixen
    return score