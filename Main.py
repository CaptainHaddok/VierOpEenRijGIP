import Bord
import MiniMax as MM
player1 = 'X'
player2 = 'O'
example = Bord.Bord("Bord 1",player1,player2)
win = 0
while win == 0:
    inpt1 = int(input("Welke rij?"))
    example.PutIn(inpt1, player2)
    print(example)
    win = example.Checkwin()
    if win == 0:
        k = MM.CalcBord(example, 5)
        print(k)
        example.PutIn(k,player1)
        print(example)
        win = example.Checkwin()
if win == 1:
    print("I won!")
elif win == 2:
    print("Agghhh, how did you beat me??")