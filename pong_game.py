import pygame, sys 
 
#-------Animation Function-------

def ball_animation():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    #bounds the ball's movement to the window
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1

    #collisions
    if ball.colliderect(opponent):
        if ball_speed_x < 0:
            ball.left = opponent.right
            ball_speed_x *= -1

    if ball.colliderect(player):
        if ball_speed_x > 0:
            ball.right = player.left
            ball_speed_x *= -1

def player_animation():

    # Move player paddle
    player.y += player_speed
        
#-------Animation Function-------

pygame.init()
clock = pygame.time.Clock()

screen_width = 1200
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Pong Game")

#Game rectangles
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10, 140)
opponent = pygame.Rect(10 , screen_height / 2 - 70, 10, 140)

#Colors
light_grey = (200, 200, 200)
bg_color = pygame.Color(75, 73, 32)

#ball speed variables
ball_speed_x = 8 
ball_speed_y = 8
player_speed = 0
opponent_speed = 6

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_speed -= 10
            if event.key == pygame.K_s:
                player_speed += 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player_speed += 10
            if event.key == pygame.K_s:
                player_speed -= 10


    #Game Logic
    ball_animation()
    player_animation()

    #Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen,light_grey, player)
    pygame.draw.rect(screen,light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0 ), (screen_width/2, screen_height))


    #updataes the game window
    pygame.display.flip()
    clock.tick(60)