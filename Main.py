import Bord
import MiniMax as MM
player1 = '1'
player2 = '2'
example = Bord.Bord("Bord 1",player1,player2)

while True:
    print(MM.CalcBord(example, 1))
    inpt1 = int(input("Welke rij?"))

    example.PutIn(inpt1,player1)
    print(example)

    inpt1 = int(input("Welke rij?"))

    example.PutIn(inpt1, player2)
    print(example)