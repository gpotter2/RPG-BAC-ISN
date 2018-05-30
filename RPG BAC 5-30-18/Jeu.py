# -*- coding: utf-8 -*-

import pygame, sys, math
from pygame.locals import *

from Textures import *
from Classes import *
from Mapping import *
from PNJs import *
from Menu import *

pygame.init()

def ChargerFenetreJeu():
    
    global Fenetre_Jeu, Hauteur_Jeu, Largeur_Jeu, Titre_Jeu
    
    Hauteur_Jeu, Largeur_Jeu = 600, 800
    Titre_Jeu = "Bac RPG TTS"
    pygame.display.set_caption(Titre_Jeu)
    Fenetre_Jeu = pygame.display.set_mode((Largeur_Jeu, Hauteur_Jeu), HWSURFACE|DOUBLEBUF)

ChargerFenetreJeu()
#---#
#Chambre = Mapping.Charger_Map("maps/ChambreTest.map")
#Salon = Mapping.Charger_Map("maps/SalonTest.map")
AllPortails = {}

AllPortailsFIXE = {
                #Chambre//Salon
                'StairsChambreToSalon' : ('ChambreTest', 'SalonTest', [9, 6], [0, 3]),
                'StairsSalonToChambre' : ('SalonTest', 'ChambreTest', [8, 3], [0, 0]),
                #Salon//Ville de Depart
                'SalonToDepart' : ('SalonTest', 'Foret13', [5, 12], [-16, -5]),
                'SalonToDepart2' : ('SalonTest', 'Foret13', [6, 12], [-16, -5]),
                'DepartToSalon' : ('Foret13', 'SalonTest', [21, 18], [0, 3]),
                'DepartToSalon2' : ('Foret13', 'SalonTest', [22, 18], [0, 3]),
                #Labo//Ville de Depart
                'DepartToLabo' : ('Foret13', 'Labo7', [38, 19], [15, 0]),
                'DepartToLabo2' : ('Foret13', 'Labo7', [39, 19], [15, 0]),
                'LaboToDepart' : ('Labo7', 'Foret13', [7, 16], [-16, -5]),
                'LaboToDepart2' : ('Labo7', 'Foret13', [8, 16], [-16, -5]),
                #RandomHouse//Ville de Depart
                'RandSalonToDepart' : ('randomsalon', 'Foret13', [4, 10], []),
                'RandSalonToDepart2' : ('randomsalon', 'Foret13', [5, 10], []),
                'DepartToRandSalon' : ('Foret13', 'randomsalon', [], []),
                'DepartToRandSalon2' : ('Foret13', 'randomsalon', [], [])
                   }

AllPortails = AllPortailsFIXE
PORT = 1
#---#

MapName = "ChambreTest"
Mapping = MappingClass()
#>>>>>>> ef8fa6c2c155937eeef10c2ca809ec239a5a2849
Map = Mapping.Charger_Map("maps/{}.map".format(MapName))
CurrentMap = "{}".format(MapName)
Terrain = Map[0]
Decor = Map[1]

#---PERSO---#
Nom = "LeoG"
Current = "Face0"
ChoixPerso = 0
Pos_PxFIXE = 0
Pos_PyFIXE = 0
TP = False
#---#

#---DIALOGUE BOX---#
DialogueBox = pygame.image.load("Textures/Detail/DialogueBox.png")
DialogueBox = pygame.transform.scale(DialogueBox, (760, 120))
DialogueSurface = pygame.Surface((760, 150), pygame.HWSURFACE|pygame.SRCALPHA)
DialogueSurface.blit(DialogueBox, (0, 0))
DialogueSurfaceLargeur, DialogueSurfaceHauteur = 760, 150

#---#

#---REDMARK---#
REDMARK = "Close"
#---#

#---PNJs---#
def CharlesARandom():
    Dialogs = [[("l'Aube et le crépuscule...","n'oublie pas..."),("la vie est tel un kinder...","pleine de surprise")], [("Bouh","AAAH")]]
    X = random.randint(0, 1)
    DialogueCharlesA = Dialogs[X]
    return DialogueCharlesA

