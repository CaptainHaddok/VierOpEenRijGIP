import pygame

class color():
    black = (0, 0, 0)
    white = (255, 255, 255)
    blue = (0, 0, 255)
    green = (0, 255, 0)
    red = (255, 0, 0)
    yellow = (255, 255, 0)


pygame.init()
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
running = True

screen.fill(color.white)

font = pygame.font.Font('freesansbold.ttf', 32)
titel = font.render('Connect4 Robot', True, color.black)
titelRect = titel.get_rect()
titelRect.center = (750, 200)
screen.blit(titel, titelRect)

font = pygame.font.Font('freesansbold.ttf', 20)
namen = font.render('Warre en Wieter', True, color.black)
namenRect = namen.get_rect()
namenRect.center = (750, 250)
screen.blit(namen, namenRect)


pygame.draw.rect(screen, color.blue, (250,300,705,610))
for y in range(7):
    for x in range(7):
        pygame.draw.circle(screen, color.white, (300 + y * 100, 350 + x * 100), 35)

pygame.display.flip()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            mousepos = pygame.mouse.get_pos()
            pygame.draw.rect(screen,color.white, (1500,100,200,200))
            font = pygame.font.Font('freesansbold.ttf', 20)
            mouse = font.render(str(mousepos), True, color.black)
            mouserect = mouse.get_rect()
            mouserect.center = (1600, 200)
            screen.blit(mouse, mouserect)
            pygame.display.flip()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                mousepos = pygame.mouse.get_pos()
                for x in range(5):
                    if 250 + x * 100 < mousepos[0] < 350 + x * 100:
                        row = x
                for y in range(5):
                    Color = pygame.Surface.get_at((row,350 + y * 100))
                    if Color != color.white:
                        pygame.draw.circle(screen,color.white,(row,350 + (y - 1) * 100))







