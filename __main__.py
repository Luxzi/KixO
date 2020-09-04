import os, sys
import config
import pygame
import time

######################
# INIT RENDER ENGINE #
######################

def __init__(self):
    pygame.init()
    
    # Set Window Params
    gameDisplay = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('KixO - v0.1b1')


    # Define Vars
    clock = pygame.time.Clock()
    font32 = pygame.font.Font("assets/font/Inter-Bold.ttf", 32)
    font16 = pygame.font.Font("assets/font/Inter-Bold.ttf", 16)
    gametitle = font32.render("KixO", True, (0, 0, 0))
    play = font16.render("Play", True, (0, 0, 0))
    options = font16.render("Options - Disabled", True, (100, 100, 100))
    quit = font16.render("Quit", True, (0, 0, 0))
    cn = font16.render("(C) 2020 Luxzi", True, (0, 0, 0))
    curplay = font16.render("Currently Playing: Popliful by Luxzi", True, (0, 0, 0))
    


    #Load and Play Startup sound
    #pygame.mixer.music.load('assets/music/menutheme.mp3')
    #pygame.mixer.music.play(0)

    # Start Game Loop
    loop = True
    while loop == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

        #Close Game On Key Press
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_ESCAPE]: pygame.quit()
        
        # Draw Studio Intro
        gameDisplay.fill((255, 255, 255))
        gameDisplay.blit(pygame.image.load('assets/overlay/vigette.png'), (0, 0))
        gameDisplay.blit(gametitle, (gametitle.get_width() / 9, gametitle.get_height() / 4))
        gameDisplay.blit(play, (10, 50))
        gameDisplay.blit(options, (10, 70))
        gameDisplay.blit(quit, (10, 90))
        gameDisplay.blit(cn, (515, 460))
        gameDisplay.blit(curplay, (5, 460))

        
            
        pygame.display.flip()
        clock.tick(60)





__init__(None)