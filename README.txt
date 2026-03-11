======================================================
                  KNIGHT RUNNER
======================================================

A 2D endless runner game built with Python and Pygame Zero. 
Dodge the Pokermad enemies, collect gold coins, and beware 
of the bats that will instantly square root your score!

------------------------------------------------------
1. LIBRARIES & DEPENDENCIES
------------------------------------------------------
This project relies on the following Python libraries:

Built-in Python Libraries (No installation required):
- random: Used for spawning enemies, bats, and coins at random intervals.
- math: Used for the score penalty calculation when hitting a bat.

External Libraries (Must be installed):
- pgzero (Pygame Zero): The core game engine used for graphics, audio, and the game loop.
- pgzhelper: An extension for Pygame Zero used to handle actor animations easily.

------------------------------------------------------
2. HOW TO INSTALL AND RUN
------------------------------------------------------
Step 1: Install Python
Ensure you have Python 3 installed on your computer. You can download it from python.org.

Step 2: Install Required Libraries
Open your terminal or command prompt and run the following command to install the necessary game libraries:
    pip install pgzero pgzhelper

Step 3: Run the Game
Navigate to the folder containing your game files in the terminal/command prompt. Run the main Python file using:
    python game.py

(Note: Make sure your entities.py file and all your image/sound folders are in the exact same directory as main.py!)

------------------------------------------------------
3. CONTROLS
------------------------------------------------------
- SPACE: Start the game
- UP ARROW: Jump
- M: Toggle Mute (Audio on/off)
- R: Restart the game (Only works on the Game Over screen)

------------------------------------------------------
4. ENEMIES & GAMEPLAY MECHANICS
------------------------------------------------------
Your goal is to survive as long as possible while racking up a massive score. But the night is full of terrors:

- Pokermad (Ground Enemies): These are your primary threat. 
  * Impact: Colliding with a Pokermad results in an instant GAME OVER. 
  * Reward: Successfully jumping over one and letting it pass safely off the screen adds +1 to your score.

- Bats (Air Enemies): These winged pests won't kill you, but they will destroy your progress.
  * Impact: Colliding with a Bat triggers a mathematical curse! Your current score is immediately square-rooted. (For example, if you have a hard-earned 100 points and hit a bat, your score instantly plummets to 10!). Avoid them at all costs.

- Gold Coins: 
  * Reward: Jump to collect these for a quick +5 point boost to your score.

Enjoy the game!