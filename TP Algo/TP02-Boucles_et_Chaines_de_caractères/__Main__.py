def somme_chiffre(n : int) -> int :
    res = 0
    for i in str(n):
        res += int(i)
        
    return res

# Exercice 2

def nombre_ordonne(n : int) -> bool :
    s = "0"
    for e in str(n) :
        if int(e) < int(s) :
            return False
        s = e
    return True

# Exercice 3

def est_voyelle_min(l : str) -> bool:
    minu = "aeiouy"
    return True if l in minu else False

# Exercice 4

def est_voyelle_maj(l : str) -> bool :
    maj = "AEIOUY"
    return True if l in maj else False

# Exercice 5

def est_voyelle(l : str) -> bool :
    return True if est_voyelle_min(l) or est_voyelle_maj(l) else False

# Exercice 6

def compte_voyelle(m : str) -> int :
    res = 0
    for e in m :
        res += 1 if est_voyelle(e) else 0
    return res

# Exercice 7

def est_majuscule(l : str) -> bool :
    maj = "ABCDEFGHIJKLMNOPQRSTUVWYXZ"
    if l in maj :
        return True
    return False

# Exercice 8

def est_minuscule(l : str) -> bool :
    minu = "abcdefghijklmnopqrstuvwxyz"
    if l in minu :
        return True
    return False

# Exercice 9

def est_lettre(l : str) -> bool :
    return True if est_majuscule(l) or est_minuscule(l) else False

#Exercice 10

def compte_maj(m : str) -> int:
    res = 0
    for e in m:
        res += 1 if est_majuscule(e) else 0
    return res

# Exercice 11

def teste_mdp(mdp : str) -> bool :
    s = "+-@?!*$"
    c_s = False
    minu = False
    c = False
    for e in mdp :
        if e in s :
            c_s = True
        if est_minuscule(e):
            minu = True
        if str.isdigit(e) :
            c = True
    return True if compte_maj(mdp) > 0 and len(mdp) >= 8 and c_s and minu and c else False

# Exercice 12

def copie_sauf(m : str, l : str) -> str:
    t = ""
    for e in m :
        t += e if e != l else ""
    return t

# Exercice 13

def remplace(m : str, l : str, _l : str) -> str :
    t = ""
    for e in m :
        t += e if e != l else _l
    return t

# Exercice 14

def derniers(m : str, n : int) -> str:
    return m[len(m)-n:len(m)]

# Exercice 15

def min_to_maj(l : str):
    maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minu = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(maj) + 1) :
        if minu[i] == l :
            return maj[i]

#Exercice 16

def maj_to_min(l : str):
    maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minu = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(maj) + 1) :
        if maj[i] == l :
            return minu[i]

# Exercice 17

def majuscules(m : str):
    t = ""
    for e in m :
        if est_minuscule(e) :
            t += min_to_maj(e)
        else :
            t += e
    return t

def minuscules(m : str):
    t = ""
    for e in m :
        if est_majuscule(e) :
            t += maj_to_min(e)
        else :
            t += e
    return t


