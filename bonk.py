import pygame as pg
import random, os
from math import sqrt

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
color = GREEN

#Screen
SCREEN = pg.display.set_mode([WIDTH, HEIGHT])
pg.display.set_caption("Bonk")
SCREEN.fill((BLACK))

#MENU
#Buttons
font = pg.font.SysFont('suigeneris', 60)
start = font.render('START', True, GREEN)
startRect = start.get_rect()
startRect.center = (WIDTH/2, HEIGHT/2)

#countdown
three = font.render('3', True, color)
threeRect = three.get_rect()
threeRect.center = (WIDTH/2, HEIGHT/3)
two = font.render('2', True, color)
twoRect = two.get_rect()
twoRect.center = (WIDTH/2, HEIGHT/3)
one = font.render('1', True, color)
oneRect = one.get_rect()
oneRect.center = (WIDTH/2, HEIGHT/3)

#OBJECTS:
#Ball
ball_width = 10
ball_height = 10
ball = pg.Rect((WIDTH-ball_width)/2, (HEIGHT-ball_height)/2, ball_width, ball_height)
ball_speed = 8

#Paddles
pad_width = 10 
pad_height = 80
pad_speed = 5
#Paddle 1
pad1 = pg.Rect(50,(HEIGHT-pad_height)/2, pad_width, pad_height)
#Paddle 2
pad2 = pg.Rect(WIDTH-50,(HEIGHT-pad_height)/2, pad_width, pad_height)

click = (0, 0)
clock = pg.time.Clock()
SCREEN.fill((BLACK))

#Menu
menu = True
run = True
while menu:
    clock.tick(FPS)
    #Events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            menu = False
        if event.type == pg.MOUSEBUTTONDOWN:
            click = pg.mouse.get_pos()
    #Buttons
    SCREEN.blit(start, startRect)
    #Clicks
    if startRect.left <= click[0] <= startRect.right and startRect.top <= click[1] <= startRect.bottom:
        menu = False
    pg.display.update()


#Game Loop
reset = True
reset_time = -1500
while run:
    clock.tick(FPS)
    SCREEN.fill((BLACK))    
    #Draw
    pg.draw.rect(SCREEN, color, pad1)
    pg.draw.rect(SCREEN, color, pad2)
    pg.draw.rect(SCREEN, color, ball)

    #Reset
    if reset:
        ball.x = (WIDTH-ball_width)/2  
        ball.y = (HEIGHT-ball_height)/2
        ball_speed_x = 0
        ball_speed_y = 0
        time_delta = pg.time.get_ticks() - reset_time
        if time_delta < 500:
            SCREEN.blit(three, threeRect)
        elif time_delta < 1000:
            SCREEN.blit(two, twoRect)
        elif time_delta < 1500:
            SCREEN.blit(one, oneRect)
        elif time_delta >= 1500:
            SCREEN.blit(one, oneRect)
            ball_speed_y = random.randint(int((-ball_speed/2)), int(ball_speed/2))
            ball_speed_x = int(sqrt(ball_speed**2 - abs(ball_speed_y)**2))
            ball_speed_x *= -1
            reset = False
    #Events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    keys = pg.key.get_pressed()

    #Ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    #Pads movement
    if keys[pg.K_w] and pad1.top > 0:
        pad1.y -= pad_speed
    if keys[pg.K_s] and pad1.bottom < HEIGHT:
        pad1.y += pad_speed
    if keys[pg.K_UP] and pad2.top > 0:
        pad2.y -= pad_speed
    if keys[pg.K_DOWN] and pad2.bottom < HEIGHT:
        pad2.y += pad_speed

    #Collisions
    if pg.Rect.colliderect(ball, pad1) and pad1.bottom > ball.centery and pad1.top < ball.centery:
        ratio = (ball.centery - pad1.centery)/(pad_height/2)
        ball_speed_y = int(ratio*abs(ball_speed/sqrt(2)))
        ball_speed_x = int(sqrt(ball_speed**2 - ball_speed_y**2))
    if pg.Rect.colliderect(ball, pad2) and pad2.bottom > ball.centery and pad2.top < ball.centery:
        ratio = (ball.centery - pad2.centery)/(pad_height/2)
        ball_speed_y = ratio*abs(ball_speed_x)
        ball_speed_x = int(sqrt(ball_speed**2 - ball_speed_y**2))*-1
    
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1
    #End
    if ball.left <= 0 or ball.right >= WIDTH:
        reset = True
        reset_time = pg.time.get_ticks()
    pg.display.update()

pg.quit()
