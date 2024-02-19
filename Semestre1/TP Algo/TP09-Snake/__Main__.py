import pygame
import random

BLANC = ( 255, 255, 255)
NOIR = ( 0, 0, 0)
VERT = ( 0, 192, 0)
ROUGE = ( 192, 0, 0)

L_CARRE = 10 # Largeur d’un carre du serpent.
VITESSE = 10 # Vitesse de deplacement du serpent (doit etre egale a L_CARRE).

WIDTH, HEIGHT = 800, 600 

# Fonction Principal
def main() :
    ''' Fonction Principal'''

    # Initialisation
    pygame.init()
    
    # Variables Principale 
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("TP09 - Snake")
    Clock = pygame.time.Clock ()
    Font = pygame.font.SysFont('timesnewroman',  30)
    niveau = niveau_init(SCREEN)
    snake = snake_init(niveau, VITESSE, 3)
    fruit = fruit_init(niveau)
    run = True
    pause = False

    # Ouverture
    ouverture(SCREEN)
    pygame.time.wait(3000)


    # Boucle Principale
    while run :
        
    
        # Boucle d'Evenement
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                run = False
            

            # Event Key
            if event.type == pygame.KEYDOWN :
                
                # Déplacement
                if event.key == pygame.K_RIGHT :
                    snake["depl_x"] = 1
                    snake['depl_y'] = 0

                elif event.key == pygame.K_LEFT :
                    snake["depl_x"] = -1
                    snake['depl_y'] = 0

                elif event.key == pygame.K_DOWN :
                    snake["depl_x"] = 0
                    snake['depl_y'] = 1

                elif event.key == pygame.K_UP :
                    snake["depl_x"] = 0
                    snake['depl_y'] = -1

                
                # Rejouer or Quit
                if  event.key == pygame.K_RETURN and pause :
                    return main()
                elif event.key == pygame.K_q and pause : 
                    run = False


        # Verif Collisions
        if snake_heurte_mur(snake)  :
            Fermeture(SCREEN, 'Game Over !!!', ROUGE)
            pause = True

        elif snake_mort_queue(snake)  :  
            Fermeture(SCREEN, 'Game Over !!!', ROUGE)
            pause = True

        elif snake_mange(snake, fruit) :
            snake_grandit(snake)
            niveau['score'] += 1
            fruit['pos'] = (random.randrange(niveau["rect_jeu"][0], niveau["rect_jeu"][2], L_CARRE), random.randrange(niveau["rect_jeu"][1], niveau["rect_jeu"][3], L_CARRE))


        # Verif Victoire
        if niveau["score"] == niveau["max_score"]  :
            Fermeture(SCREEN, 'Victoire !!!', VERT)
            pause = True

        if not pause:
        # Update la position
            snake_update_pos(snake)


        # Mise a Jour de l'Affichage
            SCREEN.fill(BLANC)
            pygame.draw.rect(SCREEN, NOIR, (niveau['rect_jeu'][0], niveau['rect_jeu'][1], 13000, 13000))
            fruit_dessine(fruit)
            snake_dessine(snake)
            niveau_dessine(niveau)
        pygame.display.update()
        Clock.tick(20)
    
    pygame.quit()



