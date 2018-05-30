# -*- coding: utf-8 -*-

import sys, os, pygame, math
from pygame.locals import *
import time

Hauteur, Largeur = 600, 800
CoordSouris = 0
Souris_x, Souris_y = 0, 0
fond = pygame.image.load("Textures/Menu/Menu.png")
fond = pygame.transform.scale(fond, (Largeur, Hauteur))
Btn_Continue = pygame.image.load("Textures/Menu/Btn_continue.png")
Btn_Continue2 = pygame.image.load("Textures/Menu/Btn_continue2.png")
Btn_Reset = pygame.image.load("Textures/Menu/Btn_reset.png")
Btn_Reset2 = pygame.image.load("Textures/Menu/Btn_reset2.png")
Btn_Exit = pygame.image.load("Textures/Menu/Btn_exit.png")
Btn_Exit2 = pygame.image.load("Textures/Menu/Btn_exit2.png")
Sound = False

def procedure():
    	
    pygame.mixer.init(44100, 0, 2, 2048)
    pygame.init()
    Menu = pygame.display.set_mode((Largeur, Hauteur))
    Menu.blit(fond, (0,0))
    Menu.blit(Btn_Continue, (200,200))
    Menu.blit(Btn_Reset, (200,300))
    Menu.blit(Btn_Exit, (200,400))
    pygame.mixer.music.load("Musique/Test_DrumBass.mp3")
    pygame.mixer.music.play()
    volume = pygame.mixer.music.get_volume()
    pygame.mixer.music.set_volume(0.1)
    channel1 = pygame.mixer.Channel(0)
    Sound = False

#400*65
    

    while True:
        for event in pygame.event.get():
            
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

        for event in pygame.event.get():
            son = pygame.mixer.Sound("Musique/tic.wav")
            if event.type == pygame.MOUSEMOTION:
                CoordSouris = pygame.mouse.get_pos()
                Souris_x = event.pos[0]
                Souris_y = event.pos[1]

                    
                #if 400<Souris_y<465:
                    #son.play(0,1000,100)
                    #if 402<Souris_y<465:
                        #pygame.mixer.stop()
                    
                if 200<Souris_x <600 :
                    if 200<Souris_y<265:
                        Menu.blit(Btn_Continue2, (200,200))
                        if Sound == False:
                            Sound = True
                            son.play(0, 0)
                            
                    elif 300<Souris_y<365:
                        Menu.blit(Btn_Reset2, (200,300))
                        
                        if Sound == False:
                            Sound = True
                            son.play(0, 0)
                            
                    elif 400<Souris_y<465:
                        Menu.blit(Btn_Exit2, (200,400))
                        
                        if Sound == False:
                            Sound = True
                            son.play(0, 0)
                            
                        
                    else:
                        Menu.blit(fond, (0,0))
                        Menu.blit(Btn_Continue, (200,200))
                        Menu.blit(Btn_Reset, (200,300))
                        Menu.blit(Btn_Exit, (200,400))
                        Sound = False
                        
                else:
                    Menu.blit(fond, (0,0))
                    Menu.blit(Btn_Continue, (200,200))
                    Menu.blit(Btn_Reset, (200,300))
                    Menu.blit(Btn_Exit, (200,400))
                    
                    

            elif event.type == MOUSEBUTTONUP and event.button == 1:
                
                if 200<Souris_x <600 and 200<Souris_y<265:
                    #son.play(0,1000,10)
                    pygame.mixer.music.stop()
                    print("Continuer")
                    import Jeu
                    
                elif 200<Souris_x <600 and 300<Souris_y<365:
                    #son.play(0,1000,100)
                    print("Nouvelle Partie")
                    # Supprimer les fichiers de sauvegarde
                    try:
                        os.remove("Save/sauvegarde.json")
                    except:
                        pass
                    try:
                        os.remove("Save/sauvegarde_module.json")
                    except:
                        pass
                    try:
                        os.remove("Save/sauvegarde_map.json")
                    except:
                        pass

                elif 200<Souris_x <600 and 400<Souris_y<465:
                    print("Quittez")
                    pygame.quit()
                    sys.exit()

            
procedure()
