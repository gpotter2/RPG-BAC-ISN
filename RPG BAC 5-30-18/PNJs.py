# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from Classes import *
from Textures import *

pygame.init()

global Current, Gesture

class GestuelClass(object):

    global Current, Gesture

    Personnages = ["LeoG", "CharlesA", "Fabien", "Nicolas", "CharlesV", "Marin",
                   "Ambre", "Amelie", "Marie", "Ewan", "Julie", "Alexis", "Adrien",
                   "Arno", "Barthelemy", "Emma", "Ewan", "Hippolyte", "Jean",
                   "Julien", "Martin", "Paul", "Sacha", "Soana", "Tanguy", "Thomas",
                   "Timothée", "VictorD", "Victoria"
                  ]
                  
    def ChargerGesture(self, Nom):
        global Current, Gesture
        Taille = [64, 64]
        Largeur = Taille[0]
        Hauteur = Taille[1]
        Perso = pygame.image.load("Textures/Perso/{}/Ov{}.png".format(Nom, Nom))
        Perso = pygame.transform.scale(Perso, (Largeur*3, Hauteur*4))

        #Gesture = self.ChargerGesture(Perso)
        

        Gesture = {}
        Taille = [64, 64]
        TailleX = Taille[0]
        TailleY = Taille[1]

        #FACE#
        Face0 = pygame.Surface(Taille, pygame.HWSURFACE|pygame.SRCALPHA)
        Face0.blit(Perso, (0,0), (TailleX*2, TailleY, TailleX*3, TailleY*2))
        Gesture["Face0"] = Face0

        Face1 = pygame.Surface(Taille, pygame.HWSURFACE|pygame.SRCALPHA)
        Face1.blit(Perso, (0,0), (TailleX*2, TailleY*2, TailleX*3, TailleY*3))
        Gesture["Face1"] = Face1

        Face2 = pygame.Surface(Taille, pygame.HWSURFACE|pygame.SRCALPHA)
        Face2.blit(Perso, (0,0), (TailleX*2, TailleY*3, TailleX*3, TailleY*4))
        Gesture["Face2"] = Face2

        #GAUCHE#
        Gauche0 = pygame.Surface(Taille, pygame.HWSURFACE|pygame.SRCALPHA)
        Gauche0.blit(Perso, (0,0), (0, TailleY*2, TailleX, TailleY*3))
        Gesture["Gauche0"] = Gauche0

        Gauche1 = pygame.Surface(Taille, pygame.HWSURFACE|pygame.SRCALPHA)
        Gauche1.blit(Perso, (0,0), (0, TailleY, TailleX, TailleY*2))
        Gesture["Gauche1"] = Gauche1

        Gauche2 = pygame.Surface(Taille, pygame.HWSURFACE|pygame.SRCALPHA)
        Gauche2.blit(Perso, (0,0), (0, TailleY*3, TailleX, TailleY*4))
        Gesture["Gauche2"] = Gauche2

        #DROITE#
        Droite0 = pygame.Surface(Taille, pygame.HWSURFACE|pygame.SRCALPHA)
        Droite0.blit(Perso, (0,0), (TailleX, 0, TailleX*2, TailleY))
        Gesture["Droite0"] = Droite0

        Droite1 = pygame.Surface(Taille, pygame.HWSURFACE|pygame.SRCALPHA)
        Droite1.blit(Perso, (0,0), (TailleX, TailleY, TailleX*2, TailleY*2))
        Gesture["Droite1"] = Droite1

        Droite2 = pygame.Surface(Taille, pygame.HWSURFACE|pygame.SRCALPHA)
        Droite2.blit(Perso, (0,0), (TailleX, TailleY*2, TailleX*2, TailleY*3))
        Gesture["Droite2"] = Droite2

        #DOS#
        Dos0 = pygame.Surface(Taille, pygame.HWSURFACE|pygame.SRCALPHA)
        Dos0.blit(Perso, (0,0), (0, 0, TailleX, TailleY))
        Gesture["Dos0"] = Dos0

        Dos1 = pygame.Surface(Taille, pygame.HWSURFACE|pygame.SRCALPHA)
        Dos1.blit(Perso, (0,0), (TailleX, TailleY*3, TailleX*2, TailleY*4))
        Gesture["Dos1"] = Dos1

        Dos2 = pygame.Surface(Taille, pygame.HWSURFACE|pygame.SRCALPHA)
        Dos2.blit(Perso, (0,0), (TailleX*2, 0, TailleX*3, TailleY))
        Gesture["Dos2"] = Dos2
        
        
        return Gesture
    
    #Gesture = ChargerGesture()
    
    #print(Gesture)

