from string import ascii_letters, digits
ACCENTS = 'àâäèéêëîïòôöùûüç'
SYMBOLES = ',.!?:; \n\t&"\'@%+-/\\*_()[]{}'
ALPHABET = ascii_letters + ACCENTS + digits + SYMBOLES


def input_mode() -> str :
    res = input("Voulez-vous chiffrer ou déchiffrer un message (c/d) ? ")
    
    if res != "c" and res != "d" :
        print('Option Invalide !')
        return input_mode()
    return res

def input_cle() -> int :
    res = input("Entrez la clé de chiffrement (1-104) : ")
    if not res.isdigit() : 
        print('Option Invalide !')
        return input_cle()
    if res > len(ALPHABET) :
        print('Option Invalide !')
        return input_cle()
    return int(res)

def pos(c : str) -> int :
    for i in range(len(ALPHABET)) :
        if c == ALPHABET[i] :
            return i
    return -1
        
def car(n : int) -> str :
    return ALPHABET[n]
    
def chiffre_car(c : str, n : int) -> str :
    n_c = pos(c) + n
    if n_c >= len(ALPHABET) :
        n_c -= len(ALPHABET)
    return car(n_c)

def dechiffre_car(c : str, n : int) -> str :
    n_c = pos(c) - n
    if n_c > 0 :
        n_c -= len(ALPHABET)
    return car(n_c)

def cesar(message : str, mode : str, cle : int) -> str :
    res = ""
    if mode == "c" :
        for l in message :
            res += chiffre_car(l , cle)
    
    if mode == "d" :
        for l in message :
            res += dechiffre_car(l , cle)
    return res



def input_method() -> str :
    res = input("Quelle m ́ethode voulez-vous utiliser : Cesar (c) ou Vigenere (v) ? ")
    if res != "c" and res != "v" :
        print("Option Invalide !")
        return input_method()
    return res


def vigenere(message : str, mode : str, mot_cle : str) :
    res = ""
    i = 0
    if mode == "c" :
        for l in message :
            res += chiffre_car(l , pos(mot_cle[i]))
            i += 1
            if i >= len(mot_cle) :
                i = 0
    if mode == "d" :
        for l in message :
            res += dechiffre_car(l , pos(mot_cle[i]))
            i += 1
            if i > len(mot_cle) - 1 :
                i = 0
            
    return res

def main():
    message = input("Entrez votre message : \n")
    mode = input_mode()
    method = input_method()
    if method == "c" :
        cle = input_cle()
        print("Résultat : \n" + cesar(message, mode, cle))
    elif method == "v":
        cle = input("Entrez le mot_clé : ")
        print("Résultat : \n" + vigenere(message, mode, cle))
    