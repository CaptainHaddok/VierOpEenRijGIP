import Bord
import MiniMax as MM
player1 = 'X'
player2 = 'O'
example = Bord.Bord("Bord 1",player1,player2)

while True:
    k = MM.CalcBord(example, 2)
    print(k+1)
    example.PutIn(k,player1)
    print(example)

    inpt1 = int(input("Welke rij?"))
    example.PutIn(inpt1-1, player2)
    print(example)