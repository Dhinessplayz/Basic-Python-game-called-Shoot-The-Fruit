import pgzrun
import pygame

from random import randint
WIDTH = 800
HEIGHT = 604
score = 0
game_over = False
apple = Actor("apple")
apple.pos = 200, 200

def draw():
    global score
    global screen

    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((800,600),pygame.RESIZABLE)
    
    screen.clear()
    apple.draw()
    screen.draw.text("Score: " + str(score), color="white", topleft=(10, 10))
    

    if (score > 10):
        screen.draw.text("Level 1", color="white", topleft=(10,20))
        

    if (score > 30):
        screen.draw.text("Level 2", color="white", topleft=(10,30))
        

    if (score > 50):
        screen.draw.text("Level 4", color="white", topleft=(10,40))
        

    if (score > 70):
        screen.draw.text("Level 5", color="white", topleft=(10,50))
        

    if (score > 100):
        screen.draw.text("You are good at this!", color="white", topleft=(10,60))
        

    if (score > 120):
        screen.draw.text("Boss Player", color="white", topleft=(10,70))
           

    if game_over:
        screen.fill("black")
        screen.draw.text("This is your final score: " + str(score), topleft=(10, 10), fontsize=60)
       
pass

def place_apple():
    apple.x = randint(20, (WIDTH - 40))
    apple.y = randint(20, (HEIGHT - 40))
    pass
  

def on_mouse_down(pos):
    global score
    if apple.collidepoint(pos):
        screen.draw.text("Good Shot!", color="white", topleft=(10, 10))
        score = score+5
        clock.schedule(time_up, 15.0)
        place_apple()
    else:
        screen.draw.text("you have bad aim!", color="white", topleft=(10, 20))
    pass

def time_up():
    global game_over
    game_over = True
    pass




pgzrun.go()
