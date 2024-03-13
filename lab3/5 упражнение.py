import pygame
from sys import exit

pygame.init()

display = pygame.display.set_mode( (800, 600) )
display.fill((255,255,255))


pygame.draw.circle( display, (255, 255, 0) , (400,250), 200)
pygame.draw.circle( display, (255,0,0) , (500,200), 25)
pygame.draw.circle( display, (0,0,0) , (500,200), 15)
pygame.draw.circle( display, (255,0,0) , (300,200), 35)
pygame.draw.circle( display, (0,0,0) , (300,200), 20)
pygame.draw.polygon( display, (0, 0, 0) , ( (500, 400), (500, 370), (300, 370), (300, 400) ) )
pygame.draw.polygon( display, (0, 0, 0) , ( (445, 180),(450, 190), (600, 140), (595, 130) ) )
pygame.draw.polygon( display, (0, 0, 0) , ( (390, 205), (395, 190), (195, 100), (190, 115) ) )
FPS = 60
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()

    clock.tick(FPS)