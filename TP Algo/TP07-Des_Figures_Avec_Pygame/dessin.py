import pygame
import couleurs

def dessine(surface) :
    dessine_ciel(surface)
    dessine_soleil(surface)
    dessine_sol(surface)
    dessine_maisons(8, 40, (40, 280), surface)
    dessine_nuage((-10, 200), surface)
    dessine_nuage((200, 100), surface)
    dessine_nuage((350, 170), surface)
    dessine_nuage((700, 150), surface)
    dessine_nuage((890, 210), surface)
    dessine_nuage((1100, 100), surface)

def dessine_ciel(surface) :
    pygame.draw.rect(surface , couleurs.bleu , (0 ,0, 1300, 1300))

def dessine_soleil(surface) :
    pygame.draw.circle(surface, couleurs.jaune, (1000, 100), 50)
    pygame.draw.circle(surface, couleurs.jauneF, (1000, 100), 40)

def dessine_sol(surface) :
    pygame.draw.rect(surface, couleurs.vert, (0, 600-200, 1300, 1300))
    pygame.draw.rect(surface, couleurs.gris, (0, 600-100, 1300, 70))

def dessine_maison(coord, surface) :
    pygame.draw.rect(surface, couleurs.violet, (coord[0], coord[1]+50, 100, 120))
    pygame.draw.polygon(surface, couleurs.noir, ((coord[0], coord[1]+50), (coord[0]+100, coord[1]+50), (coord[0]+50, coord[1])))
    pygame.draw.rect(surface, couleurs.noir, (coord[0]+10, coord[1]+60, 35, 30))
    pygame.draw.rect(surface, couleurs.noir, (coord[0]+55, coord[1]+60, 35, 30))
    pygame.draw.ellipse(surface, couleurs.jaune, (coord[0]+15, coord[1]+100, 25, 20))
    pygame.draw.rect(surface, couleurs.jaune, (coord[0]+55, coord[1]+115, 35, 30))
    pygame.draw.rect(surface, couleurs.rouge, (coord[0]+15, coord[1]+110, 25, 60))
    pygame.draw.circle(surface, couleurs.noir, (coord[0]+20, coord[1]+140), 2)
    pygame.draw.polygon(surface, couleurs.gris , ((coord[0]+15, coord[1]+170), (coord[0]+40, coord[1]+170), (coord[0]+55, coord[1]+220), (coord[0]+30, coord[1]+220)))


def dessine_maisons(nb_maisons, ecart, coord, surface) :
    x = coord[0]
    y = coord[1]
    for i in range(nb_maisons) :
        dessine_maison((x, y), surface)
        x += 100 + ecart
        

def dessine_nuage(coord, surface) :
    pygame.draw.ellipse(surface, couleurs.blanc, (coord[0], coord[1], 120, 50))
    pygame.draw.ellipse(surface, couleurs.blanc, (coord[0]+32, coord[1]+17, 60, 50))
    pygame.draw.ellipse(surface, couleurs.blanc, (coord[0]+32, coord[1]-17, 60, 50))