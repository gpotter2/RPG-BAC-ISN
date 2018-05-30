# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *



pygame.init()

class Background:
    
    TailleGrid = 32

    #---OBSTACLE---#
    Obstacle = []
    ObstaclePNJ = []
    ObstaclesListe = ["Bloc", "2", "2BD", "2HG", "2HB", "2BG", "2B", "2H", "2D", "2G", "2N1", "2N2", "2N3", "2cHG", "2cHD", "2cBD", "2cBG",
                      "3BD", "3BG","3HG", "3HD", "4", "4TG", "4TD", "4H", "4B", "4D", "4G", "4HD", "4HG", "4BD", "4BG",
                      "Pierre1", "Pierre2"]

    def Obs(Pos):
        if list(Pos) in Background.Obstacle or list(Pos) in Background.ObstaclePNJ:
            return True
        else:
            return False
        
    def Textures(Fichier, Taille1, Taille2):
        Grid = pygame.image.load(Fichier)
        Grid = pygame.transform.scale(Grid, (Taille1, Taille2))
        surface = pygame.Surface((Taille1, Taille2), HWSURFACE|SRCALPHA)
        surface.blit(Grid, (0, 0))
        return surface
    #----------TEXTURES TILES----------#
    #---SOL VILLE---#
    SolVille = Textures("Textures/SolVille/SolVille.png", TailleGrid, TailleGrid)
    SolVilleHD = Textures("Textures/SolVille/SolVilleHD.png", TailleGrid, TailleGrid)
    SolVilleHG = Textures("Textures/SolVille/SolVilleHG.png", TailleGrid, TailleGrid)
    SolVilleBG = Textures("Textures/SolVille/SolVilleBG.png", TailleGrid, TailleGrid)
    SolVilleBD = Textures("Textures/SolVille/SolVilleBD.png", TailleGrid, TailleGrid)
    SolVilleCoinHD = Textures("Textures/SolVille/SolVilleCoinHD.png", TailleGrid, TailleGrid)
    SolVilleCoinHG = Textures("Textures/SolVille/SolVilleCoinHG.png", TailleGrid, TailleGrid)
    SolVilleCoinBG = Textures("Textures/SolVille/SolVilleCoinBG.png", TailleGrid, TailleGrid)
    SolVilleCoinBD = Textures("Textures/SolVille/SolVilleCoinBD.png", TailleGrid, TailleGrid)
    SolVilleBordH = Textures("Textures/SolVille/SolVilleBordH.png", TailleGrid, TailleGrid)
    SolVilleBordB = Textures("Textures/SolVille/SolVilleBordB.png", TailleGrid, TailleGrid)
    SolVilleBordG = Textures("Textures/SolVille/SolVilleBordG.png", TailleGrid, TailleGrid)
    SolVilleBordD = Textures("Textures/SolVille/SolVilleBordD.png", TailleGrid, TailleGrid)

    #---LAC---#
    Lac = Textures("Textures/Lac/Lac.png", TailleGrid, TailleGrid)
    LacBD = Textures("Textures/Lac/LacBD.png", TailleGrid, TailleGrid)
    LacBG = Textures("Textures/Lac/LacBG.png", TailleGrid, TailleGrid)
    LacHD = Textures("Textures/Lac/LacHD.png", TailleGrid, TailleGrid)
    LacHG = Textures("Textures/Lac/LacHG.png", TailleGrid, TailleGrid)
    LacBordB = Textures("Textures/Lac/LacBordB.png", TailleGrid, TailleGrid)
    LacBordH = Textures("Textures/Lac/LacBordH.png", TailleGrid, TailleGrid)
    LacBordG = Textures("Textures/Lac/LacBordG.png", TailleGrid, TailleGrid)
    LacBordD = Textures("Textures/Lac/LacBordD.png", TailleGrid, TailleGrid)
    LacCoinBD = Textures("Textures/Lac/LacCoinBD.png", TailleGrid, TailleGrid)
    LacCoinBG = Textures("Textures/Lac/LacCoinBG.png", TailleGrid, TailleGrid)
    LacCoinHD = Textures("Textures/Lac/LacCoinHD.png", TailleGrid, TailleGrid)
    LacCoinHG = Textures("Textures/Lac/LacCoinHG.png", TailleGrid, TailleGrid)
    LacN1 = Textures("Textures/Lac/LacN1.png", TailleGrid, TailleGrid)
    LacN2 = Textures("Textures/Lac/LacN2.png", TailleGrid, TailleGrid)
    LacN3 = Textures("Textures/Lac/LacN3.png", TailleGrid, TailleGrid)
    #----------#

    #---HERBE---#
    Herbe = Textures("Textures/Herbe/Herbe.png", TailleGrid, TailleGrid)
    HerbeFosseBD = Textures("Textures/Herbe/Herbe_Fosse_BD.png", TailleGrid, TailleGrid)
    HerbeFosseBG = Textures("Textures/Herbe/Herbe_Fosse_BG.png", TailleGrid, TailleGrid)
    HerbeFosseHD = Textures("Textures/Herbe/Herbe_Fosse_HD.png", TailleGrid, TailleGrid)
    HerbeFosseHG = Textures("Textures/Herbe/Herbe_Fosse_HG.png", TailleGrid, TailleGrid)
    MontagneB = Textures("Textures/Herbe/Montagne_B.png", TailleGrid, TailleGrid)
    MontagneH = Textures("Textures/Herbe/Montagne_H.png", TailleGrid, TailleGrid)
    MontagneD = Textures("Textures/Herbe/Montagne_D.png", TailleGrid, TailleGrid)
    MontagneG = Textures("Textures/Herbe/Montagne_G.png", TailleGrid, TailleGrid)
    MontagneBD = Textures("Textures/Herbe/Montagne_BD.png", TailleGrid, TailleGrid)
    MontagneBG = Textures("Textures/Herbe/Montagne_BG.png", TailleGrid, TailleGrid)
    MontagneHD = Textures("Textures/Herbe/Montagne_HD.png", TailleGrid, TailleGrid)
    MontagneHG = Textures("Textures/Herbe/Montagne_HG.png", TailleGrid, TailleGrid)
    TrouD = Textures("Textures/Herbe/Trou_D.png", TailleGrid, TailleGrid)
    TrouG = Textures("Textures/Herbe/Trou_G.png", TailleGrid, TailleGrid)
    
    #----------MAISONS----------#
    #---ZONE AMBRE---#
    Temizuya = Textures("Textures/Maisons/Temizuya.png", 82*2, 102*2)
    Shrine = Textures("Textures/Maisons/Shrine.png", 134*2, 128*2)
    Sapin1 = Textures("Textures/Arbres/Sapin1.png", 48*2, 48*2)
    Sapin2 = Textures("Textures/Arbres/Sapin2.png", 53*2, 69*2)
    Sapin1Sha = Textures("Textures/Arbres/Sapin1Sha.png", 48*2, 48*2)
    Sapin2Sha = Textures("Textures/Arbres/Sapin2Sha.png", 53*2, 69*2)
    Champignon = Textures("Textures/Arbres/Champignon.png", TailleGrid, TailleGrid)
    Arbuste1 = Textures("Textures/Arbres/Arbuste1.png", TailleGrid*2, TailleGrid*3)
    Arbuste1Sha = Textures("Textures/Arbres/Arbuste1Sha.png", TailleGrid*2, TailleGrid*3)
    HerbeMoyenne = Textures("Textures/Arbres/HerbeMoyenne.png", TailleGrid, TailleGrid)
    FleurBlanche = Textures("Textures/Arbres/Fleur1.png", TailleGrid, TailleGrid)
    FleurRouge = Textures("Textures/Arbres/Fleur2.png", TailleGrid, TailleGrid)
    Pierre1 = Textures("Textures/Rochers/Pierre1.png", TailleGrid, TailleGrid)
    Pierre2 = Textures("Textures/Rochers/Pierre2.png", TailleGrid, TailleGrid)
    Rocher1 = Textures("Textures/Rochers/Rocher1.png", TailleGrid*2, TailleGrid*2)
    Rocher1Sha = Textures("Textures/Rochers/Rocher1Sha.png", TailleGrid*2, TailleGrid*2)
    Rocher1EAU = Textures("Textures/Rochers/Rocher1Eau.png", TailleGrid*2, TailleGrid*2)
    TemizuyaWithout = Textures("Textures/Maisons/TemizuyaSha.png", 82*2, 102*2)
    ShrineWithout = Textures("Textures/Maisons/ShrineSha.png", 134*2, 128*2)
    PontH = Textures("Textures/DecorVille/PontHaut.png", TailleGrid*3, TailleGrid)
    #-----ISLA DE LA MUERTA-----#

    Montagne_sable1 = Textures("Textures/Isla_de_la_muerta/Montagne_sable_B.png", TailleGrid, TailleGrid)
    Montagne_sable2 = Textures("Textures/Isla_de_la_muerta/Montagne_sable_BD.png", TailleGrid, TailleGrid)
    Montagne_sable3 = Textures("Textures/Isla_de_la_muerta/Montagne_sable_BD.png", TailleGrid, TailleGrid)
    Montagne_sable4 = Textures("Textures/Isla_de_la_muerta/Montagne_sable_D.png", TailleGrid, TailleGrid)
    Montagne_sable5 = Textures("Textures/Isla_de_la_muerta/Montagne_sable_HD.png", TailleGrid, TailleGrid)
    Montagne_sable6 = Textures("Textures/Isla_de_la_muerta/Montagne_sable_HG.png", TailleGrid, TailleGrid)
    Montagne_sable7 = Textures("Textures/Isla_de_la_muerta/Montagne_sable_G.png", TailleGrid, TailleGrid)
    Montagne_sable8 = Textures("Textures/Isla_de_la_muerta/Montagne_sable_H.png", TailleGrid, TailleGrid)

    GMontagne_sable1 = Textures("Textures/Isla_de_la_muerta/Gmontagnes_B.png", TailleGrid, TailleGrid)
    GMontagne_sable2 = Textures("Textures/Isla_de_la_muerta/Gmontagnes_B2.png", TailleGrid, TailleGrid)
    GMontagne_sable3 = Textures("Textures/Isla_de_la_muerta/Gmontagnes_B3.png", TailleGrid, TailleGrid)
    GMontagne_sable4 = Textures("Textures/Isla_de_la_muerta/Gmontagnes_B4.png", TailleGrid, TailleGrid)
    GMontagne_sable5 = Textures("Textures/Isla_de_la_muerta/Gmontagnes_BD.png", TailleGrid, TailleGrid)
    GMontagne_sable6 = Textures("Textures/Isla_de_la_muerta/Gmontagnes_BG.png", TailleGrid, TailleGrid)
    GMontagne_sable7 = Textures("Textures/Isla_de_la_muerta/Gmontagnes_G.png", TailleGrid, TailleGrid)
    GMontagne_sable8 = Textures("Textures/Isla_de_la_muerta/Gmontagnes_G2.png", TailleGrid, TailleGrid)
    GMontagne_sable9 = Textures("Textures/Isla_de_la_muerta/Gmontagnes_G3.png", TailleGrid, TailleGrid)
    GMontagne_sable10 = Textures("Textures/Isla_de_la_muerta/Gmontagnes_HD.png", TailleGrid, TailleGrid)
    GMontagne_sable11 = Textures("Textures/Isla_de_la_muerta/Gmontagnes_HD2.png", TailleGrid, TailleGrid)
    GMontagne_sable12 = Textures("Textures/Isla_de_la_muerta/Gmontagnes_HG.png", TailleGrid, TailleGrid)
    GMontagne_sable13 = Textures("Textures/Isla_de_la_muerta/Gmontagnes_HG2.png", TailleGrid, TailleGrid)
    GMontagne_sable14 = Textures("Textures/Isla_de_la_muerta/Gmontagnes_D.png", TailleGrid, TailleGrid)
    GMontagne_sable15 = Textures("Textures/Isla_de_la_muerta/Gmontagnes_D2.png", TailleGrid, TailleGrid)
    GMontagne_sable16 = Textures("Textures/Isla_de_la_muerta/Gmontagnes_D3.png", TailleGrid, TailleGrid)

    Sable = Textures("Textures/Isla_de_la_muerta/Sable.png", TailleGrid, TailleGrid)
    Plage1 = Textures("Textures/Isla_de_la_muerta/Plage1.png", TailleGrid, TailleGrid)
    Plage2 = Textures("Textures/Isla_de_la_muerta/Plage2.png", TailleGrid, TailleGrid)
    Plage3 = Textures("Textures/Isla_de_la_muerta/Plage3.png", TailleGrid, TailleGrid)
    Plage4 = Textures("Textures/Isla_de_la_muerta/Plage4.png", TailleGrid, TailleGrid)
    Plage5 = Textures("Textures/Isla_de_la_muerta/Plage5.png", TailleGrid, TailleGrid)
    Plage6 = Textures("Textures/Isla_de_la_muerta/Plage6.png", TailleGrid, TailleGrid)
    Plage7 = Textures("Textures/Isla_de_la_muerta/Plage7.png", TailleGrid, TailleGrid)
    Plage8 = Textures("Textures/Isla_de_la_muerta/Plage8.png", TailleGrid, TailleGrid)
    Plage9 = Textures("Textures/Isla_de_la_muerta/Plage9.png", TailleGrid, TailleGrid)
    Plage10 = Textures("Textures/Isla_de_la_muerta/Plage10.png", TailleGrid, TailleGrid)
    Plage11 = Textures("Textures/Isla_de_la_muerta/Plage11.png", TailleGrid, TailleGrid)
    Plage12 = Textures("Textures/Isla_de_la_muerta/Plage12.png", TailleGrid, TailleGrid)
    Plage13 = Textures("Textures/Isla_de_la_muerta/Plage13.png", TailleGrid, TailleGrid)
    
    Bateau1 = Textures("Textures/Isla_de_la_muerta/Bateau1.png", TailleGrid*15, TailleGrid*5)
    Coquillage = Textures("Textures/Isla_de_la_muerta/Coquillage.png", TailleGrid, TailleGrid)
    Herbe_sable = Textures("Textures/Isla_de_la_muerta/Herbe_sable.png", TailleGrid, TailleGrid)
    Noix = Textures("Textures/Isla_de_la_muerta/Noix.png", TailleGrid, TailleGrid)
    Palmier = Textures("Textures/Isla_de_la_muerta/Palmier.png", TailleGrid*2, 36*2)
    Para = Textures("Textures/Isla_de_la_muerta/Para.png", TailleGrid*2, 36*2)
    Pierre = Textures("Textures/Isla_de_la_muerta/Pierre.png", TailleGrid, TailleGrid)
    Roche = Textures("Textures/Isla_de_la_muerta/Roche.png", TailleGrid*2, 36*2)

    #----------Labo---------#

    Carelage = Textures("Textures/Labo/Carelage.png", TailleGrid, TailleGrid)
    Mur_lab1 = Textures("Textures/Labo/Mur_lab1.png", TailleGrid, TailleGrid*2)
    Mur_lab2 = Textures("Textures/Labo/Mur_lab2.png", TailleGrid, TailleGrid*2)
    Mur_lab3 = Textures("Textures/Labo/Mur_lab3.png", TailleGrid, TailleGrid*2)
    Mur_lab4 = Textures("Textures/Labo/Mur_lab4.png", TailleGrid, TailleGrid*2)
    Serveur  = Textures("Textures/Labo/Serveur.png", TailleGrid, TailleGrid*2)
    Vitrine_lab  = Textures("Textures/Labo/Vitrine.png", TailleGrid*2, 36*2)
    
    #---HOUSING CHAMBRE---#
    SolChambre = Textures("Textures/Interieur/Housing/Sol.png", TailleGrid, TailleGrid)
    SolChambreOmbre = Textures("Textures/Interieur/Housing/SolOmbre.png", TailleGrid, TailleGrid)
    SolChambreOmbreCoin = Textures("Textures/Interieur/Housing/SolOmbreCoin.png", TailleGrid, TailleGrid)
    SolChambreOmbreG = Textures("Textures/Interieur/Housing/SolOmbreG.png", TailleGrid, TailleGrid)
    SolChambreOmbreH = Textures("Textures/Interieur/Housing/SolOmbreHaut.png", TailleGrid, TailleGrid)
    MaisonFRESQUE = Textures("Textures/Interieur/Housing/Maison_H.png", TailleGrid*10, TailleGrid*4)

    #---HOUSING MEUBLES---#
    BibliothequeVerte = Textures("Textures/Interieur/Housing/Biblio1.png", TailleGrid*2, TailleGrid*2)
    BibliothequeMarron = Textures("Textures/Interieur/Housing/Biblio2.png", TailleGrid*2, TailleGrid*2)
    Vitrine = Textures("Textures/Interieur/Housing/Vitrine32x33.png", TailleGrid*2, (TailleGrid*2+1))
    Panneau = Textures("Textures/Interieur/Housing/Panneau.png", TailleGrid, TailleGrid)
    Fleur_Pot = Textures("Textures/Interieur/Housing/Fleur_Pot.png", TailleGrid, TailleGrid)
    Fenetre_Petite = Textures("Textures/Interieur/Housing/Fenetre_Petite.png", TailleGrid, TailleGrid)
    Horloge = Textures("Textures/Interieur/Housing/Horloge.png", TailleGrid, TailleGrid)
    Dossier = Textures("Textures/Interieur/Housing/Dossier.png", TailleGrid, TailleGrid)
    Lavabo = Textures("Textures/Interieur/Housing/Lavabo.png", TailleGrid*2, TailleGrid*2)
    Bureau = Textures("Textures/Interieur/Housing/Bureau.png", TailleGrid*2, TailleGrid*2)
    TV = Textures("Textures/Interieur/Housing/TV.png", TailleGrid*2, TailleGrid*2)
    Plante = Textures("Textures/Interieur/Housing/Plante.png", TailleGrid, TailleGrid*2)
    Machine = Textures("Textures/Interieur/Housing/Machine.png", TailleGrid, TailleGrid*2)
    Frigo = Textures("Textures/Interieur/Housing/Frigo.png", TailleGrid, TailleGrid*2)
    Bar = Textures("Textures/Interieur/Housing/Bar.png", 47*2, 40)
    StairsUp = Textures("Textures/Interieur/Housing/Escalier_H.png", TailleGrid*2, 80)
    StairsDown = Textures("Textures/Interieur/Housing/Escalier_B.png", TailleGrid*2, 80)
    Wii = Textures("Textures/Interieur/Housing/Wii.png", TailleGrid, TailleGrid)
    TapisRouge = Textures("Textures/Interieur/Housing/TapisROuge.png", TailleGrid*4, TailleGrid*3)
    Lit = Textures("Textures/Interieur/Housing/Lit.png", TailleGrid*2, TailleGrid*3)
    Couette = Textures("Textures/Interieur/Housing/Couette.png", TailleGrid*2, TailleGrid*2)
    Tabouret = Textures("Textures/Interieur/Housing/Tabouret.png", TailleGrid, TailleGrid)
    CoussinViolet = Textures("Textures/Interieur/Housing/Coussin_Violet.png", TailleGrid, TailleGrid)
    Table = Textures("Textures/Interieur/Housing/Table.png", TailleGrid*2, 36*2)
    EXIT = Textures("Textures/Interieur/Housing/EXIT.png", TailleGrid*2, TailleGrid*2)
    Mur1 = Textures("Textures/Interieur/Housing/Mur_Bleu1.png", TailleGrid, TailleGrid*2)
    Mur2 = Textures("Textures/Interieur/Housing/Mur_Bleu2.png", TailleGrid, TailleGrid*2)
    Mur3 = Textures("Textures/Interieur/Housing/Mur_Bleu3.png", TailleGrid, TailleGrid*2)
    Mur4 = Textures("Textures/Interieur/Housing/Mur_Bleu4.png", TailleGrid, TailleGrid*2)
    #----------#

    #----------ARBRES---------#
    Arbre = Textures("Textures/Arbres/Arbre.png", TailleGrid*3, TailleGrid*3)
    ArbreSha = Textures("Textures/Arbres/ArbreSha.png", TailleGrid*3, TailleGrid*3)
    #----------#

    #---------Hotel---------#

    Solhotel = Textures("Textures/Hotel/Solhotel.png", TailleGrid, TailleGrid)
    Solhotel2 = Textures("Textures/Hotel/Solhotel2.png", TailleGrid, TailleGrid)
    Esca = Textures("Textures/Hotel/esca.png", TailleGrid*2, TailleGrid)
    Lavabo = Textures("Textures/Hotel/lavabo.png", TailleGrid*2, TailleGrid*2)
    Toilet = Textures("Textures/Hotel/toilet.png", TailleGrid, TailleGrid*2)

    #-------Team Verichon------#
    Statue = Textures("Textures/VERICHON/Statue.png", TailleGrid*2, TailleGrid*2)

    #----------Eglise----------#
    Autel = Textures("Textures/Eglise/Autel.png", TailleGrid*2, TailleGrid*2)
    Banc = Textures("Textures/Eglise/Banc.png", TailleGrid*3, TailleGrid)
    Flambeau = Textures("Textures/Eglise/Flambeau.png", TailleGrid, TailleGrid*3)
    Mureglise = Textures("Textures/Eglise/Mureglise.png", TailleGrid, TailleGrid*2)
    Vitrail1 = Textures("Textures/Eglise/Vitrail1.png", TailleGrid, TailleGrid*2)
    Vitrail2 = Textures("Textures/Eglise/Vitrail2.png", TailleGrid*2, TailleGrid*2)

    #---BATIMENTS VILLES---#
    QGVerichon = Textures("Textures/Maisons/QGVerichon.png", 128, 128)
    MaisonDepart = Textures("Textures/Maisons/MaisonDepart.png", 170, 170)
    Eglise = Textures("Textures/Maisons/Eglise.png", 212, 380)
    LaboDepart = Textures("Textures/Maisons/LaboDepart.png", 127*2, 85*2)
    #Hotel = Textures("Textures/Maisons/Eglise.png", 212, 380)
    #---DIVERS SPECIAL---#
    #POINT = A16("Textures/SolVille/POINT.png", TailleGrid16)
    BLOC = Textures("Textures/Detail/Bloc.png", TailleGrid, TailleGrid)
    Noir = Textures("Textures/Detail/Noir.png", TailleGrid, TailleGrid)
    BLOCPROFONDEUR = Textures("Textures/Detail/Bloc.png", TailleGrid, TailleGrid)

    #----------PERSO----------#
    #-----JOUEUR-----#
    
    
    #-------------DICTIONNAIRE DES TILES-------------#
    DicoTextures = {#---IMPORTANT---#
                    "Bloc" : BLOC, "NOIR" : Noir,

                    #---SOLS---#
                    "1" : SolVille, "1HD" : SolVilleHD, "1HG" : SolVilleHG, "1BG" : SolVilleBG, "1BD" : SolVilleBD,
                    "1cHD" : SolVilleCoinHD, "1cHG" : SolVilleCoinHG, "1cBD" : SolVilleCoinBD, "1cBG" : SolVilleCoinBG,
                    "1bH" : SolVilleBordH, "1bG" : SolVilleBordG, "1bB" : SolVilleBordB, "1bD" : SolVilleBordD,
                    "2" : Lac, "2SPECIAL" : Lac, "2BD" : LacBD , "2BG" : LacBG , "2HD" : LacHD , "2HG" : LacHG, "2H" : LacBordH, "2HSPECIAL" : LacBordH, "2B" : LacBordB, "2BSPECIAL" : LacBordB,
                    "2D" : LacBordD, "2G" : LacBordG, "2cHG" : LacCoinHG, "2cHD" : LacCoinHD, "2cBG" : LacCoinBG, "2cBD" : LacCoinBD,
                     "2N1" : LacN1, "2N2" : LacN2, "2N3" : LacN3,
                    "3" : Herbe, "3BD" : HerbeFosseBD, "3BG" : HerbeFosseBG, "3HD" : HerbeFosseHD, "3HG" : HerbeFosseHG, "4B" : MontagneB,
                    "4H" : MontagneH, "4D" : MontagneD, "4G" : MontagneG, "4BD" : MontagneBD, "4BG" : MontagneBG, "4HD" : MontagneHD, "4HG" : MontagneHG,
                    "4TD" : TrouD, "4TG" : TrouG,

                    #---HOUSING TILES---#
                    "H1" : SolChambre, "H1O" : SolChambreOmbre, "H1Oc" : SolChambreOmbreCoin, "H1OG" : SolChambreOmbreG, "H1OH" : SolChambreOmbreH,

                    #---HOUSING MEUBLES---#
                    "HBiblioV" : BibliothequeVerte, "HBiblioM" : BibliothequeMarron, "HVitrine" : Vitrine, "HPanneau" : Panneau,
                    "HWindo1" : Fenetre_Petite, "HTime" : Horloge, "HDossier" : Dossier, "HBureau" : Bureau, "HTV" : TV, "HMachine" : Machine, "HLavabo" : Lavabo,
                    "HPlante" : Plante, "Frigo" : Frigo, "Bar" : Bar, "FRESQUE" : MaisonFRESQUE, "HStairsD" : StairsDown, "HStairsU" : StairsUp, "Wii" : Wii,
                    "HTapisR" : TapisRouge, "HLit" : Lit, "HCouette" : Couette, "Bloc2" : BLOCPROFONDEUR, "HFleur" : Fleur_Pot,
                    "HMur1" : Mur1, "HMur2" : Mur2, "HMur3" : Mur3, "HMur4" : Mur4, "HTable" : Table, "HTabouret" : Tabouret, "HCoussinViolet" : CoussinViolet, "HEXIT" : EXIT,

                    #---AMBRE---#
                    "Temizuya" : Temizuya, "Shrine" : Shrine, "Sapin1" : Sapin1, "Sapin2" : Sapin2, "Arbre1" : Arbre, "Arbuste1" : Arbuste1, "Fleur1" : FleurBlanche,
                    "Fleur2" : FleurRouge, "Champignon1" : Champignon, "HerbeMoyenne" : HerbeMoyenne, "Pierre1" : Pierre1, "Pierre2" : Pierre2, "Rocher1" : Rocher1,
                    "PontH" : PontH, "Rocher1EAU" : Rocher1EAU,
                    #---ISLA---#
                    "MS1" : Montagne_sable1,"MS2" : Montagne_sable2,"MS3" : Montagne_sable3,"MS4" : Montagne_sable4,"MS5" : Montagne_sable5,
                    "MS6" : Montagne_sable6 , "MS7" : Montagne_sable7, "MS8" : Montagne_sable8, "GMS1" : GMontagne_sable1,"GMS2" : GMontagne_sable2,"GMS3" : GMontagne_sable3,
                    "GMS4" : GMontagne_sable4,"GMS5" : GMontagne_sable5,"GMS6" : GMontagne_sable6,"GMS7" : GMontagne_sable7,"GMS8" : GMontagne_sable8,"GMS9" : GMontagne_sable9,
                    "GMS10" : GMontagne_sable10,"GMS11" : GMontagne_sable11,"GMS12" : GMontagne_sable12,"GMS13" : GMontagne_sable13,"GMS14" : GMontagne_sable14,"GMS15" : GMontagne_sable15,
                    "GMS16" : GMontagne_sable16,"S" : Sable,"P1" : Plage1,"P2" : Plage2,"P3" : Plage3,"P4" : Plage4,"P5" : Plage5,"P6" : Plage6,"P7" : Plage7,
                    "P8" : Plage8,"P9" : Plage9,"P10" : Plage10,"P11" : Plage11,"P12" : Plage12,"P13" : Plage13,
                    "BAT" : Bateau1, "COQ" : Coquillage, "HS" : Herbe_sable,"NX" : Noix, "PAL" : Palmier, "PAR" : Para, "Pi" : Pierre, "RO" : Roche, "Noir": Noir,
                    #---Labo---#
                    "CAR" : Carelage, "ML1" : Mur_lab1, "ML2" : Mur_lab2, "ML3" : Mur_lab3, "ML4" : Mur_lab4, "SER" : Serveur, "VIT" : Vitrine_lab,
                    #-------Hotel------#
                    "ESC" : Esca, "SH1" : Solhotel, "SH2" : Solhotel2, "LVB" : Lavabo, "TLT" : Toilet,
                    #-------Team Verichon------#
                    "STUT" : Statue,
                    #----------Eglise----------#
                    "AUT" : Autel, "BAC" : Banc, "FLB" : Flambeau, "MUE" : Mureglise, "VI1" : Vitrail1, "VI2" : Vitrail2,
                    #---Batiment---#
                    "MaisonDepart" : MaisonDepart, "Eglise" : Eglise, "QGVerichon" : QGVerichon, "LaboDepart" : LaboDepart
                    }
    
    DicoDecorsOBSTACLE = {"Bloc2" : BLOCPROFONDEUR}
    
    DicoDecors = {"NOIR" : Noir, "HCouette" : Couette, "HPlante" : Plante, "HBiblioV" : BibliothequeVerte, "HBiblioM" : BibliothequeMarron, "Temizuya" : TemizuyaWithout, "Shrine" : ShrineWithout,
                  "Sapin1" : Sapin1Sha, "Sapin2" : Sapin2Sha, "Arbuste1" : Arbuste1Sha, "Arbre1" : ArbreSha, "Champignon1" : Champignon, "Rocher1" : Rocher1Sha, "SER" : Serveur,
                  "RO" : Roche, "PAL" : Palmier, "PAR" : Para, "HVitrine" : Vitrine, "AUT" : Autel
                  }

    
    DicoPerso = {}




