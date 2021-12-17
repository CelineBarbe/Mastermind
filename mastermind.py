import random
from termcolor import colored

def mm(niv = 4, coul = 6):
    # on laisse les valeurs par défaut dans les paramètres
    c = 1

    couleur_dict = {
        "nothing": "nothing", 
        "bleu": colored("bleu", "blue"), 
        "rouge": colored("rouge", "red"), 
        "jaune": colored("jaune", "yellow"), 
        "rose": colored("rose", "magenta"), 
        "vert": colored("vert", "green"), 
        "cyan": colored("cyan", "cyan"), 
        "blanc": colored("blanc", "white"), 
        "noir": colored("noir", "grey", "on_white")
    }

    couleurs = list(couleur_dict.keys())
    couleurs_colorees = list(couleur_dict.values())

    str_couleurs = " ".join(couleurs_colorees[1:coul+1])

    secret = [random.choice(couleurs[1:coul+1]) for i in range(niv)]
    
    secret_colore_lst = []
    for j in secret:
        secret_colore_lst.append(couleur_dict[j])

    secret_colore_str = " ".join(secret_colore_lst)

    while True:
        code = list(secret)
        saisie = (input(f"Entrez {niv} couleurs parmi les suivantes : {str_couleurs}, séparées par un espace. Essai n° {c} : "))
        essai = saisie.split(" ")
        # le joueur entre sa combinaison ou peut abandonner en ne rentrant rien.
        if len(essai) < niv: 
            print(f"Perdu... La combinaison était : {secret_colore_str}")
            break
        c += 1
        bien, mal = 0, 0
        for i,v in enumerate(essai):
            if v == code[i]: 
                bien += 1
                essai[i] = "#"
                code[i] = "*"
        if bien == niv: 
            print("Gagné!")
            break
        for i, v in enumerate(essai):
            if v in code: 
                mal =+ 1
                code[code.index(v)] = "*"
        print(f"Bien : {bien} , Mal : {mal}")

# maximum 8 couleurs
mm(4,6)        
