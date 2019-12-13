import Bord as B
def Check2InRow(inputBord, inputPlayer):
    # TODO: cheker fixen
    score = 0
    for y in range(len(inputBord.rooster)):                             # horizontaal --> dir = 0
        for x in range(len(inputBord.rooster[0])):                      # verticaal --> dir = 1
            if inputBord.rooster[y][x] == inputPlayer:                  # schuinbeneden --> dir = 2
                if CheckForAmount(inputBord, x, y, 0) == 2: score += 1  # schuinboven --> dir = 3
                if CheckForAmount(inputBord, x, y, 1) == 2: score += 1
                if CheckForAmount(inputBord, x, y, 2) == 2: score += 1
                if CheckForAmount(inputBord, x, y, 3) == 2: score += 1
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
def CheckForAmount(inputBord,inpX,inpY,inpDirection):
    amount = 1
    player = inputBord.rooster[inpY][inpX]
    len = 1;
    if inpDirection == 0:
        neg = True
        pos = True
        for i in range(3):
            if neg == True:
                try:
                    if inputBord.rooster[inpY][inpX -1 - i] == player:
                        len += 1
                        amount += 1
                    elif inputBord.rooster[inpY][inpX -1 -i] == 0:
                        len += 1
                    else: neg = False
                except: neg = False
            if pos == True:
                try:
                    if inputBord.rooster[inpY][inpX + 1 + i] == player:
                        len += 1
                        amount += 1
                    elif inputBord.rooster[inpY][inpX + 1 +i] == 0:
                        len += 1
                    else: pos = False
                except: pos = False
    if len < 4 : amount == 0
    #TODO Check voor hoeveel stenen er zijn in 1 rij,en zien dat het vier op een rij kan maken
    return amount