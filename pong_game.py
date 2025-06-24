import pygame, sys, random, time

pygame.init()
pygame.mixer.init()

player_score = 0
opponent_score = 0
 
bounce_sound = pygame.mixer.Sound("bounce.wav")
#-------Animation Function------------------------------------------------

def ball_animation():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    #bounds the ball's movement to the window
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    #collisions
    if ball.colliderect(opponent):
        if ball_speed_x < 0:
            ball.left = opponent.right
            ball_speed_x *= -1
            bounce_sound.play()

    if ball.colliderect(player):
        if ball_speed_x > 0:
            ball.right = player.left
            ball_speed_x *= -1
            bounce_sound.play()

def player_animation():

    #Move player paddle
    player.y += player_speed

    #Keep player paddle on screen
    if player.top < 0:
        player.top = 0
    if player.bottom > screen_height:
        player.bottom = screen_height

def opponent_animation():
    global opponent_speed
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed

def ball_reset():
    global ball_speed_x, ball_speed_y
    random_y = random.randint(0, screen_height - ball.height)
    ball.center = (screen_width / 2, random_y)
    ball_speed_x = 15 * random.choice((1, -1))
    ball_speed_y = 15 * random.choice((1, -1))

#-------Animation Function--------------------------------------------------

def render_scores():
    #scores
    font = pygame.font.Font(None, 500)
    player_text = font.render(f"{player_score}", True, "gray")
    opponent_text = font.render(f"{opponent_score}", True, "gray")

    player_text_rect = player_text.get_rect(center=(screen_width * 3 // 4, screen_height // 2))
    opponent_text_rect = opponent_text.get_rect(center=(screen_width // 4, screen_height // 2))

    screen.blit(player_text, player_text_rect)
    screen.blit(opponent_text, opponent_text_rect)

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
ball_speed_x = 15 
ball_speed_y = 15
player_speed = 0
opponent_speed = 15

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_speed -= 20
            if event.key == pygame.K_s:
                player_speed += 20
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player_speed += 20
            if event.key == pygame.K_s:
                player_speed -= 20
                
    #Game Logic
    ball_animation()
    player_animation()
    opponent_animation()

    if ball.left <= 0:
        player_score += 1
        ball_reset()
    if ball.right >= screen_width:
        opponent_score += 1
        ball_reset()

    #Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)

    render_scores()

    pygame.draw.ellipse(screen, "orange", ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0 ), (screen_width/2, screen_height))

    #updataes the game window
    pygame.display.flip()
    clock.tick(60)