#CharlesV#
DCharlesV = [("Page 1 Ligne 1", "Page 1 Ligne 2"), ("Page 2 Ligne 1", "")]
#CharlesV = PNJ(Nom = "CharlesV", Pos = (32*14, 32*4), Dialogue = Dialogue(Texte = DCharlesV))
#Ines#
DInes = [("Bonjour Mon Chaton, bien dormi ?", "J'aurais un Bentô pour Ambre, elle se trouve devant l'Autel, elle doit avoir faim."), ("Tu pourrais lui apporter Minou ? Merci d'avance !", "")]
DInes2 = [("Salut Mon Amour ~", "Alors, Ambre a reçu son Bentô ?"), ("*Votre mère retourne dans ses pensées*", "")]
DInes3 = [("Salut Mon Amour ~", "Alors, Ambre est toujours en train de déguster son Bentô ?"), ("*Votre mère retourne dans ses pensées*", "")]
Ines = PNJ(Nom = "Ines", Pos = (32*7, 32*9), Dialogue = Dialogue(Texte = DInes), Surface = "SalonTest")
#Ambre#
DAmbre = [("Bonjour ! Je vois que tu te portes plutot bien ~", "J'adore la nature..."), ("Je pourrais passer des heures à contempler le paysage...", "Pas toi ?")]
DAmbre2 = [("C'est pour moi ça ?", "Tu remercieras ta mère de ma part ! Ca à l'air super bon ! ~"), ("Reviens me voir plus tard si ça te tente !", "")]
DAmbre3 = [("*Ambre est toujours en train de déguster votre Bento...*", "MMMmmmh... Exchellent !")]
Ambre = PNJ(Nom = "Ambre", Pos = (32*25, 32*29), Dialogue = Dialogue(Texte = DAmbre), Surface = "Ambre14")
#Julien#
DJulien1 = [("Ah, Jacques, le grand, le fameux !",""),("Si je te connais ?", "Non bien sûr, ou alors peu."),("J'aime impressionner avec des grands airs.","C'est toujours mieux que la paperasse officielle."),
           ("Je suis bien content que tu sois venu de ton plein gré.","Autrement tu serais venu de force, emballé dans un sac."),("Tu as neutralisé deux de mes Hommes en pleine affaire ...","et je n'aime pas ça."),
           ("D'ailleurs j'ai oublié de me présenter.","Julien Chaussecourte, leader de la Team Chaussecourte."),("On est le gros poisson financier de la région.","Toutes les transaction, légales ou non, passent par nous."),
           ("On est un cartel de drogue si tu veux. Mais, je préfère", "le voir comme une opportunité financière."),("On est tellement riches !","On peut s'offrir la protection du Maire De Lanversin."),("C'est pas beau, ça ?",""),
           ("Le seul obstacle au bon fonctionnement de mon business","..."),("C'est toi.","C'est assez paradoxal que tu cherches autant d'ennuis."),("Si ton frère meurt sous tes yeux, il est peut-être","temps d'arrêter de marcher dans ses pas ...")]

#Julien = PNJ(Nom = "Julien", Pos = (32*25, 32*25), Dialogue = Dialogue(Texte = DJulien1), Surface = "Foret13")
#---#
Pos_P = 0
Dep_PyH, Dep_PyB, Dep_PxD, Dep_PxG = 0, 0, 0, 0

#Pos_Px = (Largeur_Jeu/2 - Modules.Axe_x ) / Background.TailleGrid
#Pos_Py = (Hauteur_Jeu/2 - Modules.Axe_y +25) / Background.TailleGrid
   
Continuer = True

