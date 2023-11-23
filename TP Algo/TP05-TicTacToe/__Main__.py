from random import randint

HUMAIN = "X" # Le symbole de l’humain.
ORDI = "O" # Le symbole de l’ordinateur.
VIDE = " " # Le symbole de case vide.
T_PLATEAU = 3 # Taille du plateau de jeu

def init_plateau() -> list :
    plateau = []
    for i in range(T_PLATEAU) :
        plateau.append([])
        for y in range(T_PLATEAU) :
            plateau[i].append(VIDE)
    return plateau

def print_tableau (l : list) -> None :
    for i in range(len(l)) :
        for y in range(len(l[i])):
            if y != 0 :
                print("|" + l[i][y], end="")
            else :
                print(l[i][y], end="")
        if i < len(l)-1 :
            print("\n" + "-"*(T_PLATEAU) + "--")
    print("\n\n")
        
        
def input_humain (l : list) -> tuple :
    input_H = input("Votre coup : ").split()
    
    if len(input_H) < 2 and len(input_H) > 2 :
        print("Veuillez entrer les coordonnées !")
        return input_humain(l)
    elif not input_H[0].isdigit() or not input_H[1].isdigit() :
        print("Veuillez entrer des chiffres !")
        return input_humain(l)
    elif int(input_H[0]) < 0 or int(input_H[1]) < 0 :
        print("Veuillez entrer des chiffres supérieur ou égal à 0 !")
        return input_humain(l)
    elif int(input_H[0]) > T_PLATEAU or int(input_H[1]) > T_PLATEAU :
        print("Veuillez entrer des chiffres inféreieur ou égal à la taille du plateau !")
        return input_humain(l)
    return (int(input_H[0]), int(input_H[1]))
    
def coords_vide( l : list) -> list :
    coord = []
    for y in range(len(l)) :
        for x in range(len(l[y])):
            if l[y][x] == VIDE :
              coord.append((x, y))
    return coord
            

def input_ordi (l : list) -> tuple :
    coord_V = coords_vide(l)
    return coord_V[randint(0, len(coord_V)-1)]

def verif_diags(s : str, plateau : list ) -> bool :
    if plateau[0][0] == s and plateau[1][1] == s and plateau[2][2] == s :
        return True
    elif plateau[0][2] == s and plateau[1][1] == s and plateau[2][0] == s :
        return True
    return False

def verif_lignes(s : str, plateau : list) -> bool :
    if plateau[0][0] == s and plateau[0][1] == s and plateau[0][2] == s :
        return True
    elif plateau[1][0] == s and plateau[1][1] == s and plateau[1][2] == s :
        return True
    elif plateau[2][0] == s and plateau[2][1] == s and plateau[2][2] == s :
        return True
    return False

def verif_cols(s : str, plateau : list) -> bool :
    if plateau[0][0] == s and plateau[1][0] == s and plateau[2][0] == s :
        return True
    elif plateau[0][1] == s and plateau[1][1] == s and plateau[2][1] == s :
        return True
    elif plateau[0][2] == s and plateau[1][2] == s and plateau[2][2] == s :
        return True
    return False

def est_victoire (s : str, plateau : list) -> bool :
    if verif_cols(s, plateau) or verif_diags(s, plateau) or verif_lignes(s, plateau) :
        return True
    else :
        return False
    
    
def joue_partie() -> None :
    
    run = True
    
    plateau = init_plateau()
    print_tableau(plateau)
    
    while run :
        
        H = input_humain(plateau)
        plateau[H[0]][H[1]] = HUMAIN
        print_tableau(plateau)
        if est_victoire(HUMAIN, plateau) :
            print ("Félicitation, vous avez gagnez !!!\n")
            break
        O = input_ordi(plateau)
        plateau[O[0]][O[1]] = ORDI
        print_tableau(plateau)
        if est_victoire(ORDI, plateau) :
            print("vous n'étes vraiment pas douer, je jouais au hasard.\n")
            break
        
def input_rejouer() -> bool :
    m = input("Voulez-vous rejouer (y/n)? ")
    return True if m == "y" else False

def main() -> None :
    joue_partie()
    while input_rejouer() :
        joue_partie()
    
if __name__ == '__main__' :
    main()
        
    