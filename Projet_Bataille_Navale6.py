####Jeu à 1 joueur####
from upemtk import *
from random import *

def init_plateau(n) : 
    """Crée une liste de liste de longeur "n" servant de plateau"""
    ligne=[0]*n  ##Liste servant de ligne au plateau##
    plateau=[0]*n  ##Liste plateau##
    i=0 
    while i <n :  ##Boucle pour créer une liste de liste afin de créer le plateau##
        plateau[i]=ligne.copy()
        i += 1
    return plateau ##On retourne la liste de liste correspondant au plateau##

def dessine_plateau(plateau, taille_case) :  
    """Dessine un plateau de n*n cases de taille 'taille_case' grâce à la liste de liste créer 
    précédemment avec la fonction init_plateau en utilisant une boucle for  """
    for i in range(len(plateau)) :   ##Boucle sur la longeur de la liste##
        for j in range(len(plateau[0])) : ##Boucle sur la longueur de la liste de liste##
            x = j * taille_case  ##Calcule les coordonnées en X##
            y = i * taille_case  ##Calcule les coordonnées en Y##
            if plateau[i][j] == 0 :  ##La case du plateau est blanche de base##
                couleur = 'white'
            elif plateau[i][j] == 'T' :  ##Si la case touché contient un bateau elle devient rouge##
                couleur = 'red'
            elif plateau[i][j] == 'R' :  ##Si la case touché ne contient rien elle devient noire##
                couleur = 'black'
            elif plateau [i][j] == 'X' : ##Si il ya un bateau la case devient jaune##
                couleur = 'yellow'
            rectangle(x, y, x + taille_case, y + taille_case, remplissage = couleur, tag = 'plateau') ##Trace les cases du plateau##
            
            """Complète le plateaux avec les lettres et les chiffres"""
            lettre = 65
            l = 1
            x = 32
            y = 32
            while l != 20 :  ##Boucle pour placer les lettres sur le plateau##
                texte(x, 5, chr(lettre), couleur='black', ancrage='nw', police ='Helvetica', taille = 10, tag = 'lettre')
                x += 25
                lettre += 1
                l += 1
            l = 1
            k = 1
            while l != 20 :  ##Boucle pour placer les nombres sur le plateau##
                texte(5, y, k, couleur='black', ancrage='nw', police ='Helvetica', taille = 10, tag = 'lettre')
                l += 1
                y += 25
                k += 1
    mise_a_jour()


def dessine_plateau2(plateau, taille_case, x, y) :     
    """Dessine un plateau de n*n cases de taille 'taille_case' grâce à la liste de liste créer 
    précédemment avec la fonction init_plateau en utilisant une boucle while """
    i = 0
    j = 0
    while x != 1000 :
        while y != 500 :
            if plateau[i][j] == 0 :  ##La case du plateau est blanche de base##
                couleur = 'white'
            elif plateau[i][j] == 'T' :  ##Si la case touché contient un bateau elle devient rouge##
                couleur = 'red'
            elif plateau[i][j] == 'R' :  ##Si la case touché ne contient rien elle devient noire##
                couleur = 'black'
            elif plateau [i][j] == 'X' : ##Si il ya un bateau on la laisse blanche car on ne doit pas voir les bateaux adverse##
                couleur = 'yellow'
            rectangle(x, y, x + taille_case, y + taille_case, remplissage = couleur, tag = 'plateau2')
            y += 25
            i += 1
        j += 1
        x += 25
        y = 0
        i = 0
    lettre = 65
    l = 1
    x1 = 532
    y1 = 532
    k = 1
    while l != 20 :  ##Boucle permettant de placer les lettres sur le plateau##
        texte(x1, 5, chr(lettre), couleur='black', ancrage='nw', police ='Helvetica', taille = 10, tag = 'lettre2')
        x1 += 25
        lettre += 1
        l += 1
    k = 1
    ya = 32
    while k != 20 :  ##Boucle permettant de placer les chiffres sur le plateau##
        texte(505, ya, k, couleur='black', ancrage='nw', police ='Helvetica', taille = 10, tag = 'chiffre2')
        k += 1
        ya += 25
    mise_a_jour()