# Affichage Fermeture
def Fermeture(surface, message : str , couleur : tuple):
    
    # Message
    Font = pygame.font.SysFont('timesnewroman',  80)
    message = Font.render(message, True, couleur)
    messageRect = message.get_rect()
    messageRect.center = (WIDTH // 2, HEIGHT * (1/5))

    # Q Quitter or ENTER Rejouer
    Font = pygame.font.SysFont('timesnewroman',  30)
    q_or_r = Font.render("Q pour Quitter ou ENTER pour Rejouer", True, BLANC)
    q_or_rRect = q_or_r.get_rect()
    q_or_rRect.center = (WIDTH // 2, HEIGHT * (3/5))

    surface.blit(q_or_r, q_or_rRect)
    surface.blit(message, messageRect)




# Affichage de démarrage
def ouverture(surface) :

    # Titre
    Font = pygame.font.SysFont('timesnewroman',  80)
    Titre = Font.render("Snake", True, VERT)
    TitreRect = Titre.get_rect()
    TitreRect.center = (WIDTH // 2, HEIGHT * (1/5))


    # Auteur
    Font = pygame.font.SysFont('timesnewroman',  20)
    Auteur = Font.render("Descamps Sullyvan", True, BLANC)
    AuteurRect = Auteur.get_rect()
    AuteurRect.bottomleft = (5, HEIGHT - 5)


    # Instruction
    Font = pygame.font.SysFont('timesnewroman',  20)
    Inst = Font.render("→ Droite \ ← Gauche \ ↑ Haut \ ↓ Bas", True, BLANC)
    InstRect = Inst.get_rect()
    InstRect.center = (WIDTH // 2, HEIGHT * 1/3)


    # Date / Version 
    Font = pygame.font.SysFont('timesnewroman',  20)
    DV = Font.render("05/12/2023 :: V1.0", True, BLANC)
    DVRect = DV.get_rect()
    DVRect.bottomright = (WIDTH - 5, HEIGHT - 5)    


    # Update Affichage
    surface.blit(DV, DVRect)
    surface.blit(Inst, InstRect)
    surface.blit(Auteur, AuteurRect)
    surface.blit(Titre, TitreRect)
    pygame.display.update()




# -- Fonction pour Niveau -- #

    # Initialisation
def niveau_init(surface) -> dict:
    ''' Init niveau. '''
    niveau = {}
    niveau['surf'] = surface
    niveau['score'] = 0
    niveau['max_score'] = 5
    niveau['rect_score'] = pygame.Rect(0,0, 60, 30)
    niveau['rect_jeu'] = (0, 30, WIDTH, HEIGHT)
    return niveau


    # Dessin
def niveau_dessine(niveau : dict) :
    pygame.draw.rect(niveau["surf"], BLANC, niveau['rect_score'])

    Font = pygame.font.SysFont('timesnewroman',  40)
    ScoreText = Font.render(str(niveau['score']), True, NOIR)
    ScoreTextRect = ScoreText.get_rect()
    ScoreTextRect.center = niveau['rect_score'].width // 2, niveau['rect_score'].height // 2

    niveau['surf'].blit(ScoreText, ScoreTextRect) 
# -- FIN -- #




# -- Fonction Snake -- #
    # Initialisation
def snake_init(niv : dict, vit : int, longueur : int) -> dict :
    snake = {}
    snake["niv"] = niv 
    snake["vit_arg"] = vit
    snake["depl_x"] = 1
    snake["depl_y"] = 0
    snake["corps"] = [(WIDTH//2 , HEIGHT//2)]

    for i in range(longueur): 
        snake["corps"].append((snake["corps"][i][0] - L_CARRE*snake["depl_x"], snake["corps"][i][1] + L_CARRE*snake['depl_y']))
    snake['larg'] = len(snake["corps"]) * L_CARRE
         
    return snake


    # Dessin
def snake_dessine (snake : dict) :
    for e in snake['corps']:
        pygame.draw.rect(snake['niv']['surf'], VERT, (e[0],e[1], L_CARRE, L_CARRE))

    # Update Position
def snake_update_pos(snake : dict) :
    newSnake = [(snake["corps"][0][0] + snake["depl_x"]*snake["vit_arg"], snake["corps"][0][1] + snake["depl_y"]*snake["vit_arg"])]

    for i in range(1, len(snake["corps"])):
        newSnake.append(snake['corps'][i-1])

    snake['corps'] = newSnake


    # Collisions

        # Mur
def snake_heurte_mur(snake : dict) :  
    if snake['niv']['rect_jeu'][0] < snake['corps'][0][0] < snake['niv']['rect_jeu'][2] and snake['niv']['rect_jeu'][1] < snake['corps'][0][1] < snake['niv']['rect_jeu'][3] :
        return False

    else: 
        return True


        # Avec lui-même 
def snake_mort_queue(snake) :
    for i in range(1, len(snake['corps'])) :
        if snake['corps'][i][0] < snake['corps'][0][0] + L_CARRE //2 < snake['corps'][i][0] + L_CARRE and snake['corps'][i][1] < snake['corps'][0][1] + L_CARRE//2 < snake['corps'][i][1] + L_CARRE :
            return True

    return False


        # Avec les pommes
def snake_mange(snake : dict, fruit : dict) :
    if fruit['pos'][0] < snake['corps'][0][0] + L_CARRE //2 < fruit['pos'][0] + L_CARRE and fruit['pos'][1] < snake['corps'][0][1] + L_CARRE //2 < fruit['pos'][1] + L_CARRE :
        return True

    return False


    # Ajout de carré sur Snake
def snake_grandit(snake : dict) :
    snake['corps'].append((snake["corps"][-1][0] - L_CARRE*snake["depl_x"], snake["corps"][-1][1] + L_CARRE*snake['depl_y']))
# -- FIN -- #




# -- Fruit -- #

    # Initialisation
def fruit_init(niv : dict) -> dict:
    fruit = {}
    fruit["niv"] = niv
    fruit['pos'] = (random.randrange(niv["rect_jeu"][0], niv["rect_jeu"][2], L_CARRE), random.randrange(niv["rect_jeu"][1], niv["rect_jeu"][3], L_CARRE))
    fruit['larg'] = L_CARRE

    return fruit


    # Dessin
def fruit_dessine(fruit : dict) :
    pygame.draw.rect(fruit['niv']['surf'], ROUGE, (fruit['pos'][0], fruit['pos'][1], fruit['larg'], fruit['larg']))
# -- FIN -- #




# Appel de la Fonction
if __name__ == "__main__" : 
    main()