DANS JEU.PY

Pos_Px = (Largeur_Jeu/2 - Modules.Axe_x ) / Background.TailleGrid
Pos_Py = (Hauteur_Jeu/2 - Modules.Axe_y +25) / Background.TailleGrid

    #---Portail---#
    
    if Pos_Py == 10.15625  and Pos_Px == 12.5:
        POT = 1

    if POT  == 1 and 0<Pos_Py<1 and -1<Pos_Px<0:
            Background.Obstacle = []
            POT = 0

    if POT == 0 and  5<Pos_Py<6 and 6<Pos_Px<7:
                Background.Obstacle = []
                POT = 1
            
    if POT == 0:
        Mop = "maps/entre.map"
            
    elif POT == 1:
        Background.Obstacle = []
        Mop = "maps/sortie.map"
    Terrain = Mapping.Charger_Map(Mop)

    Fenetre_Jeu.fill((0, 0, 150))

