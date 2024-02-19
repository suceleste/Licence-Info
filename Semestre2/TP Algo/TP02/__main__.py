# -- Exercice 1 -- #
class Voiture() :
    def __init__(self, nom : str , couleur : str) -> None :
        self.__nom = nom
        self.__couleur = couleur
        self.__vitesse = 0

    def accelere(self, inc : int ) -> None:
        self.__vitesse += inc if inc <= 10 and self.__vitesse < 130 else 0

    def freine(self, dec : int) -> None :
        self.__vitesse -= dec if self.__vitesse > 0 else 0

    def str(self) -> str :
        return f"la {self.__nom} de couleur {self.__couleur} est à l'arrêt" if self.__vitesse <= 0 else f"la {self.__nom} de couleur {self.__couleur} est à {self.__vitesse} km/h"

    def affiche(self) -> None :
        print(self.str())


voiture = Voiture("Shelby", "rouge")
voiture2 = Voiture("Nissan GTR", 'noir')

voiture.accelere(10)
voiture.accelere(20)
voiture.freine(5)

voiture2.affiche()
voiture.affiche()



# -- Exercice 2 -- #

class CompteBancaire() :
    def __init__(self, nom : str, solde = 1000) -> None:
        self.__nom = nom
        self.__solde = solde 

    def depot(self, somme : float) -> None: 
        self.__solde += somme
    
    def retrait(self, somme : float) -> None : 
        self.__solde -= somme if somme <= self.__solde else 0
    
    def affiche(self) :
        print(f"le solde du compte bancaire de {self.__nom} est de {self.__solde}")

Compte1 = CompteBancaire('Michel')
Compte2 = CompteBancaire('Blanchard', 500)

Compte2.retrait(100)
Compte1.depot(100)

Compte1.affiche()
Compte2.affiche()




# -- Exercice 3 -- #

Points = {
    "7" : 0,
    "8" : 0,
    "9" : 0,
    "Valet" : 2,
    "Dame" : 3,
    "Roi" : 4,
    "10" : 10, 
    "As" : 11
}


class Carte() :
    def __init__(self, couleur : str, hauteur : str, atout = False) :
        self.__hauteur = hauteur
        self.__couleur = couleur
        self.__atout = atout

    def str(self) -> str :
        return f"{self.__hauteur} de {self.__couleur} "
    
    def affiche(self) -> None :
        print(self.str) 
    
    def couleur(self) -> str :
        return self.__couleur 

    def hauteur(self) -> str :
        return self.__hauteur
    
    def nbePoints(self) -> int :
        if self.__atout :
            if self.__hauteur == "Valet" :
                return 20
            elif self.__hauteur == "9" :
                return 14
            else :
                return Points[self.__hauteur]  if self.__hauteur in Points.keys() else int(self.__hauteur)
        else : 
            return Points[self.__hauteur] if self.__hauteur in Points.keys() else int(self.__hauteur)
        
    def estAtout(self) -> bool : 
        return self.__atout
    
    def est_plus_grand(self, c) -> bool :
        return True if self.nbePoints() > c.nbePoints() else False

    def est_egal(self, c) -> bool :
        return True if self.nbePoints() == c.nbePoints() else False
    

def affiche_jeu(jeu) :
    l = []
    for k in jeu :
        l.append(k.str())

    print(l)