pygame.key.set_repeat(1,10)
while Continuer:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Continuer = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z or event.key == pygame.K_UP and not Modules.DialogueOn:
                Modules.Deplacement = "haut"
                Pos_P = 1
                #Modules.Mouvement('haut')
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN and not Modules.DialogueOn:
                Modules.Deplacement = "bas"
                Pos_P = 2
                #Modules.Mouvement('bas')
            elif event.key == pygame.K_q or event.key == pygame.K_LEFT and not Modules.DialogueOn:
                Modules.Deplacement = "gauche"
                Pos_P = 3
                #Modules.Mouvement('gauche')
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT and not Modules.DialogueOn:
                Modules.Deplacement = "droite"
                Pos_P = 4
                #Modules.Mouvement('droite')
            elif event.key == pygame.K_KP1 and not Modules.DialogueOn:
                REDMARK = "Open"
            elif event.key == pygame.K_KP2 and not Modules.DialogueOn:
                REDMARK = "Close"
            elif event.key == pygame.K_KP3 and not Modules.DialogueOn:
                CurrentMap = input("CurrentMap :")

        elif event.type == pygame.KEYUP:
            
            Modules.Deplacement = ""
            if event.key == pygame.K_p:
                ChoixPerso += 1
                if ChoixPerso == len(Gestuel.Personnages):
                    ChoixPerso = 0
                #Nom = Gestuel.Personnages(ChoixPerso)
                Nom = Gestuel.Personnages[ChoixPerso]

            elif event.key == pygame.K_RETURN:
                if Modules.DialogueOn:
                    if Modules.ActiveDialogue.Page < len(Modules.ActiveDialogue.Texte) - 1:
                        Modules.ActiveDialogue.Page += 1
                    else:
                        Modules.DialogueOn = False
                        Modules.ActiveDialogue.Page = 0
                        Modules.ActiveDialogue = None
                        for npc in NPC.AllNPCs:
                            npc.Current = npc.CurrentInit
                        
                else:
                    for npc in NPC.AllNPCs:
                        NPC_x = npc.X / Background.TailleGrid
                        NPC_y = npc.Y / Background.TailleGrid

                        if Pos_Px >= NPC_x - 1 and Pos_Px <= NPC_x + 2 and Pos_Py >= NPC_y and Pos_Py <= NPC_y + 2 and npc.Surface == CurrentMap:
                            #print("NPC_y", NPC_y)
                            #print("Pos_Py", Pos_Py)

                            #QUEST BEFORE#
                            if npc.Name == "Ambre":
                                if Quest.Bento == 2:
                                    npc.Dialogue = Dialogue(Texte = DAmbre3)
                                    Quest.Bento = 3
                                if Quest.Bento == 1:
                                    npc.Dialogue = Dialogue(Texte = DAmbre2)
                                    Quest.Bento = 2
                            if npc.Name == "Ines":
                                if Quest.Bento == 2 or Quest.Bento == 3:
                                    npc.Dialogue = Dialogue(Texte = DInes3)
                            if npc.Name == "CharlesA":
                                npc.Dialogue = Dialogue(Texte = CharlesARandom())
                                    
                            #DIALOGUE BASE#
                            if Current == "Dos0" and NPC_y > (Pos_Py-2):
                                Modules.DialogueOn = True
                                Modules.ActiveDialogue = npc.Dialogue
                                npc.Current = "Face0"
                            if Current == "Face0" and NPC_y < Pos_Py:
                                Modules.DialogueOn = True
                                Modules.ActiveDialogue = npc.Dialogue
                                npc.Current = "Dos0"
                            if Current == "Gauche0" and NPC_x < Pos_Px:
                                Modules.DialogueOn = True
                                Modules.ActiveDialogue = npc.Dialogue
                                npc.Current = "Droite0"
                            if Current == "Droite0" and NPC_x > Pos_Px:
                                Modules.DialogueOn = True
                                Modules.ActiveDialogue = npc.Dialogue
                                npc.Current = "Gauche0"
                            #---#
                                
                            #QUEST AFTER#
                                
                            if npc.Name == "Ines":
                                if Quest.Maman == 0:
                                    Quest.Maman = 1
                                    Quest.Bento = 1
                                    npc.Dialogue = Dialogue(Texte = DInes2)
                            
                                
                                
                        
    pygame.time.wait(1)
    if Modules.Deplacement == "haut":
        if not Background.Obs((round(Pos_Px+float(0.4)), math.floor(Pos_Py))) and not Background.Obs((round(Pos_Px-float(0.4)), math.floor(Pos_Py))):
            Modules.Axe_y += 1.5
            Modules.Axe_yINIT += 1.5
    elif Modules.Deplacement == "bas":
        if not Background.Obs((round(Pos_Px+float(0.4)), math.ceil(Pos_Py-float(0.3)))) and not Background.Obs((round(Pos_Px-float(0.4)), math.ceil(Pos_Py-float(0.3)))):
            Modules.Axe_y -= 1.5
            Modules.Axe_yINIT -= 1.5
    elif Modules.Deplacement == "gauche":
        if not Background.Obs((math.floor(Pos_Px), round(Pos_Py-float(0.4))))and not Background.Obs((math.floor(Pos_Px), round(Pos_Py+float(0.1)))):
            Modules.Axe_x += 1.5
            Modules.Axe_xINIT += 1.5
    elif Modules.Deplacement == "droite":
        if not Background.Obs((math.ceil(Pos_Px), round(Pos_Py-float(0.4)))) and not Background.Obs((math.ceil(Pos_Px), round(Pos_Py+float(0.1)))):
            Modules.Axe_x -= 1.5
            Modules.Axe_xINIT -= 1.5

    Pos_Px = (Largeur_Jeu/2 - Modules.Axe_x ) / Background.TailleGrid
    Pos_Py = (Hauteur_Jeu/2 - Modules.Axe_y +25) / Background.TailleGrid
    #print(math.ceil(Pos_Px), round(Pos_Py))
    Fenetre_Jeu.fill((0, 0, 0))

    #----PORTAIL----#
    #DicoPortail = {"
    #for Portail in DicoPortail:
            
    #----CREATION MAP----#

        #------------# VERSION COMPLEXE (+Mapping.py)
    #Fenetre_Jeu.blit(Terrain, (Modules.Axe_x, Modules.Axe_y))
    
    
    #-----PERSO-----#
    Gesture = Gestuel.ChargerGesture(Nom)
    LocPerso = [(round(Pos_Px)), math.floor((Pos_Py)+1)]
    LocPerso2 = [(round(Pos_Px)), math.floor(Pos_Py)+2]
    LocPerso3 = [(round(Pos_Px)), math.floor((Pos_Py))]
    LocPerso4 = [(round(Pos_Px)), math.floor(Pos_Py)-1]

    for Portail in AllPortails.values():
        if LocPerso3 == Portail[2] and CurrentMap == Portail[0]:
            CurrentMap = Portail[1]
            Background.Obstacle = []
            Mapping.ObstacleDecor = []
            Background.ObstaclePNJ = []
            Mapping.DecorListe = []
            Modules.Diff = Portail[3]
            #print(LocPerso3)
            #print(Modules.Diff)
            Modules.Axe_x = Modules.Axe_xINIT + Modules.Diff[0]*Background.TailleGrid
            #print(Modules.Axe_x, Modules.Axe_xINIT)
            Modules.Axe_y = Modules.Axe_yINIT + Modules.Diff[1]*Background.TailleGrid
            #print(Modules.Axe_y, Modules.Axe_yINIT)
            Map = Mapping.Charger_Map("maps/{}.map".format(CurrentMap))
            Terrain = Map[0]
            #Decor = Map[1]

    LocPerso = [(round(Pos_Px)), math.floor((Pos_Py)+1)]
    LocPerso2 = [(round(Pos_Px)), math.floor(Pos_Py)+2]
    LocPerso3 = [(round(Pos_Px)), math.floor((Pos_Py))]
    LocPerso4 = [(round(Pos_Px)), math.floor(Pos_Py)-1]
            
    Fenetre_Jeu.blit(Terrain, (Modules.Axe_x, Modules.Axe_y))
    #print(Modules.Axe_y, Pos_PyFIXE)
    
    #LocPerso3 = [(round(Pos_Px)), math.floor(Pos_Py)]
    #print(LocPerso, LocPerso2, LocPerso3)
    #print(Gesture[Current])
    #print("A", LocPerso2)
    #print("B", LocPerso)
    #Fenetre_Jeu.blit(Gesture[Current], (Largeur_Jeu/2 -16, Hauteur_Jeu/2 -16))
    
    if Modules.Deplacement == "haut":
        if  0<Dep_PyH<25:
            Current = "Dos1"
        elif 25<Dep_PyH<50:
            Current = "Dos0"
        elif 50<Dep_PyH<75:
            Current = "Dos2"
        elif 75<Dep_PyH<100:
            Current = "Dos0"
        else:
            Current = "Dos0"
            if Dep_PyH >= 100:
                Dep_PyH -= 100
        Dep_PyH += float(0.7)

    
    elif Modules.Deplacement == "bas":
        if 0<Dep_PyB<25:
            Current = "Face1"
        elif 25<Dep_PyB<50:
            Current = "Face0"
        elif 50<Dep_PyB<75:
            Current = "Face2"
        elif 75<Dep_PyB<100:
            Current = "Face0" 
        else:
            Current = "Face0"
            if Dep_PyB >= 100:
                Dep_PyB -= 100
        Dep_PyB += float(0.7)
        
    elif Modules.Deplacement == "gauche":

        if 0<Dep_PxG<25:
            Current = "Gauche1"
        elif 25<Dep_PxG<50:
            Current = "Gauche0"
        elif 50<Dep_PxG<75:
            Current = "Gauche2" 
        elif 75<Dep_PxG<100:
            Current = "Gauche0" 
        else:
            Current = "Gauche0"
            if Dep_PxG >= 100:
                Dep_PxG -= 100
        Dep_PxG += float(0.7)
        
    elif Modules.Deplacement == "droite":
        
        if 0<Dep_PxD<25:
            Current = "Droite1"
        elif 25<Dep_PxD<50:
            Current = "Droite0"
        elif 50<Dep_PxD<75:
            Current = "Droite2"
        elif 75<Dep_PxD<100:
            Current = "Droite0"
        else:
            Current = "Droite0"
            if Dep_PxD >= 100:
                Dep_PxD -= 100
        Dep_PxD += float(0.7)
        #print(Dep_PxD)

    else:
        Dep_PxD = 0
        Dep_PyB = 0
        Dep_PxG = 0
        Dep_PyH = 0
        
        if Pos_P == 1:
            Current = "Dos0"

        elif Pos_P == 2:
            Current = "Face0"
            
        elif Pos_P == 3:
            Current = "Gauche0"

        elif Pos_P == 4:
            Current = "Droite0"
            
    if not LocPerso3 in Background.ObstaclePNJ and not LocPerso4 in Background.ObstaclePNJ:
        Fenetre_Jeu.blit(Gesture[Current], (Largeur_Jeu/2 -16, Hauteur_Jeu/2 -16))
        
    
    #---#

    #PNJs#
    
    if LocPerso in Mapping.ObstacleDecor or LocPerso2 in Mapping.ObstacleDecor:
        
        for Sprite in Mapping.DecorListe:
            Pos_Decor = Sprite[0]
                 
                #print(LocPerso, Sprite[0])
            Mapping.AjouterDecor(Background.DicoDecors[Sprite[1]], (Pos_Decor[0]+Modules.Axe_x/Background.TailleGrid, Pos_Decor[1]+Modules.Axe_y/Background.TailleGrid), Fenetre_Jeu)
    
    for npc in NPC.AllNPCs:
        if npc.Surface == CurrentMap:
            npc.Render(Fenetre_Jeu)
    

    if LocPerso3 in Background.ObstaclePNJ or LocPerso4 in Background.ObstaclePNJ:
        Fenetre_Jeu.blit(Gesture[Current], (Largeur_Jeu/2 -16, Hauteur_Jeu/2 -16))
    
    #---#
    
    if REDMARK == "Open":
        for t in Mapping.ObstacleDecor:
            pygame.draw.rect(Fenetre_Jeu, (0,0,150), (t[0]*Background.TailleGrid + Modules.Axe_x, t[1]*Background.TailleGrid + Modules.Axe_y, Background.TailleGrid, Background.TailleGrid), 3)
        for t in AllPortails.values():
            POS = t[2]
            print(POS)
            pygame.draw.rect(Fenetre_Jeu, (150,0,150), (POS[0]*Background.TailleGrid + Modules.Axe_x, POS[1]*Background.TailleGrid + Modules.Axe_y, Background.TailleGrid, Background.TailleGrid), 4)
        for t in Background.Obstacle:
            pygame.draw.rect(Fenetre_Jeu, (150,0,0), (t[0]*Background.TailleGrid + Modules.Axe_x, t[1]*Background.TailleGrid + Modules.Axe_y, Background.TailleGrid, Background.TailleGrid), 5)
        for t in Background.ObstaclePNJ:
            pygame.draw.rect(Fenetre_Jeu, (150,150,0), (t[0]*Background.TailleGrid + Modules.Axe_x, t[1]*Background.TailleGrid + Modules.Axe_y, Background.TailleGrid, Background.TailleGrid), 5)
            
        #------------# VERSION INTERMEDIAIRE
    #for X in range(0, 640, TailleGrid):
        #for Y in range(0, 480, TailleGrid):
            #for Decor in MapData:
                #TileSprite = (Decor[0] * Background.TailleGrid, Decor[1] * Background.TailleGrid)
                #if (X, Y) == TileSprite:
                    #Fenetre_Jeu.blit(Background.DicoTextures[Decor[2]], (X + Modules.Axe_x, Y + Modules.Axe_y))
        #------------# VERSION SIMPLE
            #Fenetre_Jeu.blit(Background.SolVille, (X + Modules.Axe_x, Y + Modules.Axe_y))
    #DIALOGUE BOX & TEXTE#
    if Modules.DialogueOn:
        Fenetre_Jeu.blit(DialogueSurface, (20, Hauteur_Jeu - DialogueSurfaceHauteur + 15))

    if Modules.ActiveDialogue != None:
        Lignes = Modules.ActiveDialogue.Texte[Modules.ActiveDialogue.Page]

        for Ligne in Lignes:
            Fenetre_Jeu.blit(pygame.font.Font("Font/DTM-Sans.otf", 26).render(Ligne, True, (0, 0, 0)), (50, (Hauteur_Jeu - DialogueSurfaceHauteur) + 33 + (Lignes.index(Ligne)) * 45))
    NPC.Done = True  
    pygame.display.update()


pygame.quit()
sys.exit()
    
