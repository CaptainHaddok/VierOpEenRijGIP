import Bord as B
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


def CheckMiddle(inputBord, inputPlayer):
    score = 0
    # TODO: cheker fixen
    return score


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
    #TODO Check voor hoeveel stenen er zijn in 1 rij,en zien dat het vier op een rij kan maken
    if nOpen + nPlayer == 4: amount = nPlayer
    return amount

#Testen kut