def pixel_vers_case(x, y, taille_case) :   
    """Convertis les coordonnées d'un pixel en case dans la liste de liste"""
    return x//taille_case, y//taille_case  ##Convertis les coordonnées x, y en case en fesant la  divison entière de x et y par la taille des cases##


def placer_bateau(nb, x, y, plateau, dr) :
    """A l'aide d'un plateau, le joueur place les bateaux. Il choisit d'abord combien de bateau 
    il  veut, ensuite il faut choisir si le bateau va être placer horizontalement ou 
    verticalement puis donner les coordonées de la case"""
    i = 0
    if nb == 6 :  ##Navire de 1 case##
        plateau[x][y] = 'X'
    if nb == 5 :  ##Navire de 2 cases##
        if dr == 'verticale' :  ##Navire placer de façon verticale##
            while i < 2 :
                if y >= len(plateau[i])-1 :
                    plateau[x][y-i] = 'X'
                else :
                    plateau[x][y+i] = 'X'
                i += 1
        if dr == 'horizontale' :  ##Navire placer de façon horizontale##
            while i < 2 :
                if x >= len(plateau)-1 :
                    plateau[x-i][y] = 'X'
                else :
                    plateau[x+i][y] = 'X'
                i += 1
    if nb == 4 :  ##Navire de 3 cases##
        if dr == 'verticale' :  ##Navire placer de façon verticale##
            while i < 3 :
                if y >= len(plateau[i])-2 :
                    plateau[x][y-i] = 'X'
                else :
                    plateau[x][y+i] = 'X'
                i += 1
        if dr == 'horizontale' :  ##Navire placer de façon horizontale##
            while i < 3 :
                if x >= len(plateau)-2 :
                    plateau[x-i][y] = 'X'
                else :
                    plateau[(x-1)+i][y] = 'X'
                i += 1
    if nb == 3 :  ##Navire de 4 cases##
        if dr == 'verticale' :  ##Navire placer de façon verticale##
            while i < 4 :
                if y >= len(plateau[i])-3 :
                    plateau[x][y-i] = 'X'
                else :
                    plateau[x][y+i] = 'X'
                i += 1
        if dr == 'horizontale' :  ##Navire placer de façon horizontale##
            while i < 4 :
                if x >= len(plateau)-3 :
                    plateau[x-i][y] = 'X'
                else :
                    plateau[x+i][y] = 'X'
                i += 1
    if nb == 2 :  ##Navire de 5 cases##
        if dr == 'verticale' :  ##Navire placer de façon verticale##
            while i < 5 :
                if y >= len(plateau[i])-4 :
                    plateau[x][y-i] = 'X'
                else :
                    plateau[x][y+i] = 'X'
                i += 1
        if dr == 'horizontale' :  ##Navire placer de façon horizontale##
            while i < 5 :
                if x >= len(plateau)-4 :
                    plateau[x-i][y] = 'X'
                else :
                    plateau[x+i][y] = 'X'
                i += 1
    if nb == 1 :  ##Navire de 6 cases##
        if dr == 'verticale' :  ##Navire placer de façon verticale##
            while i < 6 :
                if y >= len(plateau[i])-5 :
                    plateau[x][y-i] = 'X'
                else :
                     plateau[x][y+i] = 'X'
                i += 1
        if dr == 'horizontale' :  ##Navire placer de façon horizontale##
            while i < 6 :
                if x >= len(plateau)-5 :
                    plateau[x-i][y] = 'X'
                else :
                    plateau[x+i][y] = 'X'
                i += 1
    return plateau


