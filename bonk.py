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
YELLOW = (255, 255, 0)
PINK = (255,182,193)
ORANGE = (249, 142, 29)
GULF = (201, 223, 236)
color1 = WHITE
color2 = WHITE
ball_color = WHITE
#Screen
SCREEN = pg.display.set_mode([WIDTH, HEIGHT])
pg.display.set_caption("Bonk")
SCREEN.fill((BLACK))

#MENU SETUP
#Buttons
bigfont = pg.font.SysFont('suigeneris', 60)
smallfont = pg.font.SysFont('suigeneris', 40)

start = bigfont.render('START', True, WHITE)
startRect = start.get_rect()
startRect.center = (WIDTH/2, HEIGHT/2)
player1 = smallfont.render('Player 1', True, WHITE)
player1Rect = player1.get_rect()
player1Rect.topleft = (50, 200)
player2 = smallfont.render('Player 2', True, WHITE)
player2Rect = player2.get_rect()
player2Rect.topright = (1000 - 50 , 200)
skip = bigfont.render('>>', True, WHITE)
skipRect = skip.get_rect()
skipRect.center = (WIDTH/2, 100)

pad_width = 10
pad_height = 80
red1 = pg.Rect(100, 300, pad_width, pad_height)
yellow1 = pg.Rect(120, 300, pad_width, pad_height)
green1 = pg.Rect(140, 300, pad_width, pad_height)
blue1 = pg.Rect(160, 300, pad_width, pad_height)
blue2 = pg.Rect(WIDTH - 10 - 100, 300, pad_width, pad_height)
green2 = pg.Rect(WIDTH - 10  - 120, 300, pad_width, pad_height)
yellow2 = pg.Rect(WIDTH - 10  - 140, 300, pad_width, pad_height)
red2 = pg.Rect(WIDTH - 10  - 160, 300, pad_width, pad_height)

ballcolor = smallfont.render('BALL COLOR', True, WHITE)
ballcolorRect = ballcolor.get_rect()
ballcolorRect.center = (WIDTH/2, 450)
ball_width = 10
ball_height = 10
ballcolor1 = pg.Rect(400, 500, ball_width, ball_height)
ballcolor2 = pg.Rect(500, 500, ball_width, ball_height)
ballcolor3 = pg.Rect(600, 500, ball_width, ball_height)
#GAME SETUP
#sounds
hitsound = pg.mixer.Sound('audio/hitsound.wav')
hit = pg.mixer.Sound('audio/hit.wav')
#music
playlist = ['audio/skepta.mp3', 'audio/darude.mp3', 'audio/giorgio.mp3']
#countdown
count = '3'
centertxt = bigfont.render(count, True, WHITE)
centertxtRect = centertxt.get_rect()
centertxtRect.center = (WIDTH/2, HEIGHT/3)
#Scoreboard
score1 = 0
score1txt = bigfont.render(str(score1), True, WHITE)
score1txtRect = score1txt.get_rect()
score1txtRect.center = (200, 50)
score2 = 0
score2txt = bigfont.render(str(score2), True, WHITE)
score2txtRect = score2txt.get_rect()
score2txtRect.center = (WIDTH-200, 50)

#Ball
ball = pg.Rect((WIDTH-ball_width)/2, (HEIGHT-ball_height)/2, ball_width, ball_height)
ball_speed_default = 8
ball_speed = ball_speed_default
ball_speed_y = 0
ball_speed_x = 0
#Paddles
pad_speed = 5
#Paddle 1
pad1 = pg.Rect(50,(HEIGHT-pad_height)/2, pad_width, pad_height)
#Paddle 2
pad2 = pg.Rect(WIDTH-50,(HEIGHT-pad_height)/2, pad_width, pad_height)

#Settings
clock = pg.time.Clock()


#Run Loop
run = True
menu = True
game = False
pg.mixer.music.load('audio/ps2.mp3')
skips = 0
for song in playlist:
    pg.mixer.music.queue(song)
