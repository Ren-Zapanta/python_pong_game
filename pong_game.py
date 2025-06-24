import pygame, sys 


pygame.init()
clock = pygame.time.Clock()

screen_width = 1200
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Pong Game")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quitl()
            sys.exit()

    pygame.display.flip()
    clock.tick(60)