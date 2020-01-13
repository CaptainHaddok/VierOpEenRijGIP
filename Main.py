import Bord
import MiniMax as MM
player1 = '1'
player2 = '2'
example = Bord.Bord("Bord 1",player1,player2)

while True:
    k = MM.CalcBord(example, 5)
    print(k)
    example.PutIn(k,player1)
    print(example)

    inpt1 = int(input("Welke rij?"))
    example.PutIn(inpt1, player2)
    print(example)