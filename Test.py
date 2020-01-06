import Bord

Bord1 = Bord.Bord(player1=1,player2=2)
Bord2 = Bord.Bord(player1=Bord1.player1, player2=Bord1.player2)
for i in range(6):
    for j in range(7):
        Bord2.rooster[i][j] = Bord1.rooster[i][j]
Bord1.PutIn(5,1)
print(Bord1)
print(Bord2)