import pygame
import couleurs
import nuages
import perso

# -- Initialisation -- #
def init() -> dict:
    att = {}
    att["nuages"] = nuages.init(4)
    att["perso"] = perso.init((1000,500))
    return att
# -- Fin -- #

# -- Dessin -- #
def dessine(scenario : dict, surface) : 
    dessine_ciel(surface)
    dessine_soleil(surface)
    nuages.dessine(scenario["nuages"], surface)
    dessine_montagnes(surface)
    dessine_sol(surface)
    dessine_arbre((200, 330), surface)
    dessine_arbre((300, 390), surface)
    dessine_arbre((520, 400), surface)
    dessine_arbre((700, 330), surface)
    dessine_arbre((800, 390), surface)
    dessine_arbre((1120, 400), surface)
    perso.dessine(scenario["perso"], surface)
    dessine_arbre((100, 460), surface)
    dessine_arbre((600, 460), surface)
    dessine_arbre((150, 510), surface)
    dessine_arbre((650, 510), surface)
    dessine_arbre((750, 450), surface)
    dessine_arbre((450, 450), surface)

def dessine_ciel(surface) :
    pygame.draw.rect(surface , couleurs.bleu , (0 ,0, 1300, 1300))

def dessine_soleil(surface) :
    pygame.draw.circle(surface, couleurs.jaune, (900, 100), 50)
    pygame.draw.circle(surface, couleurs.jauneF, (900, 100), 40)
    
def dessine_montagnes(surface) :
    pygame.draw.polygon(surface, couleurs.pesto , ((-600,600), (400,100), (1000,600)))
    pygame.draw.polygon(surface, couleurs.blanc , ((200,200), (400,100), (520,200)))
    pygame.draw.polygon(surface, couleurs.pesto , ((400,600), (1000,100), (1600,600)))
    pygame.draw.polygon(surface, couleurs.blanc , ((880,200), (1000,100), (1120,200)))

def dessine_sol(surface) :
    pygame.draw.rect(surface , couleurs.blanc , (0 ,400, 1300, 1300))

def dessine_arbre(coord ,surface) :
    for i in range(0,4) :
        pygame.draw.polygon(surface, couleurs.vert , ((coord[0],coord[1]+40+(20*i)), (coord[0]+20,coord[1]+(20*i)), (coord[0]+40,coord[1]+40+(20*i))))
# -- FIN -- #

# -- Update -- #
def update(att : dict) :
    nuages.update(att["nuages"])
    perso.update(att["perso"])
# -- FIN -- #