import pygame, sys 


pygame.init()
clock = pygame.time.Clock()

screen_width = 1200
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Pong Game")

#Game rectangles
ball = pygame.Rect(screen_width/2 - 15,screen_height/2 - 15,30,30)
player = pygame.Rect(screen_width - 20, screen_height / 2 - 70,10,140)
opponent = pygame.Rect(10, screen_height / 2 - 70,10,140)

#Colors
light_grey = (200,200,200)
bg_color = pygame.Color('grey12')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    clock.tick(60)