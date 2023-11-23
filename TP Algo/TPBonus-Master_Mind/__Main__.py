from random import randint

TAILLE = 4
MAX = 5

def genere_secret() -> list :
    l = []
    for i in range(TAILLE) :
        l.append(randint(0,MAX))
    return l

def lire_prop() :
    prop = input("Votre proposition ? (au format " + "x"*TAILLE +" )")
    prop = conversion(prop)
    if valide_mm(prop) :
        return prop
    else:
        print("Erreur mauvais format !!! ")
        return lire_prop
def bp_mp(prop : [int], code : [int]) -> (int,int) :
    bp = bien_places(prop, code)
    mp = valeurs_communes(distribution(prop), distribution(code)) - bp
    return (bp, mp)

def affiche_reponse(bp : int, mp : int) -> None :
    return print(f"Il y a actuellement {bp} de bien placé.\nEt il y a {mp} de mal placé\n\n")



#-- lire_prop() --#

def valide_mm(prop : [int]) -> bool :
    if len(prop) <= TAILLE :
        for i in prop :
            if i > MAX :
                return False
    else :
        return False
    return True


def conversion(l : [str]) -> [int] :
    l2 = []
    for i in range(len(l)) :
        if l[i].isdigit() :
            l2.append(int(l[i]))
    return l2

# -- FIN -- #

#-- bp_mp() --#

def bien_places(prop : [int], code : [int]) -> int :
    n = 0
    for i in range(len(code)) :
        if code[i] == prop[i] :
            n += 1
    return n

def distribution(prop : list[int]) -> list[int]:
    l = [0 for x in range(MAX+1)]
    for i in prop :
        l[i] += 1
    return l
    
def valeurs_communes(prop : [int], code : [int]) -> int:
    n = 0
    for i in range(len(prop)) :
        n += min(prop[i], code[i])
    return n

# -- FIN -- #

#-- Mains --#
def main_1joueur() -> None :
    # Variable d'Initialisation 
    run = True
    code_secret = genere_secret()

    while run :
        # Partie Joueur
        bp, mp = 0,0
        prop = lire_prop()
        bp, mp = bp_mp(prop, code_secret)
        if bp == TAILLE :
            print("Félicitation, vous avez trouvé le bon code !!!")
            run = False
        else :
            affiche_reponse(bp , mp)


def main_2joueurs() :
    # Variables d'Initialisastion
    run = True
    code1 = genere_secret()
    code2 = genere_secret()
    coups = 0
    bon = 0
    propsBot = [{"prop" : genere_secret()}]

    while run :
        # Partie Joueur
        print("-- Votre Tour --")
        bp, mp = 0,0
        prop = lire_prop()
        bp, mp = bp_mp(prop, code1)
        if bp == TAILLE :
            print("Félicitation, vous avez trouvé le bon code !!!")
            break
        else :
            affiche_reponse(bp , mp)
        bp, mp = 0,0
        
        # Partie Bot
        print("-- Tour du Bot --")
        bp, mp = bp_mp(propsBot[coups]["prop"], code2)
        propsBot[coups]["bp"] = bp 
        if bp == TAILLE :  
            print("Dommage, c'est perdu contre un bot plutôt nul en plus")
            run = False
        else :
            affiche_reponse(bp , mp)
        propsBot, bon = codeBot(propsBot, coups, bon)
        coups += 1
        
def Main() :
    resp = input("Voulez-vous jouer en mode 2joueurs(a) ou a 1joueur(b) ? ")
    if resp == "a" :
        return main_2joueurs()
    elif resp == "b" :
        return main_1joueur()
    else :
        print("Erreur mauvais choix !! ")
        return Main()
# -- FIN --#



#-- Bot --#        
def codeBot(props : list, coups : int, bon: int) -> (list[int], int) :
    if coups == 1 :
        prop = props[coups]["prop"]
        if prop[TAILLE - bon - 1] + 1 > MAX :
            prop[TAILLE - bon - 1] = 0
        else :
            prop[TAILLE - bon - 1] += 1
        props.append({"prop" : prop })
    elif props[coups]["bp"] == props[coups-1]["bp"] :
        prop = props[coups]["prop"]
        if prop[TAILLE - bon - 1] + 1 > MAX :
            prop[TAILLE - bon - 1] = 0
        else :
            prop[TAILLE - bon - 1] += 1
        props.append({"prop" : prop })
    elif props[coups]["bp"] > props[coups - 1]["bp"] :
        bon += 1
        prop = props[coups]["prop"]
        if prop[TAILLE - bon - 1] + 1 > MAX :
            prop[TAILLE - bon - 1] = 0
        else :
            prop[TAILLE - bon - 1] += 1
        props.append({"prop" : prop })
    else :
        prop = props[coups]["prop"]
        if prop[TAILLE - bon - 1] + 1 > MAX :
            prop[TAILLE - bon - 1] = 0
        else :
            prop[TAILLE - bon - 1] += 1
        props.append({"prop" : prop })
    return props, bon
#-- FIN --#



#-- TEST Bot --#
def TestBot() :
    run = True
    code = genere_secret()
    coups = 0
    bon = 0
    propsBot = [{"prop" : genere_secret()}]
    bp, mp = 0,0
    while run :
        bp, mp = bp_mp(propsBot[coups]["prop"], code)
        propsBot[coups]["bp"] = bp 
        if bp == TAILLE :  
            print(f"Le bot a trouvé en {coups} coups.")
            run = False
        else :
            affiche_reponse(bp , mp)
        propsBot, bon = codeBot(propsBot, coups, bon)
        coups += 1

#-- FIN --#

if __name__ == "__main__":
    Main()