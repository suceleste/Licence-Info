# Descamps Sullyvan
# groupe TD4-2
#######################
# importations
#######################
from mots import MOTS
from figures_pendu import FIGURES_PENDU
import random
#######################
# fonctions
#######################

def choisit_mot(l : list) -> str :
    """
    La fonction prend une liste de mot et Retourne un mot choisit aléatoirement.
    
    Parameters
    ----------
    l : list
        liste de mots dans laquelle choisir un mot.
    """
    
    return l[random.randint(0, len(l)-1)]



def est_dans(c : str, p : str) -> bool :
    """
    La fonction utilise un caractere et une chaine de caractères et Retourne si le caractère se trouve dans la chaine de caractères.
    
    Parameters
    ----------
    c : str
        caractère a retrouver dans la chaîne de caratère.
    p : str
        mot dans lequelle chercher le caractère.
    """
    
    for i in range(len(p)) :
        if p[i] == c :
            return True
    return False



def input_lettre(props : str) -> str :
    """
    fonction qui demande une lettre, vérifié que c'est bien une lettre, et Retourne cette lettre.
    
    Parameters
    ----------
    props : str
        str qui contient toutes les lettres essayer.
    """

    l = input("\nProposez une lettre : ")
    if l.isdigit() :
        print(f"{l} n’est pas une lettre.")
        return input_lettre(props)
    elif len(l) > 1 :
        print("Proposez une seule lettre, s’il vous plaît.")
        return input_lettre(props)
    elif est_dans(l, props) : # est_dans
        print("Vous avez déjà proposé cette lettre.")
        return input_lettre(props)
    else :
        return l
    
    
    
def dessine_pendu(n : int) -> None :
    """
    La fonction prend un entier est affiche le pendu correspondant.
    
    Parameters
    ----------
    n : int
        nombre entier correspondant au nombre d'erreurs.
    """
    
    print(FIGURES_PENDU[n])
    
    
    
def affiche_erreurs(erreurs : str) -> None :
    """
    La fonction prend les erreurs et les affiches.
    
    Parameters
    ----------
    erreurs : str
        chaîne de caractères contenant les lettres erreurs.
    """
    
    print(f"Erreurs : \n {erreurs}")
    
    
    
def affiche_correctes(correctes : str, mot_secret : str) -> None :
    """
    La fonction prend deux chaines de caracteres et affiche les lettres du mot secret se trouvant dans la chaîne de caractères correcte.
    
    Parameters
    ----------
    correctes : str
        chaines de caractères contenant les propositions de lettre du joueur.
    mot_secret : str
        chaîne de caractères contenant le mot du jeu.
    """
    
    for i in range(len(mot_secret)) : # index
        if est_dans(mot_secret[i], correctes) : # est_dans
            print(mot_secret[i], end=" ")
        else :
            print("_", end=" ")
    print("\n")
            
            
            
def gagne(p : str, mot_secret : str) -> bool :
    """
    La fonction prend deux chaines de caractères et retourne True si c'est gagner et False si il n'y a toujours pas les bonnes lettres.
    
    Parameters
    ----------
    p : str
        chaines de caractères contenant toutes les lettres proposées.
    mot_secret : str
        chaîne de caractères contenant le mot du jeu.
    """
    
    for i in range(len(mot_secret)) : # index
        if not est_dans(mot_secret[i], p) : # est_dans
            return False
    return True



def Main() -> None :
    """ Fonction Principal exécutant toutes les fonctions dans le bonne ordre pour faire marcher le jeu"""
    
    ERREUR = ""
    mot = choisit_mot(MOTS)
    props = ""
    
    while len(ERREUR) < len(FIGURES_PENDU) and not gagne(props, mot):
        print(len(ERREUR))
        dessine_pendu(len(ERREUR))
        affiche_erreurs(ERREUR)
        affiche_correctes(props, mot)
        props += input_lettre(props)
        ERREUR += props[-1] if not est_dans(props[-1], mot) else ""
        
    if gagne(props, mot) :
        print("Félicitation, tu as gagné !!")
    else :
        print("Dommage, Tu as perdu.")
        
    print(f"Le mot secret : \n {mot}")
        
        
        
    
