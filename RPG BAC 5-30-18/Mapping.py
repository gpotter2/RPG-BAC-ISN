# -*- coding: utf-8 -*-

import pygame
from Textures import *
from Classes import *
import math

class Mapping:

    DecorListe = []
    ObstacleDecor = []
    
    def AjouterDecor(Texture, Coord, Zone):
        Zone.blit(Texture,(Coord[0]* Background.TailleGrid, Coord[1]* Background.TailleGrid))
    
    def Charger_Map(Fichier):
        with open(Fichier, "r") as FichierMap:
            Map_Data = FichierMap.read()
        #Data = open(Fichier, mode="r").readlines()

        Map_Data = Map_Data.split("-")

        Taille_Map = Map_Data[len(Map_Data)-1]
        Map_Data.remove(Taille_Map)
        Taille_Map = Taille_Map.replace("\n", "")
        Taille_Map = Taille_Map.split(",")
        Taille_Map[0] = (int(Taille_Map[0])+1)*Background.TailleGrid
        Taille_Map[1] = (int(Taille_Map[1])+1)*Background.TailleGrid
        

        Sprites = []

        for Sprite in range(len(Map_Data)):
            Map_Data[Sprite] = Map_Data[Sprite].replace("\n", "")
            Sprites.append(Map_Data[Sprite].split(":"))
            
        for Sprite in Sprites:
            Sprite[0] = Sprite[0].split(",")
            Coord = Sprite[0]

            for p in Coord:
                Coord[Coord.index(p)] = int(p)

            Sprites[Sprites.index(Sprite)] = (Coord, Sprite[1])

        Terrain = pygame.Surface(Taille_Map, pygame.HWSURFACE)
        Decor = pygame.Surface(Taille_Map, pygame.HWSURFACE)

        for Sprite in Sprites:
            if Sprite[1] in Background.DicoTextures:
                Mapping.AjouterDecor(Background.DicoTextures[Sprite[1]], Sprite[0], Terrain)
                
            if Sprite[1] in Background.DicoDecorsOBSTACLE:
                Loc = Sprite[0]
                LocationA = [int(Loc[0]), int((Loc[1]+1))]
                
                if not LocationA in Mapping.ObstacleDecor:
                    Mapping.ObstacleDecor.append(LocationA)
            if Sprite[1] in Background.DicoDecors:
                Mapping.DecorListe.append(Sprite)
            if Sprite[1] in Background.ObstaclesListe:
                Loc = Sprite[0]
                PosObstacle = [Loc[0], Loc[1]]
                Background.Obstacle.append(PosObstacle)

        #print(Mapping.ObstacleDecor)
        return (Terrain, Decor)


                              





        
