import pgzrun
import random
from pgzhelper import *

#Screen dimensions
WIDTH = 800
HEIGHT = 600

#Colours
black = (0, 0, 0)
brown = (139, 69, 19)

#Moon
moon = Actor('cartoon-moon')
moon.x = 650
moon.y = 200

#Houses
sand = Actor('sand')
sand.x = 400
sand.y = 300

#Bat
bat = Actor('bat1')
bat.x = 900
bat.y = 100
bat.images = ['bat1', 'bat2', 'bat3', 'bat4']
bat.fps = 10

#Knight
knight = Actor('run1')
knight.x = 100
knight.y = 470
knight.images = ['run1', 'run2', 'run3', 'run4', 'run5', 'run6', 'run7', 'run8', 'run9', 'run10']
knight.fps = 15

velocity = 0 #Vertical velocity for the knight's jump
gravity = 0.5 #Gravity affecting the knight's jump

#Coin
coin = Actor('coingold')
coin.x = random.randint(900, 5000)
coin.y = random.randint(250, 350)

def update():
    global velocity

    #Knight animation
    knight.animate()

    #Jump animation
    if keyboard.up and knight.y == 470:
        velocity = -20
    knight.y += velocity
    velocity += gravity

    #Keeping the knight on the screen
    if knight.y > 470:
        velocity = 0
        knight.y = 470

    #Bat animation
    bat.animate()
    bat.x -= 5
    if bat.x < -50:
        bat.x = random.randint(1000, 15000)
        bat.y = random.randint(100, 250)

    #Coin movement across the screen
    coin.x -= 5  
    if coin.x < -50:
        coin.x = random.randint(900, 5000)
        coin.y = random.randint(250, 350)  

    #coin and knight collision
    if knight.colliderect(coin):
        sounds.collect.play()
        coin.x = random.randint(900, 5000)
        coin.y = random.randint(250, 350)    

def draw():
    screen.draw.filled_rect(Rect(0, 0, WIDTH, HEIGHT), (black)) #Sky
    screen.draw.filled_rect(Rect(0, 500, WIDTH, 500), (brown)) #Ground

    moon.draw()
    sand.draw()
    bat.draw()
    knight.draw()
    coin.draw()

pgzrun.go()