import Bord
import MiniMax as MM
import InputOutputHandler as IOH


pins0 = [18,23,24,25,12,16,20]
pins1 = [4,17,27,22,5,6,13]

player1 = 'X'
player2 = 'O'

inpH = IOH.InputHandler(list(reversed(pins0)),list(reversed(pins1)))
example = Bord.Bord(player1,player2)

win = 0
print("You can start")
while win == 0:
    inpt1 = inpH.checkInput()
    example.PutIn(inpt1, player2)
    print(example)
    win = example.Checkwin()
    if win == 0:
        k = MM.CalcBord(example, 2)
        print(k)
        example.PutIn(k,player1)
        print(example)
        win = example.Checkwin()
if win == 1:
    print("I won!")
elif win == 2:
    print("Agghhh, how did you beat me??")
