'''player1 = font.render('Player 1', True, WHITE)
player1Rect = player1.get_rect()
player1Rect.center = (250, 450)

Player2 = fot.render('Player 2', True, WHite)
Player2Rect = player2.get_rect()
Player2Rect.center = (750, 450)

red1 = pg.Rect(50, 550, pad_width, pad_height)
green1 = pg.Rect(100'''

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

#MENU SETUP
#Buttons
font = pg.font.SysFont('suigeneris', 60)
start = font.render('START', True, WHITE)
startRect = start.get_rect()
startRect.center = (WIDTH/2, HEIGHT/2)

#GAME SETUP
#sounds
hitsound = pg.mixer.Sound('audio/hitsound.wav')
ps2 = pg.mixer.Sound('audio/ps2.wav')
#music
giorgio = pg.mixer.music.load('audio/giorgio.mp3')

#countdown
count = '3'
centertxt = font.render(count, True, WHITE)
centertxtRect = centertxt.get_rect()
centertxtRect.center = (WIDTH/2, HEIGHT/3)
#Scoreboard
score1 = 0
score1txt = font.render(str(score1), True, WHITE)
score1txtRect = score1txt.get_rect()
score1txtRect.center = (200, 50)
score2 = 0
score2txt = font.render(str(score2), True, WHITE)
score2txtRect = score2txt.get_rect()
score2txtRect.center = (WIDTH-200, 50)

#Ball
ball_width = 10
ball_height = 10
ball = pg.Rect((WIDTH-ball_width)/2, (HEIGHT-ball_height)/2, ball_width, ball_height)
ball_speed_default = 7
ball_speed = ball_speed_default
ball_speed_y = 0
ball_speed_x = 0
#Paddles
pad_width = 10
pad_height = 80
pad_speed = 5
#Paddle 1
pad1 = pg.Rect(50,(HEIGHT-pad_height)/2, pad_width, pad_height)
#Paddle 2
pad2 = pg.Rect(WIDTH-50,(HEIGHT-pad_height)/2, pad_width, pad_height)

#Settings
click = (0, 0)
clock = pg.time.Clock()
SCREEN.fill((BLACK))



#Run Loop
run = True
menu = True
game = False
ps2.play()
pg.mixer.music.play()
while run:
    #Menu
    while menu:
        clock.tick(FPS)
        SCREEN.fill(BLACK)
        #Buttons
        SCREEN.blit(start, startRect)
        #Events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                menu = False
                run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                click = pg.mouse.get_pos()
        #Clicks
        if startRect.left <= click[0] <= startRect.right and startRect.top <= click[1] <= startRect.bottom:
            click = (0,0)
            menu = False
            game = True
        pg.display.update()
        

    #Game Loop
    reset = True
    reset_time = pg.time.get_ticks()
    hits = 0
    while game:
        clock.tick(FPS)
        SCREEN.fill((BLACK))
        score1txt = font.render(str(score1), True, WHITE)
        score2txt = font.render(str(score2), True, WHITE)
        SCREEN.blit(score1txt, score1txtRect)
        SCREEN.blit(score2txt, score2txtRect)    
        #Draw
        pg.draw.rect(SCREEN, color, pad1)
        pg.draw.rect(SCREEN, color, pad2)
        pg.draw.rect(SCREEN, WHITE, ball)

        #Reset
        if reset:
            if score1 == 5:
                centertxt = font.render('PLAYER 1 WINS!', True, WHITE)
                centertxtRect = centertxt.get_rect()
                centertxtRect.center = (WIDTH/2, HEIGHT/3)
                SCREEN.blit(centertxt, centertxtRect)
                time_delta = pg.time.get_ticks() - reset_time
                if time_delta > 3000:
                    score1 = 0
                    score2 = 0
                    menu = True
                    reset = False
                    game = False
            elif score2 == 5:
                centertxt = font.render('PLAYER 2 WINS!', True, WHITE)
                centertxtRect = centertxt.get_rect()
                centertxtRect.center = (WIDTH/2, HEIGHT/3)
                SCREEN.blit(centertxt, centertxtRect)
                time_delta = pg.time.get_ticks() - reset_time
                if time_delta > 3000:
                    score1 = 0
                    score2 = 0
                    menu = True
                    reset = False
                    game = False
            else:
                time_delta = pg.time.get_ticks() - reset_time
                if time_delta < 500:
                    count = '3'
                elif time_delta < 1000:
                    count = '2'
                elif time_delta < 1500:
                    count = '1'
                elif time_delta >= 1500:
                    ball_speed_y = random.randint(int((-ball_speed/4)), int(ball_speed/4))
                    ball_speed_x = int(sqrt(ball_speed**2 - abs(ball_speed_y)**2))
                    ball_speed_x *= random.choice([-1, 1])
                    reset = False
                centertxt = font.render(count, True, WHITE)
                centertxtRect = centertxt.get_rect()
                centertxtRect.center = (WIDTH/2, HEIGHT/3)
                SCREEN.blit(centertxt, centertxtRect)
        #Events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game = False
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
            hitsound.play()
            hits += 1
            if hits%3 == 0:
                ball_speed += 1
            ratio = (ball.centery - pad1.centery)/(pad_height/2)
            ball_speed_y = int(ratio*abs(ball_speed/sqrt(2)))
            ball_speed_x = int(sqrt(ball_speed**2 - ball_speed_y**2))
        if pg.Rect.colliderect(ball, pad2) and pad2.bottom > ball.centery and pad2.top < ball.centery:
            hitsound.play()
            hits += 1
            if hits%5 == 0:
                ball_speed += 1
            ratio = (ball.centery - pad2.centery)/(pad_height/2)
            ball_speed_y = ratio*abs(ball_speed_x)
            ball_speed_x = int(sqrt(ball_speed**2 - ball_speed_y**2))*-1
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_speed_y *= -1

        #End/Score
        if ball.left <= 0 or ball.right >= WIDTH:
            hitsound.play()
            if ball.left <= 0:
                score2 += 1
            else:
                score1 += 1
            reset = True
            ball.x = (WIDTH-ball_width)/2  
            ball.y = (HEIGHT-ball_height)/2
            ball_speed = ball_speed_default
            ball_speed_x = 0
            ball_speed_y = 0
            reset_time = pg.time.get_ticks()

        pg.display.update()
pg.quit()
