# -*- coding: utf-8 -*-

import pygame, sys, math

#from Jeu import *
from Textures import *
from pygame.locals import *

def SauvegarderMap(Fichier):
    MapData = ""
    Max_x = 0
    Max_y = 0

    for t in SpriteData:
        if t[0] > Max_x:
            Max_x = t[0]
        if t[1] > Max_y:
            Max_y = t[1]

    for Sprite in SpriteData:
        MapData = MapData + str(int(Sprite[0] / Background.TailleGrid)) + "," + str(int(Sprite[1] / Background.TailleGrid)) + ":" + Sprite[2] + "-"

    MapData = MapData + str(int(Max_x / Background.TailleGrid)) + "," + str(int(Max_y / Background.TailleGrid))

    with open(Fichier, "w") as FichierMap:
        FichierMap.write(MapData)

                

    
Editeur = pygame.display.set_mode((Background.TailleGrid*51, Background.TailleGrid*30), HWSURFACE)
pygame.display.set_caption("Editeur de Map")
clock = pygame.time.Clock()

#---INVEDIT---#
InvEdit = pygame.Surface((Background.TailleGrid*51, Background.TailleGrid*15), HWSURFACE|SRCALPHA)
InvEdit.fill((0,0,0))
Editeur.blit(InvEdit, (0,Background.TailleGrid*10))
X = 0
Y = 0
Count = 0
CopyData = []
CopyData2 = []

for cle in Background.DicoTextures:
    CopySprite = [Background.TailleGrid*(X+1), Background.TailleGrid*(16+Y), cle] #16+Y
    X += 2
    Count += 1
    if Count <= 175:
        CopyData.append(CopySprite)
    elif Count > 175:
        CopyData.append(CopySprite2)
    #print(len(CopyData))
    #print(Y)
    if X == 50:
        X = 0
        Y += 2
Inv = "Close"
InvPage = 1
#---#

#---CHARGER UNE MAP---#
def RechargerMap(Fichier):
    global SpriteData
    with open(Fichier, "r") as FichierMap:
        MapData = FichierMap.read()
    MapData = MapData.split("-")
    TailleMap = MapData[len(MapData)-1]
    MapData.remove(TailleMap)
    TailleMap = TailleMap.split(",")
    TailleMap[0] = int(TailleMap[0])*Background.TailleGrid
    TailleMap[1] = int(TailleMap[1])*Background.TailleGrid

    Sprites = []

    for Sprite in range(len(MapData)):
        MapData[Sprite] = MapData[Sprite].replace("\n","")
        Sprites.append(MapData[Sprite].split(":"))

    for Sprite in Sprites:
        Sprite[0] = Sprite[0].split(",")
        Pos = Sprite[0]
        for P in Pos:
            Pos[Pos.index(P)] = int(P)
        Sprites[Sprites.index(Sprite)] = [Pos[0] * Background.TailleGrid, Pos[1] * Background.TailleGrid, Sprite[1]]

    SpriteData = Sprites
    
#---#

CoordSouris = 0
Souris_x, Souris_y = 0, 0

Largeur_Map, Hauteur_Map = 4*Background.TailleGrid, 1*Background.TailleGrid
Selection = pygame.Surface((Background.TailleGrid, Background.TailleGrid), HWSURFACE|SRCALPHA)
Selection.fill((200,0,0))

X = 0
SpriteData = []
Axe_x, Axe_y, Deplacement = 0, 0, 0

Brush = "1"

#--- MAP ---#

for x in range(0, Largeur_Map*20, Background.TailleGrid):
    for y in range(0, Hauteur_Map*50, Background.TailleGrid):
        SpriteData.append([x, y, "3"])


Continuer = True

while Continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Continuer = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z or event.key == pygame.K_UP:
                Deplacement = "haut"
                #Modules.Mouvement('haut')
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                Deplacement = "bas"
                #Modules.Mouvement('bas')
            elif event.key == pygame.K_q or event.key == pygame.K_LEFT:
                Deplacement = "gauche"
                #Modules.Mouvement('gauche')
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                Deplacement = "droite"
                #Modules.Mouvement('droite')

                
            elif event.key == pygame.K_F4:
                Brush = "r"

            elif event.key == pygame.K_F1:
                Selectionner = input("Brush Tag :")
                Brush = Selectionner
        
            elif event.key == pygame.K_F3:
                NomDeLaMap = input("Nom De La Map :")
                SauvegarderMap("maps/" + NomDeLaMap + ".map")
            elif event.key == pygame.K_F11:
                NomDeLaMap = input("Nom De La Map :")
                RechargerMap("maps/" + NomDeLaMap + ".map")
                
                
            elif event.key == pygame.K_t:

                Copy = [Souris_x, Souris_y, Brush]
                Presence = False
                for Co in CopyData:
                    if Co[0] == Copy[0] and Co[1] == Copy[1]:
                        Brush = Co[2]       
                        Presence = True
                        break
                if not Presence:
                    break
                
            elif event.key == pygame.K_i:
                if Inv == "Close":
                    Inv = "Open"
                    #print(Inv)
                else:
                    Inv = "Close"
                    #print(Inv)
            elif event.key == pygame.K_KP2:
                InvPage = 2
            elif event.key == pygame.K_KP1:
                InvPage = 1
                
        elif event.type == pygame.KEYUP:
            Deplacement = ""

        elif event.type == pygame.MOUSEMOTION:
            CoordSouris = pygame.mouse.get_pos()
            Souris_x = math.floor(CoordSouris[0] / Background.TailleGrid) * Background.TailleGrid
            Souris_y = math.floor(CoordSouris[1] / Background.TailleGrid) * Background.TailleGrid

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                Sprite = [Souris_x - Axe_x, Souris_y - Axe_y, Brush]
                
                Found = False
                for t in SpriteData:
                    if t[0] == Sprite[0] and t[1] == Sprite[1]:
                        Found = True
                        break

                if not Found:
                    if not Brush == "r":
                        SpriteData.append(Sprite)
                    
                else:
                    if Brush == "r":
                        for t in SpriteData:
                            if t[0] == Sprite[0] and t[1] == Sprite[1]:
                                SpriteData.remove(t)
                                break
                    else:
                        #for t in SpriteData:
                            #if t[0] == Sprite[0] and t[1] == Sprite[1]:
                                #SpriteData.remove(t)
                        SpriteData.append(Sprite)
                        #print("Il y a deja un Sprite ici")
            #if event.button == 4:
                #X += 1
                #Current = Background.DicoTextures[X]
                    
                            
                        
            
    if Deplacement == "haut":
        Axe_y += Background.TailleGrid
    elif Deplacement == "bas":
        Axe_y -= Background.TailleGrid
    elif Deplacement == "gauche":
        Axe_x += Background.TailleGrid
    elif Deplacement == "droite":
        Axe_x -= Background.TailleGrid

    Editeur.fill((120,0,0))

    for Sprite in SpriteData:
        Editeur.blit(Background.DicoTextures[Sprite[2]], (Sprite[0] + Axe_x, Sprite[1] + Axe_y))

    Editeur.blit(Selection, (Souris_x, Souris_y))

    if Inv == "Open":
        Editeur.blit(InvEdit, (0,Background.TailleGrid*15))
        if InvPage == 1:
            CopyDataPage = CopyData
        elif InvPage == 2:
            CopyDataPage = CopyData2
        for CopySprite in CopyDataPage:
            Editeur.blit(Background.DicoTextures[CopySprite[2]], (CopySprite[0], CopySprite[1]))
            pygame.draw.rect(Editeur,(150, 150, 0), (CopySprite[0], CopySprite[1], Background.TailleGrid, Background.TailleGrid), 2)          
            if CopySprite[2] == "Bloc":
                pygame.draw.rect(Editeur,(150, 0, 0), (CopySprite[0], CopySprite[1], Background.TailleGrid, Background.TailleGrid), 2)
            if CopySprite[2] == "Bloc2":
                pygame.draw.rect(Editeur,(0, 0, 150), (CopySprite[0], CopySprite[1], Background.TailleGrid, Background.TailleGrid), 2)
        if Brush != "r":
            Current = Background.DicoTextures[Brush]
        elif Brush == "r":
            Current = Selection
        #elif Brush == "Bloc2":
            #Current = Selection
        Editeur.blit(Current, (Background.TailleGrid*50, Background.TailleGrid*29))
    
    pygame.display.update()

    clock.tick(60)
    
pygame.quit()
sys.exit()
    