def tirer(i, j, plateau) :
    """A l'aide d'un couple de coordonnées change la valeur de la case correspondante dans la   
    liste de liste et renvoie cette nouvelle liste de liste""" 
    x = 0
    if plateau[i][j] == 'T' :      ##On regarde si la case a déja été touché##
        x = 'T'                  ##On laisse la même variable##
    elif plateau[i][j] == 'X' :     ##Si on a un bateau##
        plateau[i][j] = 'T'        ##On remplace la variable du bateau, par la variable touché##
        x = 'tirer'
    elif plateau[i][j] == 0 :     ##Si il n'y a rien##
        plateau[i][j] = 'R'   ##On remplace par la variable 'rien en vue'##
        v = voisine(i, j)        ##Si sur ces cases voisines ii y a un bateau##
        k = 0                      ##On remplace la variable par la variable 'en vue'##
        while k != len(v) :
            if plateau[v[k][0]][v[k][1]] == 'X':
                x = 'R'
                return x, plateau
            else :
                k +=1
        x = 'X'
    return x, plateau
            
            
def voisine(i, j) :
    """Si la case que le joueur à touché ne contient pas de bateau regarde les voisines de la case 
    pour permetre de dire si elles contiennent des bateaux ou non et et renvois 'EN VUE' si des 
    bateaux sont dans des voisines et 'RIEN' dans le cas contraire"""
    v=[]
    direction=[[1,0],[-1,0],[0,1],[0,-1], [-1, -1], [1, -1], [-1, 1], [1, 1]]  ##Liste des différentes voisines##
    k = 0
    while k < 8 :  ##Boucle permettant d'ajouter les voisines d'une case i, j dans une liste de liste##
        lv, cv = i + direction[k][0], j + direction[k][1]
        if 0 <= lv < 20 and 0 <= cv < 20 :
            v.append([lv,cv])
        k += 1
    return v  ##On retourne la liste avec les différents voisine##


def voisine2(l, c):
    '''ici on ne regarde que les cases en diagonales et en horizontal, au contraire de voisin ou il y a aussi les diagonales, elle retourne une liste avec les cases voisines'''
    v=[]
    direction=[[1,0],[-1,0],[0,1],[0,-1]]      ##On rend que les voisines contigue, sans les voisin en diagonales##
    i=0
    while i < 4: 
        lv,cv=l+direction[i][0],c+direction[i][1]
        if 0 <= lv < 20 and 0 <= cv < 20 :
            v.append([lv,cv])
        i+=1
    return v



 
cree_fenetre(1000, 500)            #On crée notre fenêtre
dico = {1: '1 bateau à 6 cases sélectionné', 2: '2 bateau à 5 cases sélectionné', 3: '3 bateau à 4 cases sélectionné', 4: '4 bateau à 3 cases sélectionné', 5: '5 bateau à 2 cases sélectionné', 6: '1 bateau à 6 cases sélectionné'}
v = 0

"""Menu Principale"""

