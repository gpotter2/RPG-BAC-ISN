# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *

pygame.init()

Perso = pygame.image.load("Textures/Perso/LeoG/OvLeoG.png")
Current = "Face0"

Gesture = {}
Taille = [64, 64]
TailleX = Taille[0]
TailleY = Taille[1]

Face0 = pygame.Surface(Taille, pygame.HWSURFACE|pygame.SRCALPHA)
Face0.blit(Perso, (0,0), (TailleX*2, TailleY, TailleX*3, TailleY*2))
Gesture["Face0"] = Face0

print(Gesture)

#-----#
Liste = {}
Var = "Face0"
x = 0
for i in range(0, 3):
    x += 1
    Var = Var + "r"
    Liste.append(("Var{} : ".format(x) + Var))
print(Liste)
