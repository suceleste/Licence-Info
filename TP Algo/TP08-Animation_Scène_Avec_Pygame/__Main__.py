import pygame
import scenario

# Fonction Principal
def main() :
    # Variables Principale 
    pygame.init()
    scen = scenario.init()

    SCREEN = pygame.display.set_mode((1200, 600))
    pygame.display.set_caption("TP08 - Animation Scène Avec Pygame")
    Clock = pygame.time.Clock ()

    run = True
    while run :
        
        # Boucle d'Evenement
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                run = False
        
        # Changement Variable de Scène
        scenario.update(scen)

        # Mise a Jour de l'Affichage
        SCREEN.fill ((0, 0, 0))
        scenario.dessine(scen, SCREEN)
        pygame.display.update()
        Clock.tick(40)
    
    pygame.quit()


# Appel de la Fonction
if __name__ == "__main__" : 
    main()
    