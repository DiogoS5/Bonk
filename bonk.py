import pygame as pg
import random, os

pg.init()

#Consts
FPS = 60
WIDTH = 1000
HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 255)
PINK = (255,182,193)
ORANGE = (249, 142, 29)
GULF = (201, 223, 236)
colors = [WHITE, RED, GREEN, YELLOW, PINK, ORANGE, GULF]
color = random.choice(colors)

#Screen
SCREEN = pg.display.set_mode([WIDTH, HEIGHT])
pg.display.set_caption("Bonk")
SCREEN.fill((BLACK))

#Ball
ball_width = 10
ball_height = 10
ball = pg.Rect((WIDTH-ball_width)/2, (HEIGHT-ball_height)/2, ball_width, ball_height)
ball_speed_x = 10

#Paddles
pad_width = 10 
pad_height = 80
#Paddle 1
pad1 = pg.Rect(50,(HEIGHT-pad_height)/2, pad_width, pad_height)
pad1_speed_y = 0
#Paddle 2
pad2 = pg.Rect(WIDTH-50,(HEIGHT-pad_height)/2, pad_width, pad_height)
pad2_speed_y = 0

'''---------------------------------------------------------------'''

#Game Loop
clock = pg.time.Clock()
run = True
reset = True
while run:
    clock.tick(FPS)
    SCREEN.fill((BLACK))
    #Reset
    if reset:
        ball.x = (WIDTH-ball_width)/2  
        ball.y = (HEIGHT-ball_height)/2
        ball_speed_x *= -1
        ball_speed_y = random.randint(-5, 5)
        reset = False
    #Events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        mouse = pg.mouse.get_pos()
        keys = pg.key.get_pressed()
    
    #Draw
    pg.draw.rect(SCREEN, color, pad1)
    pg.draw.rect(SCREEN, color, pad2)
    pg.draw.rect(SCREEN, color, ball, 10)

    #Ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    #Pads movement
    if keys[pg.K_w] and pad1.top > 0:
        pad1.y -= 10
    if keys[pg.K_s] and pad1.bottom < HEIGHT:
        pad1.y += 10
    if keys[pg.K_UP] and pad2.top > 0:
        pad2.y -= 10
    if keys[pg.K_DOWN] and pad2.bottom < HEIGHT:
        pad2.y += 10

    #Collisions
    if pg.Rect.colliderect(ball, pad1) or pg.Rect.colliderect(ball, pad2):
        ball_speed_x *= -1
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    #End
    if ball.left <= 0 or ball.right >= WIDTH:
        reset = True
    pg.display.update()

pg.quit()