while True :                            # Boucle infine
    
    #On remplie notre menu de rectangle, ils vont être les paramètres de la partie
    while v != 'banane' :        
        rectangle(180, 10, 800, 440, remplissage = 'RoyalBlue3')  
        rectangle(350,15, 650, 50, remplissage = 'black')              
        rectangle( 205, 80, 500, 120, remplissage = 'black')
        rectangle( 555, 80, 745, 120, remplissage = 'black')
        rectangle(310, 380, 630, 440, remplissage = 'black')
        y1 = 190
        y2 = 240
        z = 0
        while z != 3 :
            rectangle(300, y1, 500, y2, remplissage = 'black')
            rectangle(455, y1, 650, y2, remplissage = 'black')
            y1 += 60
            y2 += 60
            z += 1
        # On remplie chaque rectangle du menu avec un texte qui explique chaques paramètres et explique ce qu'il faut faire dans le menu pour lancer la partie et explique les différents paramètres
        texte(500, 30, 'Hitori', couleur='green', ancrage='center',  taille=24)
        texte(490, 400, 'Sélectionner le  nombre de joueurs et le', couleur='green', ancrage='center',  taille=10)
        texte(490, 420, 'nombre de bateaux puis appuier sur entrée', couleur='green', ancrage='center',  taille=10)
        texte(377, 100, '1 joueur', couleur='green', ancrage='center',  taille=16)
        texte(625, 100, '2 joueurs', couleur='green', ancrage='center',  taille=16)
        texte(425,215, '1 bateau à 6 cases', couleur='green', ancrage='center',  taille=10)
        texte(577.5,215, '2 bateaux à 5 cases', couleur='green', ancrage='center',  taille=10)
        texte(425,275, '3 bateaux à 4 cases', couleur='green', ancrage='center',  taille=10)
        texte(577.5,275, '4 bateaux à 3 cases', couleur='green', ancrage='center',  taille=10)
        texte(425,335, '5 bateaux à 2 cases', couleur='green', ancrage='center',  taille=10)
        texte(577.5,335, '6 bateaux à 1 cases', couleur='green', ancrage='center',  taille=10)
    
        positionMenu=''
        ev = donne_ev()
        ty = type_ev(ev)
        if ty == 'ClicGauche':          # A chaque fois que le joueur va selectionner avec son clic gauche un paramètre on affiche à l'écran ce que le joueur à selectionner comme paramètres de partie.
            x, y = abscisse(ev), ordonnee(ev)
            if 255 < x < 500 and 80 < y < 120 :
                joueur = 1
                texte(380, 150, '1 Joueur sélectionné', couleur='red',  taille=24, tag = 'j')
                attente(1)
                efface('j')
            elif 505 < x < 745 and 80 < y < 120 :
                joueur = 2
                texte(380, 150, '2 Joueur sélectionné', couleur='red',  taille=24, tag = 'j')
                attente(1)
                efface('j')
            elif 350 < x < 500 and 190 < y < 240 :
                n = 1
                case = 6
                texte(280, 150, dico[1], couleur='red',  taille=24, tag = 'p')
                attente(1)
                efface('p')
            elif 505 < x < 650 and 190 < y < 240 :
                n = 2
                case = 5
                texte(280, 150, dico[2], couleur='red',  taille=24, tag = 'p')
                attente(1)
                efface('p')
            elif 350 < x < 500 and 250 < y < 300 :
                n = 3
                case = 4
                texte(280, 150, dico[3], couleur='red',  taille=24, tag = 'p')
                attente(1)
                efface('p')
            elif 505 < x < 650 and 250 < y < 300 :
                n = 4
                case = 3
                texte(280, 150, dico[4], couleur='red',  taille=24, tag = 'p')
                attente(1)
                efface('p')
            elif 350 < x < 500 and 310 < y < 360 :
                n = 5
                case = 2
                texte(280, 150, dico[5], couleur='red',  taille=24, tag = 'p')
                attente(1)
                efface('p')
            elif 505 < x < 650 and 310 < y < 360 :
                n = 6
                case = 1
                texte(280, 150, dico[6], couleur='red',  taille=24, tag = 'p')
                attente(1)
                efface('p')
        if ty == 'Touche' :
            if 1 <= n <= 6 and (joueur == 1 or joueur == 2) :
                v = 'banane'
        if ty == 'Quitte':
            ferme_fenetre()
        mise_a_jour()
    efface_tout()


    """Programme Principale"""
    plateau = init_plateau(20)                    #On initialise chaques plateaux des joueurs
    plateau2 = init_plateau(20)
    dessine_plateau(plateau, 25)                   #On dessine chaques plateaux 
    dessine_plateau2(plateau2, 25, 500, 0)

    if joueur == 1 :
        d = 0
        dr = 'verticale'
        ligne(500, 0, 500, 500, epaisseur = 5)            #On indique au joueur qu'il faut placer ces bateaux et comment  les placer
        texte(290, 50, 'Veuillez placer vos bateaux,', couleur='red',  taille=24, tag = 'l')
        texte(80, 100,'clic gauche pour placer et clic droit pour changer le sens', couleur='red',  taille=24, tag = 'l')
        attente(2)
        efface('l')
        bateau = []
        while d != n:                               #On commence la partie
            ev = donne_ev()                         #On définie chaque évènements
            ty = type_ev(ev)
            if ty == 'ClicGauche' :                 #On indique ce que fait le clic gauche
                x, y = abscisse(ev), ordonnee(ev)               #Il va permettre de placer le(s) bateau(x)
                i,j = pixel_vers_case(x, y, 25)
                bateau.append([i, j])
                plateau = placer_bateau(n, j, i, plateau, dr)
                x2, y2 = randint(1, 19), randint(1, 19)
                m = randint(1, 2)
                if m == 1 :
                    dr2 = 'verticale'
                elif m == 2 :
                    dr2 = 'horizontale'
                plateau2 = placer_bateau(n, x2, y2, plateau2, dr2)
                efface('plateau')
                dessine_plateau(plateau, 25)
                d += 1
            elif ty == 'ClicDroit' :                               #On indique ce que fait le clic droit
                x, y = abscisse(ev), ordonnee(ev)
                if dr == 'verticale' :                               #Il va changer la direction de la position de notre bateau
                    dr = 'horizontale'
                    texte(380, 150, 'Position Verticale', couleur='red',  taille=24, tag = 'p')
                    attente(1)
                    efface('p')
                else :
                    dr = 'verticale'
                    texte(380, 150, 'Position Horizontale', couleur='red',  taille=24, tag = 'p')
                    attente(1)
                    efface('p')
            elif ty == 'Quitte':                       # Ou sinon on ferme le menu
                ferme_fenetre()
            attente(0.2)
        texte(180, 150, 'Veuillez choisir où tirer sur le deuxième plateau', couleur='red',  taille=24, tag = 'k')
        attente(1)
        efface('k')
        touche = 0
        couler = 0
        touche2 = 0
        couler2 = 0
        while couler != n or couler2 != n :       # Tant que l'on a pas gagné ou que l'on n'a pas perdu
            ev = donne_ev()
            ty = type_ev(ev)
            if ty == 'ClicGauche' :                  # Avec le clique gauche on récupère les coordonnées
                x, y = abscisse(ev)-500, ordonnee(ev)
                i, j = pixel_vers_case(x, y, 25)         
                x, plateau2 = tirer(j, i, plateau2)     #On utilise ces coordonnées pour tirer
                while x != 'pomme' :               # On définie un mesasge en fonction de la ou ce situe notre tire
                    if x == 'T' :
                        texte(380, 150, 'Vous avez déjà tirer sur cette case, veuillez changer de case', couleur='red',  taille=24, tag = 'p')
                        attente(0.5)
                        efface('p')
                    elif x == 'tirer' :    #Si on touche un bateau il affiche ''Bateau Touché'
                        texte(380, 150, 'Bateau Touché', couleur='red',  taille=24, tag = 'p')
                        attente(0.5)
                        efface('p')
                        touche += 1
                        x = 'pomme'
                    elif x == 'R' :         #Si il y a un bateau situé sur une case adjacent il affiche 'Bateau en vue'
                        texte(380, 150, 'Bateau en vue', couleur='red',  taille=24, tag = 'p')
                        attente(0.5)
                        efface('p')
                        x = 'pomme'
                    elif x == 'X' :          #Si il n'y a aucun bateau à coté il affiche 'Auncun bateau est en vue'
                        texte(380, 150, 'Auncun bateau est en vue', couleur='red',  taille=24, tag = 'p')
                        attente(0.5)
                        efface('p')
                        x = 'pomme'
                efface('plateau2')           #On efface notre plateau et on le re dessine avec les nouvelles cases
                dessine_plateau2(plateau2, 25, 500, 0)
                x2, y2 = randint(1, 19), randint(1, 19)
                x2, plateau = tirer(y2, x2, plateau)
                efface('plateau')
                dessine_plateau(plateau, 25)
                if touche == case :
                    touche = 0
                    couler += 1
                    texte(380, 150, 'Un bateau a été coulé', couleur='red',  taille=24, tag = 'te')
                    attente(0.5)
                    efface('te')
                if couler == n :
                    texte(380, 150, 'Vous avez Gagné !', couleur='red',  taille=24, tag = 'te')
                    break
                elif touche2 == case :
                    touche2 = 0
                    couler2 += 1
                    texte(380, 150, 'Un de vos bateau a été coulé', couleur='red',  taille=24, tag = 'te')
                    attente(0.5)
                    efface('te')
                if couler2 == n :
                    texte(380, 150, 'Vous avez Perdu !', couleur='red',  taille=24, tag = 'te')
                    break
            elif ty == 'Quitte':
                ferme_fenetre()
            attente(0.5)
    
    
    if joueur == 2 :
        d = 0
        d2 = 0
        dr2 = 'verticale'
        dr = 'verticale'
        ligne(500, 0, 500, 500, epaisseur = 5)            #On indique au joueur qu'il faut placer ces bateaux et comment  les placer
        texte(290, 50, 'Veuillez placer vos bateaux,', couleur='red',  taille=24, tag = 'l')
        texte(80, 100,'Joueur 1 clic gauche pour placer et clic droit pour changer le sens', couleur='red',  taille=24, tag = 'l')
        attente(2)
        efface('l')
        while d != n:                               #On commence la partie
            ev = donne_ev()                         #On définie chaque évènements
            ty = type_ev(ev)
            if ty == 'ClicGauche' :                 #On indique ce que fait le clic gauche
                x, y = abscisse(ev), ordonnee(ev)               #Il va permettre de placer le(s) bateau(x)
                i,j = pixel_vers_case(x, y, 25)
                plateau = placer_bateau(n, j, i, plateau, dr)
                efface('plateau')
                dessine_plateau(plateau, 25)
                d += 1
            elif ty == 'ClicDroit' :                               #On indique ce que fait le clic droit
                x, y = abscisse(ev), ordonnee(ev)
                if dr == 'verticale' :                               #Il va changer la direction de la position de notre bateau
                    dr = 'horizontale'
                    texte(380, 150, 'Position Verticale', couleur='red',  taille=24, tag = 'p')
                    attente(1)
                    efface('p')
                else :
                    dr = 'verticale'
                    texte(380, 150, 'Position Horizontale', couleur='red',  taille=24, tag = 'p')
                    attente(1)
                    efface('p')
            elif ty == 'Quitte':                       # Ou sinon on ferme le menu
                ferme_fenetre()
            attente(0.2)
        texte(80, 100,'Joueur 2 clic gauche pour placer et clic droit pour changer le sens', couleur='red',  taille=24, tag = 'lt')
        attente(2)
        efface('lt')
        while d2 != n:                               #On commence la partie
            ev = donne_ev()                         #On définie chaque évènements
            ty = type_ev(ev)
            if ty == 'ClicGauche' :                 #On indique ce que fait le clic gauche
                x2, y2 = abscisse(ev)-500, ordonnee(ev)               #Il va permettre de placer le(s) bateau(x)
                i2, j2 = pixel_vers_case(x2, y2, 25)
                plateau2 = placer_bateau(n, j2, i2, plateau2, dr2)
                efface('plateau2')
                dessine_plateau2(plateau2, 25, 500, 0)
                d2 += 1
            elif ty == 'ClicDroit' :                               #On indique ce que fait le clic droit
                x2, y2 = abscisse(ev), ordonnee(ev)
                if dr2 == 'verticale' :                               #Il va changer la direction de la position de notre bateau
                    dr2 = 'horizontale'
                    texte(380, 150, 'Position Verticale', couleur='red',  taille=24, tag = 'p')
                    attente(1)
                    efface('p')
                else :
                    dr2 = 'verticale'
                    texte(380, 150, 'Position Horizontale', couleur='red',  taille=24, tag = 'p')
                    attente(1)
                    efface('p')
            attente(0.2)
        texte(180, 150, 'Veuillez choisir où tirer sur le deuxième plateau', couleur='red',  taille=24, tag = 'k')
        attente(1)
        efface('k')
        touche = 0
        couler = 0
        touche2 = 0
        couler2 = 0
        while couler != n or couler2 != n :       # Tant que l'on a pas gagné ou que l'on n'a pas perdu
            ev = donne_ev()
            ty = type_ev(ev)
            texte(380, 150, 'Séléctionner  où tirer', couleur='red',  taille=24, tag = 'pi')
            attente(0.2)
            efface('pi')
            if ty == 'ClicGauche' :                  # Avec le clique gauche on récupère les coordonnées
                x, y = abscisse(ev)-500, ordonnee(ev)
                i, j = pixel_vers_case(x, y, 25)         
                x, plateau2 = tirer(j, i, plateau2)     #On utilise ces coordonnées pour tirer
                while x != 'pomme' :               # On définie un mesasge en fonction de la ou ce situe notre tire
                    if x == 'T' :
                        texte(380, 150, 'Vous avez déjà tirer sur cette case, veuillez changer de case', couleur='red',  taille=24, tag = 'p')
                        attente(0.5)
                        efface('p')
                    elif x == 'tirer' :    #Si on touche un bateau il affiche ''Bateau Touché'
                        texte(380, 150, 'Bateau Touché', couleur='red',  taille=24, tag = 'p')
                        attente(0.5)
                        efface('p')
                        touche += 1
                        x = 'pomme'
                    elif x == 'R' :         #Si il y a un bateau situé sur une case adjacent il affiche 'Bateau en vue'
                        texte(380, 150, 'Bateau en vue', couleur='red',  taille=24, tag = 'p')
                        attente(0.5)
                        efface('p')
                        x = 'pomme'
                    elif x == 'X' :          #Si il n'y a aucun bateau à coté il affiche 'Auncun bateau est en vue'
                        texte(380, 150, 'Auncun bateau est en vue', couleur='red',  taille=24, tag = 'p')
                        attente(0.5)
                        efface('p')
                        x = 'pomme'
                efface('plateau2')           #On efface notre plateau et on le re dessine avec les nouvelles cases
                dessine_plateau2(plateau2, 25, 500, 0)
            attente(0.5)
            ev = donne_ev()
            ty = type_ev(ev)
            if ty == 'ClicGauche' :                  # Avec le clique gauche on récupère les coordonnées
                x2, y2 = abscisse(ev), ordonnee(ev)
                i2, j2 = pixel_vers_case(x2, y2, 25)         
                x2, plateau = tirer(j2, i2, plateau)     #On utilise ces coordonnées pour tirer
                while x2 != 'pomme' :               # On définie un mesasge en fonction de la ou ce situe notre tire
                    if x2 == 'T' :
                        texte(380, 150, 'Vous avez déjà tirer sur cette case, veuillez changer de case', couleur='red',  taille=24, tag = 'p')
                        attente(0.5)
                        efface('p')
                    elif x2 == 'tirer' :    #Si on touche un bateau il affiche ''Bateau Touché'
                        texte(380, 150, 'Bateau Touché', couleur='red',  taille=24, tag = 'p')
                        attente(0.5)
                        efface('p')
                        touche2 += 1
                        x2 = 'pomme'
                    elif x2 == 'R' :         #Si il y a un bateau situé sur une case adjacent il affiche 'Bateau en vue'
                        texte(380, 150, 'Bateau en vue', couleur='red',  taille=24, tag = 'p')
                        attente(0.5)
                        efface('p')
                        x2 = 'pomme'
                    elif x2 == 'X' :          #Si il n'y a aucun bateau à coté il affiche 'Auncun bateau est en vue'
                        texte(380, 150, 'Auncun bateau est en vue', couleur='red',  taille=24, tag = 'p')
                        attente(0.5)
                        efface('p')
                        x2 = 'pomme'
                efface('plateau')
                dessine_plateau(plateau, 25)
                if touche == case :
                    touche = 0
                    couler += 1
                    texte(380, 150, 'Un bateau a été coulé', couleur='red',  taille=24, tag = 'te')
                    attente(0.5)
                    efface('te')
                if couler == n :
                    texte(380, 150, 'Vous avez Gagné !', couleur='red',  taille=24, tag = 'te')
                    break
                elif touche2 == case :
                    touche2 = 0
                    couler2 += 1
                    texte(380, 150, 'Un de vos bateau a été coulé', couleur='red',  taille=24, tag = 'te')
                    attente(0.5)
                    efface('te')
                if couler2 == n :
                    texte(380, 150, 'Vous avez Perdu !', couleur='red',  taille=24, tag = 'te')
                    break
            elif ty == 'Quitte':
                ferme_fenetre()
            attente(0.5)
        
            
            
            
            
            
            
        
         
        
    
    
    attend_fermeture()
    ferme_fenetre()





