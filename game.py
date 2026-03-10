import pgzrun
import random
from pgzhelper import *

#Screen dimensions
WIDTH = 800
HEIGHT = 600

#background music
music.play('background')
music.set_volume(0.5)

#Colours
black = (0, 0, 0)
brown = (139, 69, 19)
red = (255, 0, 0)
white = (255, 255, 255)

#Moon
moon = Actor('cartoon-moon')
moon.x = 650
moon.y = 200

#Houses
night = Actor('night')
night.x = 400
night.y = 300

#Bat
bat = Actor('bat1')
bat.x = 900
bat.y = 100
bat.images = ['bat1', 'bat2', 'bat3', 'bat4']
bat.fps = 10

#Enemies
enemies = []
enemies_timeout = 0 #counter to ensure enemies don't all appear at once


#Knight
knight = Actor('run1')
knight.x = 100
knight.y = 470
knight.images = ['run1', 'run2', 'run3', 'run4', 'run5', 'run6', 'run7', 'run8', 'run9', 'run10']
knight.fps = 15

#Game variables
score = 0
game_over = False
deathsound = False

velocity = 0 #Vertical velocity for the knight's jump
gravity = 0.5 #Gravity affecting the knight's jump

#Coin
coin = Actor('coingold')
coin.x = random.randint(900, 5000)
coin.y = random.randint(250, 350)

def update():
    global velocity, score, enemies_timeout, game_over, deathsound

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
    if game_over == False:
        coin.x -= 5  

    if coin.x < -50:
        coin.x = random.randint(900, 5000)
        coin.y = random.randint(250, 350)  

    #coin and knight collision
    if knight.colliderect(coin):
        sounds.collect.play()
        coin.x = random.randint(900, 5000)
        coin.y = random.randint(250, 350) 
        score += 5  

    #Enemies
    enemies_timeout += 1
    if enemies_timeout > random.randint(60, 7000):
        pokermad = Actor('pokermad')
        pokermad.x = 860
        pokermad.y = 500
        if game_over == False:
            enemies.append(pokermad)
            enemies_timeout = 0
        

    #Move enemies across screen
    for pokermad in enemies:
        pokermad.x -= 8
        #remove pokermad and add one to score
        if pokermad.x < 50:
            enemies.remove(pokermad)    
            score += 1

    #Collision with pokermad
    if knight.collidelist(enemies) != -1: #If the knight collides with any pokermad, the game is over
        game_over = True
        enemies.remove(pokermad) #delete enemies
        if deathsound == False:
            sounds.gameover.play() #play game over sound  
        deathsound = True #ensures game over sound only plays once


              


def draw():
    
    #Game over
    if game_over:
        screen.draw.text('Game Over', centerx = 380, centery = 150, color = red, fontsize=80)
        screen.draw.text(f'Score: {score}', centerx = 380, centery = 300, color = white, fontsize=60)
        music.stop()
    else:
        night.draw()
        bat.draw()
        knight.draw()
        coin.draw()
        screen.draw.text(f'Score: {score}', (10, 10), fontsize=30, color=white)
        for pokermad in enemies:
            pokermad.draw()
     

    

pgzrun.go()