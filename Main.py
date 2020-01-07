import Bord
import MiniMax as MM
player1 = '1'
player2 = '2'
example = Bord.Bord("Bord 1",player1,player2)

while True:
    inpt1 = int(input("Welke rij?"))

    example.PutIn(inpt1,player1)
    print(example)

    inpt1 = int(input("Welke rij?"))

    example.PutIn(inpt1, player2)
    print(example)
    print(MM.CalcBord(example, 2))