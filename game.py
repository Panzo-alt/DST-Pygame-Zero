import pgzrun
import random
import math
from pgzhelper import *
from entities import Knight, Bat, Enemy

#Screen dimensions
WIDTH = 800
HEIGHT = 600

#Game States and Audio variables
game_state = "start"
is_muted = False

#background music
music.play('background')
music.set_volume(0.5)

#Colours
black = (0, 0, 0)
brown = (139, 69, 19)
red = (255, 0, 0)
white = (255, 255, 255)

#Background
night = Actor('night')
night.x = 400
night.y = 300

knight = Knight()
bat = Bat()

#Game variables
score = 0
deathsound = False
velocity = 0 #Vertical velocity for the knight's jump
gravity = 0.5 #Gravity affecting the knight's jump
enemies = []        
enemies_timeout = 0

#Coin
coin = Actor('coingold')
coin.x = random.randint(900, 5000)
coin.y = random.randint(250, 350)

def reset_game():
    global score, velocity, game_state, deathsound, enemies_timeout
    
    # Reset variables
    score = 0
    velocity = 0
    game_state = "playing"
    deathsound = False
    
    # Clear out any existing enemies
    enemies.clear()
    enemies_timeout = 0
    
    # Reset actor positions
    knight.x = 100
    knight.y = 470
    
    bat.x = random.randint(900, 2000)
    bat.y = random.randint(100, 250)
    
    coin.x = random.randint(900, 5000)
    coin.y = random.randint(250, 350)
    
    # Restart the music if it's not muted
    if not is_muted:
        music.play('background')
        music.set_volume(0.5)

#Game start
def on_key_down(key):
    global game_state, is_muted

    # Start the game from the start screen
    if game_state == "start" and key == keys.SPACE:
        game_state = "playing"
        
    # Restart the game from the game over screen
    elif game_state == "gameover" and key == keys.R:
        reset_game()

    # Toggle Mute with the 'M' key at any time
    if key == keys.M:
        is_muted = not is_muted
        if is_muted:
            music.set_volume(0) # Mute music
        else:
            music.set_volume(0.5) # Restore music volume

def update():
    global velocity, score, enemies_timeout, game_state, deathsound

    if game_state != "playing":
        return
    
    knight.move()
    bat.move()

    #Coin movement across the screen
    coin.x -= 5  

    if coin.x < -50:
        coin.x = random.randint(900, 5000)
        coin.y = random.randint(250, 350)  

    #coin and knight collision
    if knight.colliderect(coin):
        if not is_muted:               
            sounds.collect.play()
        coin.x = random.randint(900, 5000)
        coin.y = random.randint(250, 350) 
        score += 5 

    # Enemies
    enemies_timeout += 1
    if enemies_timeout > random.randint(60, 7000):
        new_enemy = Enemy()
        enemies.append(new_enemy)
        enemies_timeout = 0
    
    # Move enemies across screen
    for pokermad in enemies.copy():
        pokermad.move()

        # remove pokermad and add one to score
        if pokermad.x < 50:
            enemies.remove(pokermad)    
            score += 1

    #Collision with pokermad
    if knight.collidelist(enemies) != -1: #If the knight collides with any pokermad, the game is over
        game_state = "gameover"
        enemies.remove(pokermad) #delete enemies

        if not is_muted:
            if deathsound == False:
                sounds.gameover.play() #play game over sound 
    
        deathsound = True #ensures game over sound only plays once

    # Bat and knight collision (Square root the score)
    if knight.colliderect(bat):
        # Square root the score and round it to the nearest whole number
        score = round(math.sqrt(score))
        
        # Reset the bat so it doesn't continuously drain the score
        bat.x = random.randint(900, 2000)
        bat.y = random.randint(100, 250)
        
        # Play a negative sound effect so the player knows they lost points!
        if not is_muted:
            try:
                sounds.bat.play() # Replace 'hurt' with whatever sound file you want to use
            except:
                pass # Just in case you don't have a hurt sound yet 

    # Win condition
    if score >= 10:
        if not is_muted:
            sounds.cheer.play()
        game_state = "gameover"           

def draw():
    # Draw background for all screens
    night.draw()

    if game_state == "start":
        # Draw Start Screen UI
        screen.draw.text('KNIGHT RUNNER', centerx=400, centery=150, color=white, fontsize=80)
        screen.draw.text('Press SPACE to Start', centerx=400, centery=300, color=white, fontsize=50)
        
        # Display current mute status
        mute_status = "MUTED" if is_muted else "ON"
        screen.draw.text(f"Press 'M' to Toggle Audio (Currently: {mute_status})", centerx=400, centery=400, color=white, fontsize=30)

    elif game_state == "playing":
        # Draw game objects
        bat.draw()
        knight.draw()
        coin.draw()
        screen.draw.text(f'Score: {score}', (10, 10), fontsize=30, color=white)
        for pokermad in enemies:
            pokermad.draw()

    elif game_state == "gameover" and score >= 10:
        # Draw Win Screen UI
        screen.draw.text('You Win!', centerx=400, centery=150, color=brown, fontsize=80)
        screen.draw.text(f'Score: {score}', centerx=400, centery=250, color=white, fontsize=60)
        
        # Tell the player how to restart
        screen.draw.text('Press R to Restart', centerx=400, centery=350, color=white, fontsize=40)
        music.stop()        

    elif game_state == "gameover":
        # Draw Game Over UI
        screen.draw.text('Game Over', centerx=400, centery=150, color=red, fontsize=80)
        screen.draw.text(f'Score: {score}', centerx=400, centery=250, color=white, fontsize=60)
        
        # Tell the player how to restart
        screen.draw.text('Press R to Restart', centerx=400, centery=350, color=white, fontsize=40)
        music.stop()
 
pgzrun.go()