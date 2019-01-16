
# Learning

import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
car_width = 73
high_score = 0

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('RaceCar Game Python Practice')
clock = pygame.time.Clock()

carImg = pygame.image.load('racecar.png')


def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def crash(score):
    global high_score
    font = pygame.font.SysFont(None, 32)
    if score > high_score:
        high_score = score
        new_high = font.render("NEW HIGH SCORE!!", True, (253, 134, 195))
        gameDisplay.blit(new_high, (310, 355))

    text = font.render("Highscore: " + str(high_score), True, (0, 250, 0))
    gameDisplay.blit(text, (352, 400))
    message_display('You crashed!')


def text_objects(text , font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    textSurface, textRect = text_objects(text, largeText)
    textRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(textSurface, textRect)
    pygame.display.update()
    time.sleep(4)

    game_loop()


def draw_hackermode():

    font = pygame.font.SysFont(None, 25)
    text = font.render("Hacker: ON", True, red)
    gameDisplay.blit(text, (700, 5))


def thins_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def game_loop():
    cube_color = black
    bg = white
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = False
    crashed = 0
    dodged = 0
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100
    hacker_mode = False
    car_speed = 5

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change -= car_speed
                elif event.key == pygame.K_RIGHT:
                    x_change += car_speed

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    print("Hackermode ON!")
                    hacker_mode = True
                    car_speed += 5

        x += x_change
        gameDisplay.fill(bg)

        if hacker_mode:
            tf = pygame.image.load("wtf.jpg")
            gameDisplay.blit(tf, (0, 0))

        things(thing_startx, thing_starty, thing_width, thing_height, cube_color)
        thing_starty += thing_speed
        thins_dodged(dodged)
        car(x, y)

        if hacker_mode:
            draw_hackermode()
            if cube_color == black:
                cube_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))

        if x > display_width - car_width or x < 0:
            crash(dodged)

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            thing_speed += 1
            thing_width += 3
            if hacker_mode:
                cube_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))

        if y < thing_starty+thing_height:
            if x + car_width > thing_startx and x < thing_startx + thing_width:
                crash(dodged)

        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