Gestuel = GestuelClass()

def MoveNPC(npc):
    npc.facing = random.choice(("Face0", "Dos0", "Gauche0", "Droite0"))
    npc.walking = random.choice((True, False))


class Dialogue(object):

    def __init__(self, Texte):
        self.Page = 0
        self.Texte = Texte #[('Page 1 Ligne 1', 'Page 1 Ligne 2'), ('Page 2 Ligne 1')]
        
class NPC(object):

    AllNPCs = []
    Decor = []
    LastLocation = 0
    Done = False
    
    def __init__(self, Nom, Pos, Dialogue, Surface):
        self.Name = Nom
        self.X = Pos[0]
        self.Y = Pos[1]
        self.Dialogue = Dialogue
        self.Surface = Surface
        self.Largeur = 64
        self.Hauteur = 64
        self.walking = False
        self.Timer = Timer(1)
        self.Timer.OnNext = lambda: MoveNPC(self)
        self.Current = "Face0"
        self.CurrentInit = "Face0"
        self.Gesture = Gestuel.ChargerGesture(Nom)

        NPC.AllNPCs.append(self)
        print(NPC.AllNPCs)
        
    def Render(self, surface):
        if not self.walking:
            #Mouv = 100 * Modules.deltatime
            #Location = [(self.X / Background.TailleGrid), ((self.Y+64) / Background.TailleGrid)]
            #Location1 = [((self.X+32) / Background.TailleGrid), ((self.Y+64) / Background.TailleGrid)]
            Location2 = [(self.X / Background.TailleGrid), ((self.Y+32) / Background.TailleGrid)]
            Location3 = [((self.X+32) / Background.TailleGrid), ((self.Y+32) / Background.TailleGrid)]
            
            #if self.LastLocation in Background.Obstacle and self.walking == True:
                #Background.Obstacle.remove(self.LastLocation)
                #Background.Obstacle.remove(self.LastLocation1)
                #Background.Obstacle.remove(self.LastLocation2)
                #Background.Obstacle.remove(self.LastLocation3)
            #if not Location in Background.Obstacle:
            #    Background.Obstacle.append(Location)
            #    self.LastLocation = Location
            #if not Location1 in Background.Obstacle:
            #    Background.Obstacle.append(Location1)
            #    self.LastLocation1 = Location1
            if not Location2 in Background.ObstaclePNJ:
               Background.ObstaclePNJ.append(Location2)
               self.LastLocation2 = Location2
            if not Location3 in Background.ObstaclePNJ:
               Background.ObstaclePNJ.append(Location3)
               self.LastLocation3 = Location3
        
                
        surface.blit(self.Gesture[self.Current], (self.X + Modules.Axe_x, self.Y + Modules.Axe_y))

class PNJ(NPC):

    def __init__(self, Nom, Pos, Dialogue = None, Surface = None):
        super(PNJ, self).__init__(Nom, Pos, Dialogue, Surface)
        #super().__init__()
    #def ApparitionPNJ(surface):
        
class Timer:
    
    def __init__(self, interval = 1):
        self.Interval = interval
        self.Value = 0
        self.LastInt = 0
        self.Active = False
        self.OnNext = None

        
