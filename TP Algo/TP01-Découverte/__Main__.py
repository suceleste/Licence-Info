import math



def etoile_six_branche (h) :
    return (((h**2*math.sqrt(3)) / 4) * 2) - (3*math.sqrt(3)*(h/3)**2)/2

def pot_peinture (largeur, longueur, hauteur, ULitre, litre) :
    return (((longueur * largeur) / ULitre) + ( (( largeur * hauteur ) / ULitre ) * 2 ) + ( (( longueur * hauteur ) / ULitre ) * 2 ) ) / litre

def annee_bisextile (annee : int) -> bool :
    
    if annee % 4 == 0 :
        if annee % 400 == 0 :
            return True
        elif annee % 100 == 0 :
            return False
        else :
            return True
    else :
        return False

def nbr_jours_mois (m : int, a : int) -> int :
    nbrJours = [31,28,31,30,31,30,31,31,30,31,30,31]
    return 29 if annee_bisextile(a) and m == 2 else nbrJours[m-1]


def numero_jour (j : int, m : int, a : int) -> int :
    jours = 0
    for i in range( 1, m ) :
        jours += nbr_jours_mois(i-1, a)
    return jours + j

def nbr_jours_debut_ere( a: int ) -> int :
    jours = 0
    for i in range(1, a+1):
        jours += 366 if annee_bisextile(i) else 365
        
    return jours

def nbr_jours_debut_ere_jma (j : int, m: int, a: int ) -> int :
    return nbr_jours_debut_ere(a-1) + numero_jour(j, m, a)

def nbr_jours_entre_deux_dates(j, m, a, _j, _m, _a) :
    return nbr_jours_debut_ere_jma(_j, _m, _a) - nbr_jours_debut_ere_jma(j, m, a)

def suivant_syracuse(n : int) -> int :
    return n/2 if n % 2 == 0 else 3*n+1

def nb_etapes_syracuse(n : int) -> int :
    e = 0
    while n > 1 :
        n = suivant_syracuse(n)
        e += 1
    return e

def altitude_syracuse(n : int) -> int :
    a = 0
    while n > 1 :
        if n > a :
            a = n
        n = suivant_syracuse(n)
    return a











