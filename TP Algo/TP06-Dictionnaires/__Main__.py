# TPrix : dictionnaire dont la cl ́e est un article, la valeur son prix unitaire
# TPrix : dico(str : float)
lesPrix = {'perceuse':60,'ampoule':3.5,'clous':1.99,'vis':2.20}
# TStock : dictionnaire dont la cl ́e est un article, la valeur sa quantit ́e
# TStock : dico(str : int)
leStock = {'perceuse':15,'ampoule':75,'vis':300,'clous':400}

# Exercice 1

def informationsStocks(Stocks : dict, Prix : dict) -> tuple :
    prixTotal = 0
    quantité = 0
    for key in Stocks :
        if key not in Prix.keys() :
            prixTotal += Stocks[key]
        else :
            prixTotal += Prix[key] * Stocks[key]
            
        quantité += Stocks[key]
        
    return (prixTotal, quantité, prixTotal/quantité)
    
    
#Exercice 2

# TDepts : dictionnaire dont la cl ́e est un d ́epartement,
# la valeur les articles qu'il a en rayon (et leur quantit ́e)
# TDepts : dico(str : TStocks)
lesDepts = {'quincaillerie':leStock,'outillage':{'perceuse':5,'visseuse':8}}


def infoDepts(Depts : dict, Prix : dict) -> dict :
    dico = {}
    for key in Depts :
        dico[key] = informationsStocks(Depts[key], Prix)
        
    return dico

# Exercice 3


def indexDuMagasin(Depts : dict) -> dict :
    dico = {}
    for key, value in Depts.items() :
        for _key, _value in value.items():
            if _key in dico.keys() :
                dico[_key].append(key)
            else :
                dico[_key] = [key]
    return dico

#--------------------------------------------------------------------------------------------------------------------------------------------#


# -- TP6-b -- #
quatreQuarts = {'oeufs':4,'sucre':250,'farine':250,'beurre':250}
gateauChoc = {'oeufs':4,'sucre':150,'farine':80,'beurre':200,'chocolat':200}
lesRecettes = {'omelette' :{ 'oeufs': 4, 'lait (en cl)': 5},'soupe' : {'poireau': 4, 'pommes de terre': 2},'fondant au chocolat' : gateauChoc, 'quatre-quarts' : quatreQuarts}


laClassification = {'recettes végétariennes' : ['omelette', 'soupe'],
                    'entrées' : ['soupe'],
                    'desserts' : ['quatre-quarts', 'fondant au chocolat'] }



# Exercice 1
def recettePossible(frigo : dict, Recette : dict) -> bool :
    
    for key, value in Recette.items():
        if key not in frigo.keys() or value > frigo[key] :
            return False
    return True


#Exercice 2
def ajouteCourse(frigo : dict, courses : dict) -> dict :
    
    for k, v in courses.items():
        if k in frigo.keys() :
            frigo[k] += v
        else :
            frigo[k] = v
    return frigo


# Exercice 3
def recettesPossibles(frigo : dict, Recettes : dict) -> list :
    R_Possible = []
    for k, v in Recettes.items() :
        if recettePossible(frigo, v ) :
            R_Possible.append(k)
    return R_Possible


# Exercice 4
def cuisineRecette(frigo : dict, recette : dict) -> dict :
    
    for k, v in recette.items() :
        frigo[k] -= v
        if frigo[k] <= 0 :
            del frigo[k]
        
    return frigo


# Exercice 5
def cuisineLesRecettes(frigo : dict, recettes : dict) -> dict :
    for k, v in recettes.items() :
        frigo = cuisineRecette(frigo, v)
    return frigo


# Exercice 6
def coursesPourRecette(frigo : dict, recette : dict) -> dict :
    course = {}
    for k, v in recette.items() :
        if k not in frigo.keys() :
            course[k] = v
        elif v > frigo[k] :
            course[k] = v - frigo[k]
        
    return course


# Exercice 7
def toutesLesCourses(frigo : dict, recettes: dict) -> dict :
    course = {}
    for k, v in recettes.items() :
        for _k, _v in coursesPourRecette(frigo, v) :
            if _k in course.keys() :
                course[_k] += _v
            else :
                course[_k] = _v
    return courses


# Exercice 8
def lesIngredients(repas : list, recettes : dict) -> dict :
    Ingredient = {}
    
    for e in repas :
        for k, v in recettes[e].items() :
            if k in Ingredient.keys() :
                Ingredient[k] += v
            else :
                Ingredient[k] = v
    return Ingredient


# Exercice 9
def categoriesDUneRecette(recette : str, classi : dict) -> list :
    categories = []
    
    for k, v in classi.items() :
        if recette in v :
            categories.append(k)
    return categories


# Exercice 10
def recettesDUneCategorie(categ : str, classi : dict, repas : list) -> list :
    recette_categ = []
    for e in repas :
        if categ in categoriesDUneRecette(e, classi) :
            recette_categ.append(e)
    return recette_categ
    
    
# Exercice 11
def convient(rep : list, categ : list, classi : dict) -> bool :
    verif = False
    for k, v in classi.items() :
        for e in rep :
            if e in v :
                verif = True
        if not verif :
            return verif
        verif = False
    return True





