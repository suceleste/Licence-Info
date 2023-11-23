import pygame
import dessin

def main() :
    pygame.init()

    SCREEN = pygame.display.set_mode((1200, 600))
    pygame.display.set_caption("TP9 - Pygame")
    Clock = pygame.time.Clock ()

    run = True
    while run :

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                run = False

        SCREEN.fill ((0, 0, 0))
        dessin.dessine(SCREEN)

        pygame.display.update()
        Clock.tick(40)
    
    pygame.quit()

if __name__ == "__main__" : 
    main()