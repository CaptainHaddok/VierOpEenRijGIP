import pygame as pg

class color:
    black = (65, 65, 60)
    white = (255, 245, 214)
    blue = (69, 81, 255)
    green = (81, 173, 83)
    red = (255, 100, 69)
    yellow = (245, 218, 83)

class Cel:
    def __init__(self,width,height,content=0):
        self.width = width
        self.height = height
        self.content = content
class bord:
    def __init__(self,width,height):
        self.width = width*7
        self.height = height * 6
        self.drawing = 7 * [ 6 * [Cel(width,height)]]
    def drawBord(self,beginX,beginY):
        pg.draw.rect(screen,color.blue,(beginX,beginY,self.width,self.height))
        for i in range(0,6):
            for j in range(0,7):
                if self.drawing[j][i].content == 0:
                    pg.draw.circle(screen,color.white,(int(beginX + self.drawing[j][i].width/2 + j * self.drawing[j][i].width),int(beginY + self.drawing[j][i].height/2 + i * self.drawing[j][i].height)),int(self.drawing[j][i].width/2)-10)



pg.init()
pg.font.init()
screen = pg.display.set_mode((0,0),pg.FULLSCREEN)
titleFont = pg.font.SysFont('Comic Sans MS', 30)
normFont = pg.font.SysFont('Comic Sans MS', 20)


B = bord(150,150)
running = True


while running:
    screen.fill(color.black)
    mousePos = pg.mouse.get_pos()
    p = pg.display.get_surface().get_size()
    B.drawBord(50,p[1]-B.height-50)
    titel = titleFont.render('Connect4 Robot', True, color.white)
    subtitle = normFont.render('Warre Bruyninckx & Wieter Smolders', True,color.white)
    screen.blit(titel, (10, 0))
    screen.blit(subtitle,(10,35))

    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
    pg.display.flip()