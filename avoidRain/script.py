import pygame
import sys
import time
import copy
from typing import List
from random import randint as rd
import math
import subprocess as sbp

pygame.init()
pygame.font.init()
myfont: pygame.font.Font = pygame.font.SysFont('Comic Sans MS', 40)
pygame.mixer.music.load('the-avengers-theme-song-youtubemp3free.org.wav')
pygame.mixer.music.play(-1)
width = 1000
height = 700

screen: pygame.Surface = pygame.display.set_mode([width, height])
pygame.display.set_caption("Try to avoid rain simulator")

def playGame(screen):


    deltaX: float = 0
    deltaY: float = 0
    speed: float = 1.5

    playerX: float = 600
    playerY: float = 600
    playerSize = 5
    collisionDis = playerSize * 1.6

    rainS = []


    def distance(x1: float, y1: float, x2: float, y2: float):
        xDis = abs(x2 - x1)
        yDis = abs(y2 - y1)
        return math.sqrt(xDis ** 2 + yDis ** 2)

    def constraint(inp: float, lower: float, upper: float):
        result = inp
        if inp < lower:
            result = lower
        elif inp > upper:
            result = upper
        return result

    def checkCollision():
        for rain in rainS:
            if distance(rain.x, rain.y, playerX, playerY) < collisionDis:
                print('you lost')
                return True


    class Rain():
        def __init__(self, x: float, y: float, xV: float, yV: float):
            self.x: float = x
            self.y: float = y
            self.xV: float = xV
            self.yV: float = yV
            self.size = 10
        def move(self):
            self.x += self.xV
            self.y += self.yV



        def draw(self, screen):
            pygame.draw.polygon(screen, (111, 123, 234), 
                        [[self.x - self.size, self.y], 
                        [self.x, self.y + self.size + 5],
                        [self.x + self.size, self.y], 
                        [self.x, self.y - self.size - 5]])  # draws a kite

    def appendRains(x: int, y: int, num: int):

        for i in range(num):
            rainS.append(Rain(x, y, rd(-10, 10)/10, rd(-10, 10)/10))
   


    #home screen
    done = False
    seeInstructions = False
    while not done:
        screen.fill((0, 0, 0))
        textsurface = myfont.render("Welcome to avoid rain!", False, (255, 255, 255))
        screen.blit(textsurface,(200, 200))
        textsurface = myfont.render("a game made by Andy Chen!", False, (255, 255, 255))
        screen.blit(textsurface,(200, 300))
        textsurface = myfont.render("press space to start! or press I to see instructions", False, (255, 255, 255))
        screen.blit(textsurface,(100, 400))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    done = True
                elif event.key == pygame.K_i:
                    seeInstructions = True
                    done = True

    if seeInstructions:
        screen.fill((0, 0, 0))
        textsurface = myfont.render("use arrow keys to move your character and avoid the rain!", False, (255, 255, 255))
        screen.blit(textsurface,(0, 200))
        pygame.display.flip()    

        time.sleep(2)

    iteration = 0
    level = 0
    while True:
        
        screen.fill((0, 0, 0))
        

        pygame.draw.circle(screen, (255, 255, 150), [int(playerX), int(playerY)], round(playerSize))
        for rain in rainS:
            rain.move()
            rain.draw(screen)

        playerX += deltaX
        playerY += deltaY
        playerX = constraint(playerX, 0, width)
        playerY = constraint(playerY, 0, height)
        if checkCollision():
            break
        textsurface = myfont.render("level: %d" % (level), False, (255, 255, 255))
        screen.blit(textsurface,(500, 0))
        pygame.display.flip()

        for rain in rainS:
            if rain.x < 0 or width < rain.x or rain.y < 0 or height < rain.y:
                rainS.pop(rainS.index(rain))

        if iteration % 50 == 0:
            rand = rd(0, 3)
            randNum = rd(5, 10)
            if rand == 0:
                appendRains(0, 0, randNum)
            elif rand == 1:
                appendRains(width, 0, randNum)
            elif rand == 2:
                appendRains(0, height, randNum)
            elif rand == 3:
                appendRains(width, height, randNum)
        iteration += 1
        level = iteration / 2000

        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    deltaY = -speed
                elif event.key == pygame.K_DOWN:
                    deltaY = speed
                elif event.key == pygame.K_LEFT:
                    deltaX = -speed
                elif event.key == pygame.K_RIGHT:
                    deltaX = speed
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    deltaY = 0
                elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    deltaX = 0
        
        



        # ending screen
    while True:
        screen.fill((0, 0, 0))
        textsurface = myfont.render("you lost lol, press space play again", False, (255, 255, 255))
        screen.blit(textsurface,(200, 200))
        pygame.display.flip()    

        time.sleep(2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playGame(screen)
playGame(screen)

