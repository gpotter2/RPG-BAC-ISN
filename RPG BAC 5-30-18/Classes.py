# -*- coding: utf-8 -*-

import pygame
from Save import *

class SDict(dict):
    """
    Fait qu'on peut faire aussi bien
    
    a = SDict()
        a.b = 0
    que
        a["b"] = 0
    """
    def __getattr__(self, attr):
        return self[attr]
    def __setattr__(self, attr, valeur):
        self[attr] = valeur

class ModulesClass(SDict):

    def __init__(self, *args):
        super(ModulesClass, self).__init__(*args)

    def default(self):
        #global Axe_y, Axe_x
        self.Axe_y = -5
        self.Axe_x = 255
        self.Axe_xINIT = 255
        self.Axe_yINIT = -5
        self.Deplacement = ""

        self.DialogueOn = False
        self.ActiveDialogue = None

        self.Diff_x = 0
        self.Diff_y = 0
        
        #---PNJ---#
        #---#
        
        #if direction == 'haut':
            #self.Axe_y += 1
        #elif direction == 'bas':
            #self.Axe_y -= 1
       # elif direction == 'gauche':
            #self.Axe_x -= 1
        #elif direction == 'droite':
            #self.Axe_x += 1

        #return self.Axe_x, self.Axe_y

class QuestClass(SDict):

    def __init__(self, *args):
        super(QuestClass, self).__init__(*args)

    def default(self):
        #Maison Perso#
        self.Maman = 0
        self.Bento = 0
        #Premier Village#
        #Labo#
        self.Fabien = False

class MapClass(SDict):

    def __init__(self, *args):
        super(MapClass, self).__init__(*args)

    def default(self):
        self.CurrentMapName = "ChambreTest"
### CHARGER ###

#---QUEST---#
Fichier_sauvegarde = "Save/sauvegarde.json"
try:
    Quest = QuestClass(charger_fichier(Fichier_sauvegarde))
except (OSError, IOError):  # Pas de sauvegarde
    Quest = QuestClass()
    Quest.default()

#---MODULES---#
Fichier_sauvegarde_module = "Save/sauvegarde_module.json"
try:
    Modules = ModulesClass(charger_fichier(Fichier_sauvegarde_module))
except (OSError, IOError):  # Pas de sauvegarde
    Modules = ModulesClass()
    Modules.default()
#---MAP---#
Fichier_sauvegarde_Map = "Save/sauvegarde_map.json"
try:
    Maps = MapClass(charger_fichier(Fichier_sauvegarde_Map))
except (OSError, IOError):
    Maps = MapClass()
    Maps.default()