pg.mixer.music.play()
while run:
    click = (500, 450)
    SCREEN.fill((BLACK))
    #Menu
    while menu:
        clock.tick(FPS)
        #Events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                menu = False
                run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                click = pg.mouse.get_pos()
        #Draw
        SCREEN.blit(start, startRect)
        SCREEN.blit(player1, player1Rect)
        SCREEN.blit(player2, player2Rect)
        SCREEN.blit(skip, skipRect)
        SCREEN.blit(ballcolor, ballcolorRect)
        
        if click[0] <= 500:
            pg.draw.rect(SCREEN, RED, red1)
            pg.draw.rect(SCREEN, YELLOW, yellow1)
            pg.draw.rect(SCREEN, GREEN, green1)
            pg.draw.rect(SCREEN, BLUE, blue1)
        if click[0] >= 500:
            pg.draw.rect(SCREEN, RED, red2)
            pg.draw.rect(SCREEN, YELLOW, yellow2)
            pg.draw.rect(SCREEN, GREEN, green2)
            pg.draw.rect(SCREEN, BLUE, blue2)
        if click[1] >= 400:
            pg.draw.rect(SCREEN, YELLOW, ballcolor1)
            pg.draw.rect(SCREEN, WHITE, ballcolor2)
            pg.draw.rect(SCREEN, BLUE, ballcolor3)
        #Clicks
        if red1.collidepoint(click):
            color1 = RED
            pg.draw.rect(SCREEN, BLACK, red1)
        if yellow1.collidepoint(click):
            color1 = YELLOW
            pg.draw.rect(SCREEN, BLACK, yellow1)
        if green1.collidepoint(click):
            color1 = GREEN
            pg.draw.rect(SCREEN, BLACK, green1)
        if blue1.collidepoint(click):
            color1 = BLUE
            pg.draw.rect(SCREEN, BLACK, blue1)
        if red2.collidepoint(click):
            color2 = RED
            pg.draw.rect(SCREEN, BLACK, red2)
        if yellow2.collidepoint(click):
            color2 = YELLOW
            pg.draw.rect(SCREEN, BLACK, yellow2)
        if green2.collidepoint(click):
            color2 = GREEN
            pg.draw.rect(SCREEN, BLACK, green2)
        if blue2.collidepoint(click):
            color2 = BLUE
            pg.draw.rect(SCREEN, BLACK, blue2)
        if ballcolor1.collidepoint(click): 
            ball_color = YELLOW
            pg.draw.rect(SCREEN, BLACK, ballcolor1)
        if ballcolor2.collidepoint(click): 
            ball_color = WHITE
            pg.draw.rect(SCREEN, BLACK, ballcolor2)
        if ballcolor3.collidepoint(click): 
            ball_color = BLUE
            pg.draw.rect(SCREEN, BLACK, ballcolor3)
        if skipRect.collidepoint(click):
            skips += 1
            if skips >= len(playlist):
                skips = 0
            pg.mixer.music.stop()
            pg.mixer.music.unload()
            pg.mixer.music.load(playlist[skips])
            pg.mixer.music.play()
            for song in playlist[skips+1:]:
                pg.mixer.music.queue(song)
            click = (0,0)
        if startRect.collidepoint(click):
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
        score1txt = bigfont.render(str(score1), True, WHITE)
        score2txt = bigfont.render(str(score2), True, WHITE)
        SCREEN.blit(score1txt, score1txtRect)
        SCREEN.blit(score2txt, score2txtRect)    

        #Draw
        pg.draw.rect(SCREEN, color1, pad1)
        pg.draw.rect(SCREEN, color2, pad2)
        pg.draw.rect(SCREEN, ball_color, ball)

        #Reset
        if reset:
            #Wins
            if score1 == 5:
                centertxt = bigfont.render('PLAYER 1 WINS!', True, WHITE)
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
                centertxt = bigfont.render('PLAYER 2 WINS!', True, WHITE)
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
            #Reset
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
                centertxt = bigfont.render(count, True, WHITE)
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
