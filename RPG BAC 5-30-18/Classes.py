# -*- coding: utf-8 -*-

import pygame

class Modules:

    #global Axe_y, Axe_x
    Axe_y = -5
    Axe_x = 255
    Axe_xINIT = 255
    Axe_yINIT = -5
    Deplacement = ""

    DialogueOn = False
    ActiveDialogue = None

    Diff_x = 0
    Diff_y = 0
    
    #---PNJ---#
    #---#
    
    #def Mouvement(direction):
        #global Axe_y, Axe_x
        
        #if direction == 'haut':
            #Axe_y += 1
        #elif direction == 'bas':
            #Axe_y -= 1
       # elif direction == 'gauche':
            #Axe_x -= 1
        #elif direction == 'droite':
            #Axe_x += 1

        #return Axe_x, Axe_y
class Quest:

    #Premier Village#

    #Maison Perso#
    Maman = 0
    Bento = 0