####Jeu à 2 joueurs####

"""Changement dans programme principale avec affichage du plateau, effacer puis afficher le plateau de l'autre joueur"""


####Améliorations####

def placer_bateau_aleatoire(n) :
    """Place les bateaux aléatoirement à l'aide de la fonction rand() du module srand(getpid())"""


def niveaux_bots(plateau, w) :
    """Permet de choisir la difficulté du bot dans le menu"""
    w=input("Bot 'facile' , 'moyen' ou 'difficile' ?")
    if w == 'facile':
        i, j = randint(1, 19), randint(1, 19)
        tirer(i, j, plateau)
        i, j = randint(voisine3(i, j))
    elif w =='moyen':
        i, j = randint(1, 19), randint(1, 19)
        tirer(i, j, plateau)
        i, j = randint(voisine2(i, j))
    elif w =='difficile':
        i, j = randint(1, 19), randint(1, 19)
        tirer(i, j, plateau)
        i, j = randint(voisine(i, j))
    return plateau


    """Combat bots"""
    plateau = init_plateau(20)
    plateau2 = init_plateau(20)
    dessine_plateau(plateau, 25)
    dessine_plateau2(plateau2, 25, 500, 0)
    d = 0
    ligne(500, 0, 500, 500, epaisseur = 5)
    while d != n:
        x, y = randint(1, 19), randint(1, 19)
        m = randint(1, 2)
        if m == 1 :
            dr = 'verticale'
        elif m == 2 :
            dr = 'horizontale'
        plateau = placer_bateau(n, x, y, plateau, dr)
        x2, y2 = randint(1, 19), randint(1, 19)
        m2 = randint(1, 2)
        if m2 == 1 :
            dr2 = 'verticale'
        elif m2 == 2 :
            dr2 = 'horizontale'
        plateau2 = placer_bateau(n, x2, y2, plateau2, dr2)
        efface('plateau')
        dessine_plateau(plateau, 25)
        efface('plateau2')
        dessine_plateau2(plateau, 25)
        d += 1
        attente(0.2)
    while not gagne(n, plateau2) or perdu(n, plateau) :
        x, y = randint(1, 19), randint(1, 19)
        x, plateau2 = tirer(j, i, plateau2)
        efface('plateau2')
        dessine_plateau2(plateau2, 25, 500, 0)
        x2, y2 = randint(1, 19), randint(1, 19)
        x2, plateau = tirer(y2, x2, plateau)
        efface('plateau')
        dessine_plateau(plateau, 25)
        attente(0.5)