import pygame

class color():
    Black = (0,0,0)
    White = (255,255,255)
    Blue = (0,0,255)
    Green = (0,255,0)
    Red = (255,0,0)
    Yellow = (255,255,0)

xMid = 950
yMid = 550

pygame.init()
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
running = True

#Menu layout
pygame.display.set_caption('GIP - Wieter en Warre')
font = pygame.font.Font('freesansbold.ttf', 32)
titel = font.render('Connect4 Robot', True, color.Black)
titelRect = titel.get_rect()
titelRect.center = (xMid, 200)

font = pygame.font.Font('freesansbold.ttf', 20)
namen = font.render('Warre en Wieter', True, color.Black)
namenRect = namen.get_rect()
namenRect.center = (xMid, 250)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, color.Blue, (250,300,1000,600))
    screen.blit(titel, titelRect)
    screen.blit(namen, namenRect)
    pygame.display.flip()
pygame.quit()