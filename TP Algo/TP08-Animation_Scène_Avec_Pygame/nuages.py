from random import randint
import couleurs
import pygame

# -- Initialisation -- #
def init(nombre) -> dict :
    att = { "vit" : 3,
            "lim" : (1200, 300),
            "objs" : [(randint(0,1200), randint(0, 300))for i in range(nombre)]}
    return att
# -- FIN -- #

# -- Dessin -- #
def dessine(att: dict, surface ) :
    for e in att["objs"] :
        nuage(e, surface)

def nuage(coord : tuple, surface) :
    pygame.draw.ellipse(surface, couleurs.blanc, (coord[0], coord[1], 120, 50))
    pygame.draw.ellipse(surface, couleurs.blanc, (coord[0]+32, coord[1]+17, 60, 50))
    pygame.draw.ellipse(surface, couleurs.blanc, (coord[0]+32, coord[1]-17, 60, 50))
# -- FIN -- #

# -- Update -- #
def update(att : dict) -> dict :
    objs = []
    for e in att["objs"] :
        if e[0] >= att["lim"][0] :
            objs.append((-20, randint(0, 300)))
        else :
            objs.append((e[0]+att["vit"], e[1]))
    att["objs"] = objs
    return att
# -- FIN -- #