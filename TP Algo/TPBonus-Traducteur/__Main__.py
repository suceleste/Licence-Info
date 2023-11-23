Traducteur = {
    "chat" : "cat",
    "chien" : "dog",
    "maison" : "house",
    "voiture" : "car",
    "ordinateur" : "computer",
    "jardin" : "garden",
    "école" : "school",
    "banane" : "banana",
    "plage" : "beach",
    "musique" : "music",
    "livre" : "book",
    "pont" : "bridge",
    "cadeau" : "gift",
    "fleur" : "flower",
    "montagne" : "mountain",
    "rivière" : "river",
    "soleil" : "sun",
    "lune" : "moon",
    "étoile" : "star",
    "aventure" : "adventure"
    }


def est_un_mot(m : str) -> bool :
    Alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZéè"
    
    for l in m :
        if l not in Alphabet :
            return False
    return True

def lire_mot() -> str :
    mot = input("Veuillez rentrez un mot : ")
    if not est_un_mot(mot) :
        print("Mot Incorrect !!!\n")
        return lire_mot()
    return mot

def lire_Traduit() -> str :
    mot = input("Veuillez rentrez sa traduction : ")
    if not est_un_mot(mot) :
        print("Mot Incorrect !!!\n")
        return lire_mot()
    return mot

def Enrichir_traducteur(motSource : str, motTraduit : str) -> dict :
    if motSource not in Traducteur.keys() or motTraduit not in Traducteur.values() :
        Traducteur[motSource]  = motTraduit
    return Traducteur

def lettre_mot(mot : str) -> dict :
    dico =  {}
    for l in mot :
        if l not in dico.keys() :
            dico[l] = 1
        else :
            dico[l] += 1
    return dico

def pseudo_similaire(motSource : str, motTraduit : str) -> bool :
    diff = 0
    if len(motSource) - 1 <= len(motTraduit) <= len(motSource) + 1 :
        dictSource = lettre_mot(motSource)
        dictTraduit = lettre_mot(motTraduit)
        for key, value in dictTraduit.items() :
            if key in dictSource.keys() and value != dictSource[key] :
                diff += abs(value - dictSource[key])
            if key not in dictSource.keys() :
                diff += value
    else :
        diff += 2
    return True if diff <= 1 else False

def lesmot_similaires() -> list :
    l = []
    
    for key, value in Traducteur.items() :
        if pseudo_similaire(key, value) :
            l.append({key : value})
    return l

def Trier_Traducteur() -> list :
    li = []
    for key, value in Traducteur.items() :
        li.append(key)  
    return sorted(li)

def Traducteur_Inverse(Traducteur : dict) -> dict :
    TInverse = {}
    for k, v in Traducteur.items() :
        TInverse[v] = k
    return TInverse

def Main() :
    mot = lire_mot()
    traduit = lire_Traduit()
    Enrichir_traducteur(mot, traduit)
    for e in lesmot_similaires():
        print(e, end=", ")
    print("\n\n-Traducteur Trier : ")
    for k in Trier_Traducteur() :
        print(k , end=", ")
    print("\n\n-Traducteur Inverse : ")
    for k, v in Traducteur_Inverse(Traducteur).items() :
        print(k + " = "+ v)

if __name__ == "__main__" : 
    Main()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    