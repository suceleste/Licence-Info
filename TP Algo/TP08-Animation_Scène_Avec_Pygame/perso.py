import pygame
import couleurs

# -- Initialisation -- #
def init(coord : tuple) -> dict:
    att = {"pos" : coord,
           "lim" : (1200-40, 600-40),
           "vit" : 3,
           "img" : 2}
    return att
# -- FIN -- #

# -- Dessin -- #    
def dessine(att : dict, surface):
    coord = att["pos"]
    if att["img"] == 0 :
        dessine1(coord, surface)
    elif att["img"] == 1 :
        dessine2(coord, surface)
    elif att["img"] == 2 :
        dessine3(coord, surface)

def dessine1(coord : tuple, surface) :
    pygame.draw.circle(surface, couleurs.beige, (coord[0], coord[1]), 10)
    pygame.draw.line(surface,couleurs.violet, (coord[0], coord[1]+10), (coord[0], coord[1]+30), 3)
    pygame.draw.line(surface,couleurs.violet, (coord[0], coord[1]+12), (coord[0]-10, coord[1]+27), 3)
    pygame.draw.line(surface,couleurs.violet, (coord[0], coord[1]+12), (coord[0]+10, coord[1]+27), 3)
    pygame.draw.line(surface,couleurs.marine, (coord[0], coord[1]+30), (coord[0]-10, coord[1]+48), 3)
    pygame.draw.line(surface,couleurs.marine, (coord[0], coord[1]+30), (coord[0]+10, coord[1]+48), 3)

def dessine2(coord : tuple, surface) :
    pygame.draw.circle(surface, couleurs.beige, (coord[0], coord[1]), 10)
    pygame.draw.line(surface,couleurs.violet, (coord[0], coord[1]+10), (coord[0], coord[1]+30), 3)
    pygame.draw.line(surface,couleurs.violet, (coord[0], coord[1]+12), (coord[0]-10, coord[1]+27), 3)
    pygame.draw.line(surface,couleurs.violet, (coord[0], coord[1]+12), (coord[0]+10, coord[1]+27), 3)
    pygame.draw.line(surface,couleurs.marine, (coord[0], coord[1]+30), (coord[0]-5, coord[1]+48), 3)
    pygame.draw.line(surface,couleurs.marine, (coord[0], coord[1]+30), (coord[0]+5, coord[1]+48), 3)

def dessine3(coord : tuple, surface) :
    pygame.draw.circle(surface, couleurs.beige, (coord[0], coord[1]), 10)
    pygame.draw.line(surface,couleurs.violet, (coord[0], coord[1]+10), (coord[0], coord[1]+30), 3)
    pygame.draw.line(surface,couleurs.violet, (coord[0], coord[1]+12), (coord[0]-10, coord[1]+27), 3)
    pygame.draw.line(surface,couleurs.violet, (coord[0], coord[1]+12), (coord[0]+10, coord[1]+27), 3)
    pygame.draw.line(surface,couleurs.marine, (coord[0], coord[1]+30), (coord[0]-1, coord[1]+48), 3)
    pygame.draw.line(surface,couleurs.marine, (coord[0], coord[1]+30), (coord[0]+1, coord[1]+48), 3)
# -- FIN -- #

# -- Update -- #
def update(att : dict) -> dict :
    if att["img"] < 2 :
        att["img"] += 1
    elif att["img"] >= 2 :
        att["img"] = 0

    if att["pos"][0] >= att["lim"][0] or att["pos"][0] <= 0:
        att["vit"] *= -1
    
    att["pos"] = (att["pos"][0] + att["vit"], att["pos"][1])
    return att
# -- FIN -- #